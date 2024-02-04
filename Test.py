import requests
import json
from pprint import pprint
import pandas as pd

leagueLeader_url = "https://api-web.nhle.com/v1/skater-stats-leaders/current"

team_response = requests.get(leagueLeader_url)

pretty_json = json.loads(team_response.text)
# print(json.dumps(pretty_json, indent=4))

# fetch players and categories
SHGoals = pretty_json["goalsSh"][0]["firstName"]["default"]
print(SHGoals)
