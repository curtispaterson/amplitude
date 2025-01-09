# API script to pull data from Amplitude Export API
# https://amplitude.com/docs/apis/analytics/export

# Load libraries
import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read .env file
api_key=os.getenv('AMP_API_KEY')
api_secret_key=os.getenv('AMP_SECRET_KEY')
print(api_key)
print(api_secret_key)