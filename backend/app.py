from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

mock_catalog = [
    {"id": 1, "title": "Song Alpha", "artist": "Artist X", "mood": "chill", "energy": 0.5},
    {"id": 2, "title": "Song Beta", "artist": "Artist Y", "mood": "party", "energy": 0.8},
    {"id": 3, "title": "Song Gamma", "artist": "Artist Z", "mood": "sad", "energy": 0.3}
]

@app.route('/search', methods=['GET'])
def search_tracks():
    return jsonify({"results": mock_catalog})

@app.route('/generate', methods=['POST'])
def generate_playlist():
    # Always returns 50 mock tracks with the same mood as seed
    seed = request.json.get("seed", {})
    mood = seed.get("mood") or "chill"
    energy = seed.get("energy") or 0.5
    playlist = [
        {"id": i, "title": f"Generated Song {i}", "artist": f"Similar Artist {i}", "mood": mood, "energy": energy}
        for i in range(1, 51)
    ]
    return jsonify({"playlist": playlist})

if __name__ == '__main__':
    app.run(debug=True, port=5050)
