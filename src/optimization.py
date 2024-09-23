import numpy as np

def optimize_campaign(engagement_data):
    optimal_time = np.argmax(engagement_data)
    return f"Optimal time for campaign: {optimal_time} PM"

# Example engagement data
engagement_data = np.array([0.25, 0.5, 0.3, 0.8])
print(optimize_campaign(engagement_data))
