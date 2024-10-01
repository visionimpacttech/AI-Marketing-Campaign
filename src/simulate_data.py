import pandas as pd
import numpy as np

# Step 1: Simulate Data

num_customers = 100

engagement_times = ['09:00', '12:00', '15:00', '18:00']
platforms = ['email', 'social_media']

customer_ids = np.arange(1, num_customers + 1)

click_rates = np.random.uniform(0.1, 1.0, size=num_customers)
open_rates = np.random.uniform(0.1, 1.0, size=num_customers)


engagement_times_random = np.random.choice(engagement_times, size=num_customers)
platforms_random = np.random.choice(platforms, size=num_customers)

data = pd.DataFrame({
    'customer_id': customer_ids,
    'click_rate': click_rates,
    'open_rate': open_rates,
    'engagement_time': engagement_times_random,
    'platform': platforms_random
})

data.to_csv('customer_engagement_data.csv', index=False)
print("Simulated Data:")
print(data.head())  

# Step 2: Clean and Organize Data

# Load the simulated customer engagement data
data = pd.read_csv('customer_engagement_data.csv')


print("\nMissing values per column:")
print(data.isnull().sum())  # Check for missing values


data = data.fillna({
    'click_rate': 0.0,  
    'open_rate': 0.0,   
    'engagement_time': '09:00',  
    'platform': 'email' 
})


data['click_rate'] = data['click_rate'].astype(float)
data['open_rate'] = data['open_rate'].astype(float)
data['engagement_time'] = data['engagement_time'].astype(str)
data['platform'] = data['platform'].astype(str)


data.to_csv('cleaned_customer_engagement_data.csv', index=False)

print("\nCleaned Data:")
print(data.head()) 
