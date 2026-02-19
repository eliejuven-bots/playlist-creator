"""
basic Flask API for playlist-creator backend
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/search", methods=["GET"])
def search_tracks():
    # TODO: Implement search via Spotify/Deezer API
    return jsonify({"results": []})

@app.route("/generate", methods=["POST"])
def generate_playlist():
    seed_tracks = request.json.get("seeds", [])
    # TODO: Call recommendation algo and return playlist
    return jsonify({"playlist": []})

@app.route("/deezer/add", methods=["POST"])
def add_to_deezer():
    playlist = request.json.get("playlist", [])
    # TODO: Implement Deezer playlist creation/auth
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)