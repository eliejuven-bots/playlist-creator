from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

mock_catalog = [
    {"id": 1, "title": "Lost in the Echo", "artist": "Linkin Park", "mood": "energetic", "energy": 0.9},
    {"id": 2, "title": "Blinding Lights", "artist": "The Weeknd", "mood": "upbeat", "energy": 0.85},
    {"id": 3, "title": "Someone Like You", "artist": "Adele", "mood": "sad", "energy": 0.25},
    {"id": 4, "title": "Shape of You", "artist": "Ed Sheeran", "mood": "romantic", "energy": 0.6},
    {"id": 5, "title": "Can’t Stop the Feeling!", "artist": "Justin Timberlake", "mood": "happy", "energy": 0.8},
    {"id": 6, "title": "Take Five", "artist": "The Dave Brubeck Quartet", "mood": "chill", "energy": 0.4},
    {"id": 7, "title": "Bad Guy", "artist": "Billie Eilish", "mood": "funky", "energy": 0.7},
    {"id": 8, "title": "Moonlight Sonata", "artist": "Beethoven", "mood": "melancholic", "energy": 0.15},
    {"id": 9, "title": "Sandstorm", "artist": "Darude", "mood": "epic", "energy": 1.0},
    {"id": 10, "title": "Happy", "artist": "Pharrell Williams", "mood": "joyful", "energy": 0.95},
    {"id": 11, "title": "Africa", "artist": "Toto", "mood": "nostalgic", "energy": 0.6},
    {"id": 12, "title": "Counting Stars", "artist": "OneRepublic", "mood": "inspirational", "energy": 0.85},
    {"id": 13, "title": "Smells Like Teen Spirit", "artist": "Nirvana", "mood": "rebellious", "energy": 0.9},
    {"id": 14, "title": "Believer", "artist": "Imagine Dragons", "mood": "powerful", "energy": 0.8},
    {"id": 15, "title": "Summertime Sadness", "artist": "Lana Del Rey", "mood": "moody", "energy": 0.4}
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

if __name__ == '__main__':
    app.run(debug=True, port=5050)
