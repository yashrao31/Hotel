import streamlit as st 
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Hotel Cancellation Prediction")

st.subheader("This is a simple application to predict hotel cancellations based on historical data.")
# Load the dataset
df = pd.read_csv("hotel_bookings 2.csv")
# Display the shape of the dataset
st.write(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")
# replace the low requency values in the 'country' column with 'Other'
st.write("Replacing low frequency values(< 1000) in the 'country' column with 'Other'...")
country_counts = df['country'].value_counts()
low_frequency_countries = country_counts[country_counts < 1000].index
df['country'] = df['country'].replace(low_frequency_countries, 'Other')

# Dispay all unique values in the 'hotel' column
st.subheader("Unique values in the 'hotel' column:")
hotel = st.sidebar.multiselect("Select a hotel:", df['hotel'].unique())

# display all unique value arival_date_year in the 'arrival_date_year' column
year = arrival_date_years = df['arrival_date_year'].unique()
year = st.sidebar.multiselect("Select a year:", arrival_date_years)

# filter the data based on the selected year
df = df[df['arrival_date_year'].isin(year)] if year else df

# Filter the dataset based on the selected hotel
df = df[df['hotel'].isin(hotel)] if hotel else df


st.subheader("Dataset Preview")
st.dataframe(df.head())
# Display basic statistics
st.subheader("Basic Statistics")
st.write(df.describe())
# remove highly null values column
st.write("Removing columns with high percentage of null values...")
st.write("Columns 'company' and 'agent' have a high percentage of null values and will be removed.")
df = df.drop(columns=['company', 'agent'])
# remobe the rows with null values
st.subheader("Removing rows with null values...")
df = df.dropna()
# remove the duplicate rows
st.subheader("Removing duplicate rows...")
df = df.drop_duplicates()
# Display the null values in the dataset
st.subheader("Null values in the dataset:")
st.write(df.isnull().sum())
# Display the number of unique values in each column
st.subheader("Number of unique values in each column:")
st.write(df.nunique())
# Display the number of cancellations
cancellation_counts = df['is_canceled'].value_counts()
st.subheader("Number of cancellations vs non-cancellations:")
st.bar_chart(cancellation_counts)
# Display the cacellation percantage
cancellation_percentage = (cancellation_counts[1] / cancellation_counts.sum()) * 100
st.write(f"Percentage of cancellations: {cancellation_percentage:.2f}%")

# Display the number of unique values in the 'country' column after replacement
st.write("Number of unique values in the 'country' column after replacement:")
st.write(df['country'].nunique())

# Display the number of cancellations by country
cancellations_by_country = df[df['is_canceled'] == 1]['country'].value_counts()
st.subheader("Number of cancellations by country:") 
st.bar_chart(cancellations_by_country)

# Display the top three countries in terms of the number of bookings
top_countries = df['country'].value_counts().head(3)
st.write("Top three countries in terms of the number of bookings:")
st.write(top_countries)

# Display the cancellations for top three countries
cancellations_by_top_countries = df[df['is_canceled'] == 1]['country'].value_counts().loc[top_countries.index]
st.write("Percentage of cancellations for top three countries:")
st.write(cancellations_by_top_countries)

st.write("The majority of cancellations come from Portugal, Spain and Great Britain, which are the top three countries in terms of the number of bookings. This could be due to various factors such as travel restrictions, weather conditions, or changes in travel plans in these countries.")

# Display the number of cancellations by month
cancellations_by_month = df[df['is_canceled'] == 1]['arrival_date_month'].value_counts()
st.subheader("Number of cancellations by month:") 
st.bar_chart(cancellations_by_month)

st.write("The number of cancellations is higher in the months of August, September and October, which are the peak tourist season in Portugal. This could be due to various factors such as weather conditions, travel restrictions, or changes in travel plans during these months.")

# Display the number of cancellations by market segment
cancellations_by_market_segment = df[df['is_canceled'] == 1]['market_segment'].value_counts()
st.subheader("Number of cancellations by market segment:")  
st.bar_chart(cancellations_by_market_segment)

st.write("The majority of cancellations come from the 'Online TA' market segment, which includes bookings made through online travel agencies. This could be due to various factors such as changes in travel plans, better cancellation policies offered by online travel agencies, or increased competition among hotels in this market segment.")

# Display the number of cancellations by distribution channel
cancellations_by_distribution_channel = df[df['is_canceled'] == 1]['distribution_channel'].value_counts()
st.subheader("Number of cancellations by distribution channel:")    
st.bar_chart(cancellations_by_distribution_channel)

st.write("The majority of cancellations come from the 'TA/TO' distribution channel, which includes bookings made directly with the hotel. This could be due to various factors such as changes in travel plans, better cancellation policies offered by the hotel, or increased competition among hotels in this distribution channel.")

# Display the number of cancellations by deposit type
cancellations_by_deposit_type = df[df['is_canceled'] == 1]['deposit_type'].value_counts()
st.subheader("Number of cancellations by deposit type:")    
st.bar_chart(cancellations_by_deposit_type)

st.write("The majority of cancellations come from the 'No Deposit' deposit type, which includes bookings that do not require a deposit. This could be due to various factors such as changes in travel plans, better cancellation policies offered by the hotel for this deposit type, or increased competition among hotels in this deposit type.")
# Display the number of cancellations by customer type
cancellations_by_customer_type = df[df['is_canceled'] == 1]['customer_type'].value_counts()
st.subheader("Number of cancellations by customer type:")   
st.bar_chart(cancellations_by_customer_type)
st.write("The majority of cancellations come from the 'Transient' customer type, which includes bookings made by individual customers. This could be due to various factors such as changes in travel plans, better cancellation policies offered by the hotel for this customer type, or increased competition among hotels in this customer type.")

# Dispay the number of cancellationn in PRT,ESP and GBR countries
cancellations_by_country_specific = df[df['is_canceled'] == 1]['country'].value_counts().loc[['PRT', 'ESP', 'GBR']]
st.subheader("Number of cancellations in PRT, ESP and GBR countries:")
st.bar_chart(cancellations_by_country_specific)
st.write("The majority of cancellations come from Portugal, Spain and Great Britain, which are the top three countries in terms of the number of bookings. This could be due to various factors such as travel restrictions, weather conditions, or changes in travel plans in these countries.")

# Display the number of cancellations by month for PRT, ESP and GBR countries
cancellations_by_month_specific = df[df['is_canceled'] == 1][df['country'].isin(['PRT', 'ESP', 'GBR'])]['arrival_date_month'].value_counts()
st.subheader("Number of cancellations by month for PRT, ESP and GBR countries:")
st.bar_chart(cancellations_by_month_specific)

# Dispay the average adr per month for PRT, ESP and GBR countries
average_adr_by_month_specific = df[df['country'].isin(['PRT', 'ESP', 'GBR'])].groupby('arrival_date_month')['adr'].mean()
st.subheader("Average ADR by month for PRT, ESP and GBR countries:")
st.write(average_adr_by_month_specific)

st.write("The number of cancellations is higher in the months of August, July and June, which are the peak tourist season in Portugal. This could be due to various factors such as weather conditions, travel restrictions, or changes in travel plans during these months.")

# Display the number not canceled bookings by month for PRT, ESP and GBR countries
not_canceled_by_month_specific = df[df['is_canceled'] == 0][df['country'].isin(['PRT', 'ESP', 'GBR'])]['arrival_date_month'].value_counts()
st.subheader("Number of not canceled bookings by month for PRT, ESP and GBR countries:")
st.bar_chart(not_canceled_by_month_specific)
st.write("The number of not canceled bookings is higher in the months of August, July and October, which are the peak tourist season in Portugal. This could be due to various factors such as weather conditions, travel restrictions, or changes in travel plans during these months.") 

# Display the number of cancellations by market segment for PRT, ESP and GBR countries
cancellations_by_market_segment_specific = df[df['is_canceled'] == 1][df['country'].isin(['PRT', 'ESP', 'GBR'])]['market_segment'].value_counts()
st.subheader("Number of cancellations by market segment for PRT, ESP and GBR countries:")
st.bar_chart(cancellations_by_market_segment_specific)
st.write("The majority of cancellations come from the 'Online TA' market segment, which includes bookings made through online travel agencies. This could be due to various factors such as changes in travel plans, better cancellation policies offered by online travel agencies, or increased competition among hotels in this market segment.")

# Display the number of cancellations by distribution channel for PRT, ESP and GBR countries
cancellations_by_distribution_channel_specific = df[df['is_canceled'] == 1][df['country'].isin(['PRT', 'ESP', 'GBR'])]['distribution_channel'].value_counts()
st.subheader("Number of cancellations by distribution channel for PRT, ESP and GBR countries:")
st.bar_chart(cancellations_by_distribution_channel_specific)
st.write("The majority of cancellations come from the 'Direct' distribution channel, which includes bookings made directly with the hotel. This could be due to various factors such as changes in travel plans, better cancellation policies offered by the hotel, or increased competition among hotels in this distribution channel.")

# Find the correlation between the number of cancellations and the average daily rate (adr) for PRT, ESP and GBR countries
correlation_cancellations_adr = df[df['country'].isin(['PRT', 'ESP', 'GBR'])].groupby('arrival_date_month')[['is_canceled', 'adr']].mean().corr().iloc[0, 1]
st.subheader("Correlation between the number of cancellations and the average daily rate (adr) for PRT, ESP and GBR countries:")
st.scatter_chart(df[df['country'].isin(['PRT', 'ESP', 'GBR'])].groupby('arrival_date_month')[['is_canceled', 'adr']].mean().reset_index(), x='adr', y='is_canceled')
st.write(f"The correlation between the number of cancellations and the average daily rate (adr) for PRT, ESP and GBR countries is {correlation_cancellations_adr:.2f}. A positive correlation indicates that as the average daily rate increases, the number of cancellations also increases. This could be due to various factors such as changes in travel plans, better cancellation policies offered by the hotel, or increased competition among hotels in this market segment.")      

# Find the correlation between the number of cancellations and the lead time for PRT, ESP and GBR countries
correlation_cancellations_lead_time = df[df['country'].isin(['PRT', 'ESP', 'GBR'])].groupby('arrival_date_month')[['is_canceled', 'lead_time']].mean().corr().iloc[0, 1]
st.subheader("Correlation between the number of cancellations and the lead time for PRT, ESP and GBR countries:")
st.scatter_chart(df[df['country'].isin(['PRT', 'ESP', 'GBR'])].groupby('arrival_date_month')[['is_canceled', 'lead_time']].mean().reset_index(), x='lead_time', y='is_canceled')
st.write(f"The correlation between the number of cancellations and the lead time for PRT, ESP and GBR countries is {correlation_cancellations_lead_time:.2f}. A positive correlation indicates that as the lead time increases, the number of cancellations also increases. This could be due to various factors such as changes in travel plans, better cancellation policies offered by the hotel, or increased competition among hotels in this market segment.")    


# Find the cancellation rate after filtering  the top three countries (PRT, ESP, GBR)
top_countries_filtered = df[df['country'].isin(['PRT', 'ESP', 'GBR'])]
cancellation_rate_filtered = (top_countries_filtered['is_canceled'].sum() / top_countries_filtered.shape[0]) * 100
st.subheader("Cancellation rate after filtering the top three countries (PRT, ESP, GBR):")
st.write(f"The cancellation rate after filtering the top three countries (PRT, ESP, GBR) is {cancellation_rate_filtered:.2f}%. This indicates that the majority of cancellations come from these three countries, which could be due to various factors such as travel restrictions, weather conditions, or changes in travel plans in these countries.")       

# Find the shape of data after removing the top three countries (PRT, ESP, GBR)
data_without_top_countries = df[~df['country'].isin(['PRT', 'ESP', 'GBR'])]
st.subheader("Shape of data after removing the top three countries (PRT, ESP, GBR):")
st.write(f"The shape of the data after removing the top three countries (PRT, ESP, GBR) is {data_without_top_countries.shape}. This indicates that a significant portion of the data is from these three countries, and removing them has a noticeable impact on the dataset.")     

st.subheader("Conclusion")
st.write("In conclusion, the analysis of hotel cancellations reveals that the majority of cancellations come from Portugal, Spain and Great Britain, which are the top three countries in terms of the number of bookings. The number of cancellations is higher in the months of August, September and October, which are the peak tourist season in Portugal. The majority of cancellations come from the 'Online TA' market segment and the 'TA/TO' distribution channel. The majority of cancellations come from the 'No Deposit' deposit type and the 'Transient' customer type. The correlation between the number of cancellations and the average daily rate (adr) for PRT, ESP and GBR countries is positive, indicating that as the average daily rate increases, the number of cancellations also increases. The correlation between the number of cancellations and the lead time for PRT, ESP and GBR countries is also positive, indicating that as the lead time increases, the number of cancellations also increases.")        

#find the correlation between the number of cancellations and the average daily rate (adr) for the entire dataset
correlation_cancellations_adr_entire = df.groupby('arrival_date_month')[['is_canceled', 'adr']].mean().corr().iloc[0, 1]
st.subheader("Correlation between the number of cancellations and the average daily rate (adr) for the entire dataset:")
st.scatter_chart(df.groupby('arrival_date_month')[['is_canceled', 'adr']].mean().reset_index(), x='adr', y='is_canceled')
st.write(f"The correlation between the number of cancellations and the average daily rate (adr) for the entire dataset is {correlation_cancellations_adr_entire:.2f}. A positive correlation indicates that as the average daily rate increases, the number of cancellations also increases. This could be due to various factors such as changes in travel plans, better cancellation policies offered by the hotel, or increased competition among hotels in this market segment.")



