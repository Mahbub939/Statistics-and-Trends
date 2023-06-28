Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import pandas as pd
... import matplotlib.pyplot as plt
... 
... # Assuming you have already loaded the climate change data into a pandas DataFrame
... 
... # Selecting the indicators of interest
... indicators_of_interest = ['Population Growth', 'Energy Consumption']
... 
... # Filtering the DataFrame to include only the selected indicators
... filtered_df = original_df.loc[original_df['Indicator'].isin(indicators_of_interest)]
... 
... # Grouping the data by country and calculating correlations between indicators
... correlation_by_country = filtered_df.groupby('Country')[indicators_of_interest].corr()
... 
... # Grouping the data by year and calculating correlations between indicators
... correlation_by_year = filtered_df.groupby('Year')[indicators_of_interest].corr()
... 
... # Visualizing correlations by country
... correlation_by_country.plot(kind='bar', figsize=(10, 6))
... plt.title('Correlations between Indicators by Country')
... plt.xlabel('Country')
... plt.ylabel('Correlation Coefficient')
... plt.legend(indicators_of_interest)
... plt.show()
... 
... # Visualizing correlations over time
... correlation_by_year.unstack().plot(kind='line', figsize=(10, 6))
... plt.title('Correlations between Indicators over Time')
... plt.xlabel('Year')
... plt.ylabel('Correlation Coefficient')
... plt.legend(indicators_of_interest)
... plt.show()
