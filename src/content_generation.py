import pandas as pd
import numpy as np
import openai
import time

# Step 1: Set up your OpenAI API key
openai.api_key = 'your-openai-api-key'

# Step 2: Load Segmented Data
segmented_data = pd.read_csv('segmented_customer_data.csv')
print("Segmented Customer Data:")
print(segmented_data.head())

# Step 3: Generate Marketing Content for Each Segment
def generate_marketing_content(segment):
    if segment == 0:
        prompt = "Generate a personalized email for frequent buyers of electronics. Offer them a 20% discount."
    elif segment == 1:
        prompt = "Create a welcome email for a new customer interested in fitness products. Offer a 10% discount."
    elif segment == 2:
        prompt = "Generate a reminder email for a customer who rarely buys. Offer a 15% discount."
    else:
        prompt = "Generate a personalized email for a frequent browser who hasn't made a purchase."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful marketing assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].message["content"].strip()
    except openai.error.RateLimitError as e:
        print(f"Rate limit error: {e}")
        return "Rate limit exceeded. Try again later."

segmented_data['generated_content'] = segmented_data['segment'].apply(generate_marketing_content)
time.sleep(1)  # Add 1-second delay to avoid rate-limiting

segmented_data.to_csv('personalized_marketing_content.csv', index=False)

# Step 4: Load additional engagement data
engagement_data = pd.read_csv('customer_engagement_data.csv')

# Display available columns for debugging
print("Available columns in engagement_data:", engagement_data.columns)

# Step 5: Merge the datasets
merged_data = pd.merge(segmented_data, engagement_data, on='customer_id')

# Step 6: Check for missing columns and create them if necessary
required_columns = ['click_rate', 'open_rate', 'conversion_rate']

for col in required_columns:
    if col not in merged_data.columns:
        print(f"Column {col} not found. Creating mock data for {col}.")
        merged_data[col] = np.random.rand(len(merged_data))

# Step 7: Calculate performance metrics
segment_performance = merged_data.groupby('segment').agg({
    'click_rate': 'mean',
    'open_rate': 'mean',
    'conversion_rate': 'mean'
})

print("Segment Performance Metrics:")
print(segment_performance)

# Step 8: Optimize Timing and Channels
best_time = merged_data.groupby('segment').agg({
    'engagement_time': lambda x: x.value_counts().idxmax() if 'engagement_time' in merged_data.columns else 'No data',
    'platform': lambda x: x.value_counts().idxmax() if 'platform' in merged_data.columns else 'No data'
})

print("Optimal Engagement Times and Platforms for Each Segment:")
print(best_time)

# Step 9: Real-time Monitoring and Adaptation
def monitor_and_adapt(campaign_data):
    for index, row in campaign_data.iterrows():
        if row['click_rate'] < 0.1:
            print(f"Segment {row['segment']}: Low click rate, trying a different platform or content.")
            row['platform'] = 'social_media'  # Example adaptation
        else:
            print(f"Segment {row['segment']}: Campaign performing well.")
        time.sleep(2)  # Simulate delay

monitor_and_adapt(merged_data)

# Step 10: Save final performance report
merged_data.to_csv('final_campaign_performance.csv', index=False)
