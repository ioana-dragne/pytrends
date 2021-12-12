# Import modules
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
plt.style.use('bmh')
from pandas.plotting import register_matplotlib_converters

# Initiate Google Trends
pytrends = TrendReq(hl='en-US', tz=360)
# Set the keywords to search for
pytrends.build_payload(kw_list=['data science'])

# Set the dataframe containing the interest over time
time_df = pytrends.interest_over_time()
print(time_df.head(15))


# Creating plot
fig, ax = plt.subplots(figsize=(12, 6))
time_df['data science'].plot(color='purple')
plt.title('Total Google Searches for "Data Science"', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
#plt.show()
plt.savefig('pytrends.png')
