# In the stock market, perception can be as powerful as the numbers. 
# Smart investors know it’s not just about the figures, but the stories, 
# the news, and the buzz shaping the market.

# When a stock is trending — whether for good or bad 
# reasons — more people talk about it, and more articles are written about it. 
# This growing chatter can offer valuable clues for making smarter buy or sell decisions.

# This automation script taps into Google Trends to 
# create a graph for any stock you’re interested in, 
# giving you insights into its popularity and helping 
# guide your investment strategy.

from pytrends.request import TrendReq
import matplotlib.pyplot as plt

# Function to get Google Trends data
def get_google_trends_data(keywords, timeframe='today 3-m', geo='US'):
    pytrends = TrendReq(hl='en-US', tz=360)

    # Build the payload
    pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo=geo, gprop='')

    # Get interest over time
    interest_over_time_df = pytrends.interest_over_time()

    return interest_over_time_df

# Example keywords related to your article
STOCKS = ["AMZN", "MSFT", "NVDA", "AAPL", "GOOG"]

# Fetch Google Trends data
trends_data = get_google_trends_data(STOCKS)

# Plot the data
trends_data.plot(title='Google Trends for STOCKS')
plt.xlabel('Date')
plt.ylabel('Interest Over Time')
plt.show()
