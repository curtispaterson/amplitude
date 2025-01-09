# API script to pull data from Amplitude Export API
# https://amplitude.com/docs/apis/analytics/export

# Load libraries
import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read .env file
api_key = os.getenv('AMP_API_KEY')
api_secret_key = os.getenv('AMP_SECRET_KEY')

# Time parameters
start_time = '20250101T00'
end_time = '20250109T00'

# Build API endpoint
url = 'https://analytics.eu.amplitude.com/api/2/export'
params = {
    'start' : start_time,
    'end' : end_time
}

# Build API response
response = requests.get(url, params=params, auth=(api_key, api_secret_key))

if response.status_code == 200:
    data = response.content      
    print('Data retrieved successfully.')
    with open('data.zip', 'wb') as file:         
        file.write(data) 
else:
    print(f'Error {response.status_code}: {response.text}')