from _888sport import _888sport
from pinnacle import Pinnacle
from apiclient import ApiClient
from sportsbook import Sportsbook
from typing import List, Type

class OddsProcessor:
    def __init__(self, pinnacle, bookies: List[Type[Sportsbook]], live: bool):
        self.pinnacle = pinnacle
        self.bookies = bookies
        self.live = live

    def compare_mlb(self, pinnacle: Sportsbook, book1: Sportsbook):
        pinnacle_mlb = pinnacle.get_mlb_odds()
        book1_mlb = book1.get_mlb_odds()

        pinnacle_mlb_odds = {}
        book1_mlb_odds = {}

        for games in pinnacle_mlb:
            try:
                pinnacle_mlb_odds[games['id']] = [
                        int(games['sportsbooks'][0]['odds'][0]['price']), 
                        int(games['sportsbooks'][0]['odds'][1]['price'])
                ]
            except IndexError:
                pass

        for games in book1_mlb:
            try:
                book1_mlb_odds[games['id']] = [
                    int(games['sportsbooks'][0]['odds'][1]['price']), 
                    int(games['sportsbooks'][0]['odds'][0]['price'])
                ]
            except IndexError:
                pass

        pinnacle_mlb_fair_odds = self.de_vig(pinnacle_mlb_odds)
        self.compare_odds(pinnacle_mlb_fair_odds, book1_mlb_odds)

    @staticmethod
    def de_vig(odds):
        for key, value in odds.items():
            value1 = value[0] / (value[0] - 100) if value[0] < 0 else 100 / (value[0] + 100)
            value2 = value[1] / (value[1] - 100) if value[1] < 0 else 100 / (value[1] + 100)
            value1, value2 = value1 / (value1 + value2), value2 / (value1 + value2)
            if value1 == value2:
                value[0] = 100
                value[1] = 100
            elif value1 < value2:
                value[0] = 1/value1 * 100 - 100
                value[1] = -100 / (1/value2 - 1)
            else:
                value[1] = 1/value2 * 100 - 100
                value[0] = -100 / (1/value1 - 1)
        return odds

    @staticmethod
    def compare_odds(pinnacle_odds, bookie_odds):
        for key, value in pinnacle_odds.items():
            if key in bookie_odds:
                if value[0] < bookie_odds[key][0]:
                    print("VALUE HERE")
                    print(f"{key} {value[0]} vs {bookie_odds[key][0]}")
                if value[1] < bookie_odds[key][1]:
                    print("VALUE HERE")
                    print(f"{key} {value[1]} vs {bookie_odds[key][1]}")

                print(f"{key} {value[0]} vs {bookie_odds[key][0]}")
                print(f"{key} {value[1]} vs {bookie_odds[key][1]}")
                print("next")
        print("COMPARISON HAS ENDED")