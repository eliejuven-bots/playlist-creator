# Playlist Creator

A web app to create custom playlists with songs from Spotify/Deezer based on vibe, energy, and mood.

## Features

- **Browse/Search Music:** Explore and search all available songs
- **Select Seed Song:** Choose a track as your mood seed (from the built-in mock catalog)
- **Playlist Generation:** Instantly create a playlist of 50 tracks in the same mood/energy
- **Add to Deezer:** (Mock) Button confirms addition—API ready for real Deezer export

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

## Features

- **Search all Spotify/Deezer tracks** (API credentials required!)
- **Select any songs as playlist seeds**
- **Generate 50-track smart playlist (mood/energy/vibe)**
- **Add playlist to Deezer account via OAuth (real export, optional to fill keys)**

## Screenshots
_TODO: Add screenshots after latest polish—will show full, real API flow._

## Extending (APIs)
- Code is ready for real Spotify/Deezer integration. See backend code and API notes for more instructions.

---
This MVP is ready for your keys, demo, or further feature work!
