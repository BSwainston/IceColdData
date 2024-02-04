from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import numpy as np

# Data for the two teams
team1 = {
    "faceoffWinPct": 0.521689,
    "gamesPlayed": 45,
    "goalsAgainst": 124,
    "goalsAgainstPerGame": 2.75555,
    "goalsFor": 158,
    "goalsForPerGame": 3.51111,
    "losses": 15,
    "otLosses": 1,
    "penaltyKillNetPct": 0.856209,
    "penaltyKillPct": 0.830066,
    "pointPct": 0.65555,
    "points": 59,
    "powerPlayNetPct": 0.241134,
    "powerPlayPct": 0.269503,
    "regulationAndOtWins": 27,
    "seasonId": 20232024,
    "shotsAgainstPerGame": 28.02222,
    "shotsForPerGame": 33.77777,
    "teamFullName": "Edmonton Oilers",
    "teamId": 22,
    "ties": None,
    "wins": 29,
    "winsInRegulation": 24,
    "winsInShootout": 2,
}

team2 = {
    "faceoffWinPct": 0.513025,
    "gamesPlayed": 49,
    "goalsAgainst": 126,
    "goalsAgainstPerGame": 2.57142,
    "goalsFor": 157,
    "goalsForPerGame": 3.20408,
    "losses": 14,
    "otLosses": 4,
    "penaltyKillNetPct": 0.85119,
    "penaltyKillPct": 0.827381,
    "pointPct": 0.67346,
    "points": 66,
    "powerPlayNetPct": 0.189024,
    "powerPlayPct": 0.237804,
    "regulationAndOtWins": 30,
    "seasonId": 20232024,
    "shotsAgainstPerGame": 27.2653,
    "shotsForPerGame": 34.32653,
    "teamFullName": "Florida Panthers",
    "teamId": 13,
    "ties": None,
    "wins": 31,
    "winsInRegulation": 26,
    "winsInShootout": 1,
}

# Define the features you want to use in your model (exclude non-numeric columns)
features = [
    "faceoffWinPct",
    "gamesPlayed",
    "goalsAgainst",
    "goalsAgainstPerGame",
    "goalsFor",
    "goalsForPerGame",
    "losses",
    "otLosses",
    "penaltyKillNetPct",
    "penaltyKillPct",
    "pointPct",
    "points",
    "powerPlayNetPct",
    "powerPlayPct",
    "regulationAndOtWins",
    "shotsAgainstPerGame",
    "shotsForPerGame",
]

# Create a dataset with the features for both teams
data = [[team1[feat] for feat in features], [team2[feat] for feat in features]]
labels = [0, 1]

# Standardize the features (scaling)
scaler = StandardScaler()
X = scaler.fit_transform(data)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X, labels)

# Predict the probability of team2 winning
prob_team2_wins = model.predict_proba(X)[:, 1]

print(f"Probability of {team2['teamFullName']} winning: {prob_team2_wins[0]:.4f}")
print(f"Probability of {team1['teamFullName']} winning: {1 - prob_team2_wins[0]:.4f}")
