import pandas as pd
import numpy as np

df = pd.read_csv('AQI_Data.csv')
print("First 5 rows of the dataset:")
print(df.head(5))
print("\n")
print("Last 6 rows of the dataset:")
print(df.tail(6))
print("\n")

summary_stats = df.describe()
print("Summary stats for the data:")
print(summary_stats)
print("\n")

selected_columns = df[['City', 'AQI', 'PM2.5', 'PM10']]
grouped = selected_columns.groupby('City')
result = grouped.mean()
print("Mean of AQI, PM2.5 & PM10 values of cities:")
print(result)
print("\n")

missing_values = df.isnull().sum()
print("Missing Values in Each Column:")
print(missing_values)
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
print("Updated dataframe:")
print(df)
print("\n")

aqi_values = df['AQI'].to_numpy()
print("AQI values extracted ..")
print(aqi_values)
print("\n")

mean_aqi = np.mean(aqi_values)
median_aqi = np.median(aqi_values)
std_dev_aqi = np.std(aqi_values)

print(f"Mean of AQI values: {mean_aqi}")
print(f"Median of AQI values: {median_aqi}")
print(f"Standard Deviation of AQI values: {std_dev_aqi}")

