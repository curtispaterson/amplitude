# API script to pull data from Amplitude Export API
# https://amplitude.com/docs/apis/analytics/export

# Load libraries
import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from datetime import datetime, timedelta
# importing module
import logging

# Create and configure logger
logging.basicConfig(filename="C:/Users/CurtisPaterson/Documents/GitHub/amplitude/amplitude_extraction_log.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Load .env file
load_dotenv()

# Read .env file
api_key = os.getenv('AMP_API_KEY')
api_secret_key = os.getenv('AMP_SECRET_KEY')

# Current datetime
current_datetime = datetime.now()
yesterday_datetime = datetime.now() - timedelta(days=1)

# dynamic dates
today = current_datetime.strftime('%Y%m%d') + 'T00'
yesterday = yesterday_datetime.strftime('%Y%m%d') + 'T00'

# yesterday = '20250115T00'
# today = '20250116T00'

# Build API endpoint
url = 'https://analytics.eu.amplitude.com/api/2/export'
params = {
    'start' : yesterday,
    'end' : today
}

# Build API response
response = requests.get(url, params=params, auth=(api_key, api_secret_key))

if response.status_code == 200:
    data = response.content      
    print('Data retrieved successfully.')

# Format the filename to include the current date and time
    output_filename = f"amplitude_data_{current_datetime.strftime('%Y-%m-%d_%H%M%S')}.zip"

    with open(output_filename, 'wb') as file:         
        file.write(data) 
else:
    print(f'Error {response.status_code}: {response.text}')

logger.debug("Harmless debug Message")