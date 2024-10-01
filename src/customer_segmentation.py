import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv('cleaned_customer_engagement_data.csv')


print("Preview of Cleaned Data:")
print(data.head())


X = data[['click_rate', 'open_rate']]

# Define the number of clusters (in this case, 3 segments)
kmeans = KMeans(n_clusters=3, random_state=42)
data['segment'] = kmeans.fit_predict(X)


# This shows customer IDs with their corresponding segments
print("\nSegmented Data:")
print(data[['customer_id', 'click_rate', 'open_rate', 'segment']].head())


# Plot click_rate vs open_rate, and color the points by their segment
plt.scatter(data['click_rate'], data['open_rate'], c=data['segment'], cmap='viridis')
plt.xlabel('Click Rate')
plt.ylabel('Open Rate')
plt.title('Customer Segments Based on Click and Open Rates')
plt.show()


# This will save the data with the new 'segment' column to a file called 'segmented_customer_data.csv'
data.to_csv('segmented_customer_data.csv', index=False)

print("\nSegmented data saved to 'segmented_customer_data.csv'.")
