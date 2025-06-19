import requests

def upload_to_test(url, data):
    response = requests.post(url, json=data)
    print(response.status_code)
