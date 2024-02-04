import requests
import json

resp = requests.get(
    "https://api.nhle.com/stats/rest/en/team/summary?sort=shotsForPerGame&cayenneExp=seasonId=20232024%20and%20gameTypeId=2"
)
data = resp.json()

print(json.dumps(data, indent=4))
# print(resp.content)
