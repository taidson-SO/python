import requests

class HttpClient:
    def __init__(self):
        self.session = requests.Session()

    def get_response(self, url, params=None):
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"HTTP GET request failed: {e}")
            return None

