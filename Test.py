import requests
import json
from pprint import pprint
import pandas as pd

leagueLeader_url = "https://api-web.nhle.com/v1/skater-stats-leaders/current"

# ANSI escape codes for text color
category_color = "\033[1;34m"  # Blue color
reset_color = "\033[0m"  # Reset color to default

# Dictionary to map original category names to new names
category_mapping = {
    "goalsSh": "SH Goals",
    "plusMinus": "Plus/Minus",
    "assists": "Assists",
    "goalsPp": "PP Goals",
    "faceoffLeaders": "FO %",
    "penaltyMins": "Penalty Minutes",
    "goals": "Goals",
    "toi": "Time On Ice",
    # Add more mappings as needed
}

team_response = requests.get(leagueLeader_url)

pretty_json = json.loads(team_response.text)

# print(json.dumps(pretty_json, indent=4))

for original_category, players in pretty_json.items():
    # Get the corresponding new category name from the mapping
    new_category = category_mapping.get(original_category, original_category)

    # Print the new category name with enhanced formatting
    print(f"{category_color}Category: {new_category}{reset_color}\n")
    for player in players:
        print(f"Name: {player['firstName']['default']} {player['lastName']['default']}")
        print(f"Team: {player['teamName']['default']} ({player['teamAbbrev']})")
        print(f"Position: {player['position']}")
        print(f"Value: {player['value']}")
        print(f"Headshot: {player['headshot']}")
        print("\n")
