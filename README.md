# Playlist Creator

A web app to create custom playlists with songs from Spotify/Deezer based on vibe, energy, and mood.

## Features

- **Browse/Search Music:** Explore and search all available songs
- **Select Seed Song:** Choose a track as your mood seed (from the built-in mock catalog)
- **Playlist Generation:** Instantly create a playlist of 50 tracks in the same mood/energy
- **Add to Deezer:** (Mock) Button confirms addition—API ready for real Deezer export

## Quickstart

### Backend
```bash
cd backend
pip install -r ../requirements.txt
python app.py
```
Frontend expects backend on localhost:5050.

### Frontend
```bash
cd frontend
npm install
npm run dev
```
App will be at http://localhost:5173

## Screenshots
_TODO: Add screenshots after latest polish—will show MVP end-to-end._

## Extending (APIs)
- **To connect Spotify API:** Implement real search and get audio features
- **To connect real Deezer API:** Replace the mock in /deezer endpoint and UI

---
This MVP is ready to demo or extend!
