import requests
import sys
import json
from datetime import datetime

def get(api_url, token, start_date, end_date):
    auth_endpoint = api_url + '/therapylink'
    headersList = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json" 
    }
    if isinstance(start_date, datetime):
        start_date = start_date.isoformat()
    if isinstance(end_date, datetime):
        end_date = end_date.isoformat()
    payload = json.dumps({
        "date_from": start_date,
        "date_to": end_date,
    })
    try:
        response = requests.get(auth_endpoint, data=payload, headers=headersList)
        response.raise_for_status()
        data = response.json()
        if data:
            print('Data retrieved.')
            return data
        else:
            print("Data not found in response.")
            sys.exit(1)
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        sys.exit(1)