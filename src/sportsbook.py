import requests
import apiclient


class Sportsbook:
    def __init__(self, api_client, sportsbook):
        self.id = id
        self.api_client = api_client
        self.sportsbook = sportsbook

    def get_mlb_odds(self):
        params = {
            "league": "MLB",
            "sportsbook": self.sportsbook,
            "market": "Moneyline"
        }
        data = self.api_client.get("odds", params=params)
        return data['games'] if data else []