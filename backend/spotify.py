import os
import requests
from flask import jsonify

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")

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

def spotify_search_api(query):
    token, err = get_spotify_token()
    if err:
        return {"error": err}, 400
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(
        "https://api.spotify.com/v1/search",
        headers=headers,
        params={"q": query, "type": "track", "limit": 10}
    )
    if r.status_code != 200:
        return {"error": f"Spotify search failed: {r.text}"}, 502
    tracks = r.json().get("tracks", {}).get("items", [])
    # extract essentials (id, title, artist, preview, etc)
    result = [
        {
            "id": t["id"],
            "title": t["name"],
            "artist": t["artists"][0]["name"] if t["artists"] else "",
            "album": t["album"]["name"] if t.get("album") else None,
            "preview_url": t.get("preview_url"),
            "cover": t["album"]["images"][0]["url"] if t.get("album") and t["album"].get("images") else None
        }
        for t in tracks
    ]
    return {"results": result}, 200

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

# NEW: recommend (uses Spotify recommendations API)
def spotify_recommend(seed_track_id, target_vals=None, n=50):
    token, err = get_spotify_token()
    if err:
        return {"error": err}, 400
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "seed_tracks": seed_track_id,
        "limit": n
    }
    if target_vals:
        if "energy" in target_vals:
            params["target_energy"] = target_vals["energy"]
        if "valence" in target_vals:
            params["target_valence"] = target_vals["valence"]
        if "danceability" in target_vals:
            params["target_danceability"] = target_vals["danceability"]
    r = requests.get("https://api.spotify.com/v1/recommendations", headers=headers, params=params)
    if r.status_code != 200:
        return {"error": f"Spotify recommendation failed: {r.text}"}, 502
    tracks = r.json().get("tracks", [])
    playlist = [
        {
            "id": t["id"],
            "title": t["name"],
            "artist": t["artists"][0]["name"] if t["artists"] else "",
            "album": t["album"]["name"] if t.get("album") else None,
            "preview_url": t.get("preview_url"),
            "cover": t["album"]["images"][0]["url"] if t.get("album") and t["album"].get("images") else None
        }
        for t in tracks
    ]
    return {"playlist": playlist}, 200
