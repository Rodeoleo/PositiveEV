import requests
import json
import pandas as pd
from apiclient import ApiClient
from _888sport import _888sport
from pinnacle import Pinnacle
from oddsProcessor import OddsProcessor

api_client = ApiClient()

_888 = _888sport(api_client)
pinnacle = Pinnacle(api_client)

bookies = [_888]
oddsProcessor = OddsProcessor(pinnacle, bookies, False)



_888_mlb =  _888.get_mlb_odds()
pinnace_mlb = pinnacle.get_mlb_odds()
print(len(_888_mlb))
print(len(pinnace_mlb))


# pinnacle_mlb_odds = {}
# _888_mlb_odds = {}



# # print(_888_mlb)
# # print(pinnace_mlb)
# # print(pinnace_mlb[9]['sportsbooks'][0]['odds'][0]['price'])

# for games in pinnace_mlb:
#     try:
#         pinnacle_mlb_odds[games['id']] = [
#                 int(games['sportsbooks'][0]['odds'][0]['price']), 
#                 int(games['sportsbooks'][0]['odds'][1]['price'])
#         ]
#     except IndexError:
#         pass


# for games in _888_mlb:
#     try:
#         _888_mlb_odds[games['id']] = [
#             int(games['sportsbooks'][0]['odds'][1]['price']), 
#             int(games['sportsbooks'][0]['odds'][0]['price'])
#         ]
#     except IndexError:
#         pass


# pinnacle_mlb_fair_odds = oddsProcessor.de_vig(pinnacle_mlb_odds)

oddsProcessor.compare_mlb(pinnacle, _888)
print("end")

# print(pinnace_mlb)
# print()
# print(_888_mlb_odds)
# print()
# print(pinnacle_mlb_fair_odds)


# compare_odds(pinnacle_mlb_fair_odds, _888_mlb_odds)
