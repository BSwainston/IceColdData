import requests
import numpy as np
from sklearn.linear_model import LogisticRegression

# Define the URL for the API
url = "https://api.nhle.com/stats/rest/en/team/summary?sort=shotsForPerGame&cayenneExp=seasonId=20232024%20and%20gameTypeId=2"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Create a dictionary to store each team's data
    team_data = {}

    # Iterate through the teams in the data
    for team in data["data"]:
        team_name = team["teamFullName"]
        team_data[team_name] = team

    # Now you can access each team's data using their name as the key
    team1_data = team_data.get("San Jose Sharks")
    team2_data = team_data.get("Chicago Blackhawks")

    # Example: Accessing specific data for team 1
    print("Team 1 Name:", team1_data["teamFullName"])
    print("Team 1 Wins:", team1_data["wins"])
    print("Team 1 Goals For Per Game:", team1_data["goalsForPerGame"])

    # Example: Accessing specific data for team 2
    print("Team 2 Name:", team2_data["teamFullName"])
    print("Team 2 Wins:", team2_data["wins"])
    print("Team 2 Goals For Per Game:", team2_data["goalsForPerGame"])

else:
    print("Failed to fetch data from the API")
