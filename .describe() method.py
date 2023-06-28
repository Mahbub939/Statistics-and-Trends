Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

import pandas as pd

# Assuming you have already loaded the climate change data into a pandas DataFrame
... 
... # Selecting the indicators of interest
... indicators_of_interest = ['Access to Electricity', 'Agricultural Activity', 'Urban Population']
... 
... # Selecting a few countries for comparison
... countries_of_interest = ['Country A', 'Country B', 'Country C']
... 
... # Filtering the DataFrame to include only the selected indicators and countries
... filtered_df = original_df.loc[original_df['Indicator'].isin(indicators_of_interest) &
...                               original_df['Country'].isin(countries_of_interest)]
... 
... # Using .describe() method to get summary statistics for the selected indicators
... summary_stats = filtered_df.groupby('Indicator').describe()
... 
... # Additional statistical methods
... # Method 1: Correlation between indicators for each country
... correlation_by_country = filtered_df.groupby('Country')[indicators_of_interest].corr()
... 
... # Method 2: Mean and standard deviation for each indicator across all countries
... mean_values = filtered_df.groupby('Indicator')[countries_of_interest].mean()
... std_dev_values = filtered_df.groupby('Indicator')[countries_of_interest].std()
... 
... # Printing the summary statistics
... print("Summary Statistics:")
... print(summary_stats)
... 
... print("\nCorrelation between Indicators by Country:")
... print(correlation_by_country)
... 
... print("\nMean Values across Countries:")
... print(mean_values)
... 
... print("\nStandard Deviation across Countries:")
... print(std_dev_values)
