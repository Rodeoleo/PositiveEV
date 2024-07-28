from sportsbook import Sportsbook

class Pinnacle(Sportsbook):
    def __init__(self, api_client):
        super().__init__(api_client, "pinnacle")
