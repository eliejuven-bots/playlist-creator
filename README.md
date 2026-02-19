# Playlist Creator

A web app to create custom playlists with songs from Spotify/Deezer based on vibe, energy, and mood.

## Features

- **Browse/Search Music:** Explore and search all available songs on Spotify or Deezer
- **Select Seed Songs:** Choose multiple tracks you like
- **Playlist Generation:** Generate a playlist of 50 tracks matching the mood/energy/vibe of your selection
- **Deezer Integration:** Add the generated playlist to your Deezer account automatically

## Core Algorithm

1. **Song Feature Extraction:** When you select songs, fetch their audio features from Spotify/Deezer APIs (energy, danceability, mood, etc.)
2. **Profile Building:** Aggregate features (average/median energy, mood, etc.) from your selected songs
3. **Recommendation Fetching:** Query Spotify/Deezer for recommendations/seeds based on the profile and get a large pool of matches
4. **Curate Final Playlist:** Filter, sort, and deduplicate songs for coherence and diversity (target 50 tracks)

## Deezer Playlist Export
- Authenticate to Deezer via OAuth
- Create a new playlist in your Deezer account using its API
- Add the generated 50 tracks in one batch

---

### Future Enhancements
- Export to Spotify
- Advanced filtering (explicit content, genre focus, etc.)

---

## Project Structure
- `/frontend` - Browser UI (React/Vue or similar)
- `/backend` - API server for music search, recommendations, and Deezer integration
- `/algo` - Playlist generation and recommendation logic

## Setup

### Backend (Python)
1. Install dependencies: `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and set API keys (Deezer, if available)
3. Run: `cd backend && python app.py`

### Frontend (coming soon)

---
