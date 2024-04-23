import requests
import os
import json
import sys 

def get(username, password, api_url):
    auth_endpoint = api_url + '/login'
    headersList = {
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "username": username,
        "password": password
    })
    try:
        response = requests.post(auth_endpoint, data=payload, headers=headersList)
        response.raise_for_status()
        data = response.json()
        token = data.get('token')
        if token:
            return token
        else:
            print("No token found in the response.")
            sys.exit(1)
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        sys.exit(1)