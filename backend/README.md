# Backend API: Playlist-Creator

## Endpoints
- `/search` (GET): Search tracks in Spotify/Deezer
- `/generate` (POST): Generate playlist of 50 similar songs
- `/deezer/add` (POST): Add playlist to user’s Deezer account

## Deezer API Integration (Planned)
1. **Auth:** Implement OAuth2 to get `access_token` for user.
2. **Create Playlist:** Use endpoint `POST /user/me/playlists` with playlist name
3. **Add Tracks:** Use endpoint `POST /playlist/{playlist_id}/tracks` with song IDs

References:
- https://developers.deezer.com/api/oauth
- https://developers.deezer.com/api/playlists

## .env Variables Needed
- DEEZER_APP_ID
- DEEZER_APP_SECRET
- DEEZER_REDIRECT_URI

---
Run `pip install -r ../requirements.txt` before starting.