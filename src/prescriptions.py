import requests
import sys

def get(api_url, token, date_start, date_end):
    auth_endpoint = api_url + '/prescriptions'
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    params = {
        'date_start': date_start,
        'date_end': date_end
    }
    try:
        response = requests.get(auth_endpoint, headers=headers, params=params)
        response.raise_for_status() 
        data = response.json()
        return data or "No data."
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        sys.exit(1)
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
        sys.exit(1)
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')
        sys.exit(1)
    except requests.exceptions.RequestException as req_err:
        print(f'An error occurred: {req_err}')
        sys.exit(1)