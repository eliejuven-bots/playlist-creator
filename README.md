# Playlist Creator

A web app to create custom playlists with songs from Spotify/Deezer based on vibe, energy, and mood.

## Features

- **Browse/Search Music:** Explore and search all available songs
- **Select Seed Song:** Choose a track as your mood seed (from the built-in mock catalog or real Spotify search)
- **Playlist Generation:** Instantly create a playlist of 50 tracks in the same mood/energy
- **Add to Deezer:** (WIP) Button/UI and backend scaffolded—OAuth export landing next!

## Quickstart

### 1. Backend Setup
```bash
cd backend
pip install -r ../requirements.txt
cp ../.env.example ../.env  # Fill in your Spotify/Deezer API keys as needed
python app.py
```
Frontend expects backend on localhost:5050.

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
App will be at http://localhost:5173

---

## Screenshots
_TODO: Add screenshots after latest polish—see `/frontend` for full UI code. To add your own: take a screenshot with a generated playlist shown, place it here!_

## Current Flow
- Search and select any real Spotify song (with your API keys in `.env`)
- See live mood/energy analysis for your seed song (Spotify audio features)
- Generate a **real**, mood-matched playlist of 50 songs via the Spotify recommendations API
- Preview and browse the playlist, with cover art and song previews
- **Add to Deezer:** (WIP) Button and UI scaffold in code; backend export flow will be live soon

## Upcoming/Planned
- 🔜 Deezer export: True OAuth authorization and push-to-Deezer integration. Ready for API keys in `.env`, UI/route scaffolded, final code landing next!
- 📸 Add demo screenshots from browser—PRs welcome!

## API Credential Setup

**You MUST fill in real API credentials in the `.env` file to search all tracks and to add playlists to Deezer!**

- **Spotify:** Create an app at https://developer.spotify.com/dashboard/applications and use your Client ID/Client Secret/Redirect URI. Enables searching and feature extraction.
- **Deezer:** Register at https://developers.deezer.com/myapps for App ID/Secret/Redirect URI. Enables playlist export.

Example:
```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_secret
SPOTIFY_REDIRECT_URI=http://localhost:5050/callback/spotify

DEEZER_APP_ID=your_app_id
DEEZER_APP_SECRET=your_secret
DEEZER_REDIRECT_URI=http://localhost:5050/callback/deezer
```

You can leave these blank until launch; note features will not work until keys are filled.

---
