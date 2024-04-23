import requests
import sys

def get(username, password, api_url):
    auth_endpoint = api_url + '/login'
    payload = {
        'username': username,
        'password': password
    }
    try:
        response = requests.post(auth_endpoint, json=payload)
        response.raise_for_status()
        bearer_token = response.json().get('token')
        if bearer_token:
            return bearer_token
        else:
            print("Bearer token not found in response.")
            sys.exit(1)
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
    except ValueError as json_err:
        print(f'JSON decoding failed: {json_err}')
        sys.exit(1)
