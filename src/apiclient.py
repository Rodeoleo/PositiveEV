import requests

class ApiClient:
    def __init__(self):
        self.api_key = "O4PTM9XDloP8Nohbi6vn"
        self.base_url = "https://api.oddsblaze.com/v1/"

    def get(self, endpoint, params=None):
        if params is None:
            params = {}
        params['key'] = self.api_key

        try:
            response = requests.get(f"{self.base_url}{endpoint}", params)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve data: {e}")
