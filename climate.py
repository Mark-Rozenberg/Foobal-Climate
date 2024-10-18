import requests

# Set your NOAA API token here
api_token = 'YOUR_NOAA_API_TOKEN'

# Define the endpoint
endpoint = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'

# Define the parameters for the request
params = {
    'datasetid': 'GHCND',  # Global Historical Climatology Network - Daily
    'locationid': 'CITY:US390029',  # Example location ID (Cincinnati, OH)
    'startdate': '2020-01-01',
    'enddate': '2020-12-31',
    'datatypeid': 'TMAX',  # Maximum temperature
    'limit': 1000  # Number of results to return
}

# Set the headers with the API token
headers = {
    'token': api_token
}

# Make the request
response = requests.get(endpoint, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)