import requests

def check_response(url):
    r = requests.get(str(url))
    return r
