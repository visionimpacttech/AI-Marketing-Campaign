# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('simulated_customer_data.csv')  # Make sure this file exists
print("First 5 rows of the dataset:")
print(data.head())

print("\nBasic Statistics:")
print(data[['click_rate', 'open_rate', 'engagement_time']].describe())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nData Types:")
print(data.dtypes)

plt.hist(data['click_rate'], bins=10, alpha=0.7, label='Click Rates')
plt.xlabel('Click Rate')
plt.ylabel('Number of Customers')
plt.title('Distribution of Click Rates')
plt.legend()
plt.show()

plt.hist(data['open_rate'], bins=10, alpha=0.7, label='Open Rates', color='orange')
plt.xlabel('Open Rate')
plt.ylabel('Number of Customers')
plt.title('Distribution of Open Rates')
plt.legend()
plt.show()


engagement_counts = data['engagement_time'].value_counts().sort_index()

engagement_counts.plot(kind='bar', alpha=0.7)
plt.xlabel('Engagement Time (Hour of the Day)')
plt.ylabel('Number of Customers')
plt.title('Distribution of Engagement Times')
plt.show()

platform_stats = data.groupby('platform')[['click_rate', 'open_rate']].mean()
print("\nAverage Click and Open Rates by Platform:")
print(platform_stats)

platform_stats.plot(kind='bar', alpha=0.7)
plt.xlabel('Platform')
plt.ylabel('Average Rate')
plt.title('Average Click and Open Rates by Platform')
plt.show()

correlation = data[['click_rate', 'open_rate']].corr()
print("\nCorrelation Between Click Rate and Open Rate:")
print(correlation)
