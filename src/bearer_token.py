import requests

def get(username, password, api_url):
    auth_endpoint = api_url + '/login'
    payload = {
        'username': username,
        'password': password
    }
    try:
        response = requests.post(auth_endpoint, json=payload)
        response.raise_for_status()
        bearer_token = response.json().get('access_token')
        if bearer_token:
            return bearer_token
        else:
            print("Failed to obtain Bearer token.")
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None