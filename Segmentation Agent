import pandas as pd
from sklearn.cluster import KMeans

def segment_customers(data):
    kmeans = KMeans(n_clusters=3)
    data['segment'] = kmeans.fit_predict(data)
    return data

# Load customer data and segment
data = pd.read_csv('data/customer_data.csv')
segmented_data = segment_customers(data)
print(segmented_data)
