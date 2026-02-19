"""
Algorithm to recommend playlist in the same mood (mock for MVP)
"""
def recommend_songs(seed_mood, seed_energy, n=50):
    return [
        {
            'id': i,
            'title': f"Similar Song {i}",
            'artist': f"Related Artist",
            'mood': seed_mood,
            'energy': seed_energy
        }
        for i in range(1, n+1)
    ]
