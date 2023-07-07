import requests

def get_headers():
    return {'Content-Type': 'application/json'}

def determine_url(base_url, relative_url):
    url = relative_url if relative_url.startswith('http') else base_url + '/' + relative_url
    return url

class BaseApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, relative_url):
        headers = get_headers()
        options = {'headers': headers, 'params': {}}
        url = determine_url(self.base_url, relative_url)
        response = requests.get(url, **options)
        return response

    def get_with_params(self, relative_url, params):
        headers = get_headers()
        options = {'headers': headers, 'params': params}
        url = determine_url(self.base_url, relative_url)
        response = requests.get(url, **options)
        return response

    def post(self, relative_url, data):
        headers = get_headers()
        options = {'headers': headers, 'params': {}}
        url = determine_url(self.base_url, relative_url)
        response = requests.post(url, data=data, **options)
        return response

    def put(self, relative_url, data):
        headers = get_headers()
        options = {'headers': headers, 'params': {}}
        url = determine_url(self.base_url, relative_url)
        response = requests.put(url, data=data, **options)
        return response

    def delete(self, relative_url):
        headers = get_headers()
        options = {'headers': headers, 'params': {}}
        url = determine_url(self.base_url, relative_url)
        response = requests.delete(url, **options)
        return response
