from flask import Flask, request, jsonify
from flask_cors import CORS
from spotify import spotify_search_api, get_audio_features

app = Flask(__name__)
CORS(app)

@app.route('/spotify/search')
def spotify_search():
    q = request.args.get('q', '').strip()
    if not q:
        return jsonify({"error": "Missing 'q' parameter."}), 400
    result, status = spotify_search_api(q)
    return jsonify(result), status

# (legacy) mock endpoints below; will be phased out
mock_catalog = [
    {"id": 1, "title": "Lost in the Echo", "artist": "Linkin Park", "mood": "energetic", "energy": 0.9},
    {"id": 2, "title": "Blinding Lights", "artist": "The Weeknd", "mood": "upbeat", "energy": 0.85},
    {"id": 3, "title": "Someone Like You", "artist": "Adele", "mood": "sad", "energy": 0.25},
    {"id": 4, "title": "Shape of You", "artist": "Ed Sheeran", "mood": "romantic", "energy": 0.6},
    {"id": 5, "title": "Can’t Stop the Feeling!", "artist": "Justin Timberlake", "mood": "happy", "energy": 0.8}
]

@app.route('/search', methods=['GET'])
def search_tracks():
    return jsonify({"results": mock_catalog})

@app.route('/generate', methods=['POST'])
def generate_playlist():
    seed = request.json.get("seed", {})
    mood = seed.get("mood") or "chill"
    energy = seed.get("energy") or 0.5
    playlist = [
        {"id": i, "title": f"Generated Song {i}", "artist": f"Similar Artist {i}", "mood": mood, "energy": energy}
        for i in range(1, 51)
    ]
    return jsonify({"playlist": playlist})

@app.route('/spotify/features/<track_id>')
def spotify_features(track_id):
    result, status = get_audio_features(track_id)
    return jsonify(result), status

if __name__ == '__main__':
    app.run(debug=True, port=5050)
