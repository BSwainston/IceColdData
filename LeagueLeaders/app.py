import requests
import json
from pprint import pprint
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

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
    "points": "Points",
    "faceoffLeaders": "FO %",
    "penaltyMins": "Penalty Minutes",
    "goals": "Goals",
    "toi": "Time On Ice",
    # Add more mappings as needed
}

team_response = requests.get(leagueLeader_url)

pretty_json = json.loads(team_response.text)


@app.route("/")
def index():
    # Create a list to store formatted data for rendering
    formatted_data = []

    # Loop through each category and format player details
    for original_category, players in pretty_json.items():
        # Get the corresponding new category name from the mapping
        new_category = category_mapping.get(original_category, original_category)

        category_data = {
            "category": new_category,
            "players": [],
        }

        for player in players:
            formatted_player = {
                "id": player["id"],
                "name": f"{player['firstName']['default']} {player['lastName']['default']}",
                "team": f"{player['teamName']['default']} ({player['teamAbbrev']})",
                "position": player["position"],
            }

            if original_category == "faceoffLeaders":
                # Convert the "value" to a percentage for the "faceoffLeaders" category
                value_decimal = player["value"]
                value_percentage = value_decimal * 100
                formatted_player["value"] = f"{value_percentage:.2f}%"
            else:
                # Keep all other "value" fields as decimals
                value_decimal = player["value"]
                formatted_player["value"] = f"{value_decimal:.2f}"

            formatted_player["headshot"] = player["headshot"]

            category_data["players"].append(formatted_player)

        formatted_data.append(category_data)

    return render_template("index.html", formatted_data=formatted_data)


if __name__ == "__main__":
    app.run(debug=True)
