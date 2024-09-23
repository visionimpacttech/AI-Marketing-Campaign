def adapt_campaign_performance(feedback):
    # Adjust based on real-time feedback data
    if feedback['click_rate'] > 0.5:
        return "Increase frequency of campaign"
    else:
        return "Lower frequency and test content variation"

# Example feedback loop
feedback = {'click_rate': 0.6}
print(adapt_campaign_performance(feedback))
