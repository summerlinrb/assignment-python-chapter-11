import requests

"""
Documentation at 
https://documenter.getpostman.com/view/10808728/SzS8rjbc
"""

# BRANDON SUMMERLIN

# 1. get the API data from the web server
# This API server does not require an API key
# 2. Convert the data into a useful python objects: usually a list or dictionaries
url = "https://api.covid19api.com/summary"


headers_dictionary = {
    'X-Access-Token': "5cf9dfd5-3449-485e-b5ae-70a60e997864"
}

response = requests.get(url, headers=headers_dictionary)

result = response.json()

print(type(result))

global_stats = result['Global']
deaths = global_stats['TotalDeaths']
cases = global_stats['TotalConfirmed']
mortality_rate = (deaths / cases)
print(global_stats)
print(f"{deaths:,}")
print(f"{cases:,}")
print(f"{mortality_rate:.3f}")
