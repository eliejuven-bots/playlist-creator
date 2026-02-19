import os
import requests
from flask import jsonify

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")

# --- unchanged search functions omitted for brevity ---

def get_spotify_token():
    if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
        return None, "Spotify API keys missing. See README for setup."
    resp = requests.post(
        "https://accounts.spotify.com/api/token",
        data={"grant_type": "client_credentials"},
        auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    )
    if resp.status_code != 200:
        return None, f"Spotify auth failed: {resp.text}"
    return resp.json()["access_token"], None

# --- search API omitted ---

def get_audio_features(track_id):
    token, err = get_spotify_token()
    if err:
        return {"error": err}, 400
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return {"error": f"Spotify audio features failed: {r.text}"}, 502
    data = r.json()
    # Return only relevant features
    feat = {
        "id": data.get("id"),
        "energy": data.get("energy"),
        "valence": data.get("valence"),
        "danceability": data.get("danceability"),
        "tempo": data.get("tempo"),
        "acousticness": data.get("acousticness"),
        "instrumentalness": data.get("instrumentalness")
    }
    return feat, 200
