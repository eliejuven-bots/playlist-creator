import React, { useState } from 'react';
import SpotifySearch from "./SpotifySearch";
import FeatureDisplay from "./FeatureDisplay";

function SongList({ songs, selectSong, selectedId, filter }) {
  const filtered = songs.filter(
    s => s.title.toLowerCase().includes(filter.toLowerCase()) ||
         s.artist.toLowerCase().includes(filter.toLowerCase())
  );
  return (
    <div>
      {filtered.length === 0 ? <div style={{margin:'20px 0',color:'#c00'}}>No songs match your search.</div> : <div style={{ display: 'flex', flexWrap: 'wrap', gap: 16 }}>
        {filtered.map(song => (
          <div
            key={song.id}
            style={{
              border: song.id === selectedId ? '2px solid #3f51b5' : '1px solid #ccc',
              padding: 12, borderRadius: 8, cursor: 'pointer', width: 180,
              background: song.id === selectedId ? '#e3eaff' : '#fff',
              boxShadow: song.id === selectedId ? '0 0 12px #bbcafc' : '0 1px 5px #eee',
              transition: 'box-shadow 0.2s, border 0.2s' 
            }}
            onClick={() => selectSong(song)}
          >
            <div style={{ fontWeight: 'bold' }}>{song.title}</div>
            <div>{song.artist}</div>
            <div style={{ fontSize: 12, color: '#666' }}>Mood: {song.mood}, Energy: {song.energy}</div>
          </div>
        ))}
      </div>}
    </div>
  );
}

function Playlist({ tracks }) {
  return (
    <div>
      <h2>Generated Playlist</h2>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 12 }}>
        {tracks.map(track => (
          <div key={track.id} style={{ border: '1px solid #bbb', padding: 10, borderRadius: 7, width: 165, background: '#f8f8ff', boxShadow: '0 1px 2px #eee' }}>
            <div style={{ fontWeight: 'bold' }}>{track.title}</div>
            <div style={{ fontSize: 12, color: '#444' }}>{track.artist}</div>
            <div style={{ fontSize: 10, color: '#999' }}>{track.album || ''}</div>
            {track.cover && <img src={track.cover} alt="cover" style={{width: 48, borderRadius: 5, margin: '8px 0'}} />}
            {track.preview_url && <audio controls src={track.preview_url} style={{width:'100%'}} />}
          </div>
        ))}
      </div>
    </div>
  );
}

function App() {
  const [songs, setSongs] = useState([]);
  const [selected, setSelected] = useState(null);
  const [playlist, setPlaylist] = useState([]);
  const [filter, setFilter] = useState('');
  const [loading, setLoading] = useState(false);
  const [deezerMsg, setDeezerMsg] = useState('');
  const [error, setError] = useState('');
  const [features, setFeatures] = useState(null);
  const [playlistError, setPlaylistError] = useState('');

  async function fetchSongs() {
    try {
      const r = await fetch('/search');
      const data = await r.json();
      setSongs(data.results);
    } catch (e) {
      setError('Failed to load songs. Please check your backend connection.');
    }
  }

  async function generatePlaylist() {
    setLoading(true);
    setPlaylistError('');
    setPlaylist([]);
    setDeezerMsg('');
    setError('');
    if (selected && selected.id && features) {
      // Spotify (real recommendation)
      try {
        const r = await fetch('/spotify/recommend', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ seed_id: selected.id, target: {
            energy: features.energy,
            valence: features.valence,
            danceability: features.danceability
          } })
        });
        const data = await r.json();
        if (!r.ok) throw new Error(data.error || "Failed to get recommendations");
        setPlaylist(data.playlist || []);
      } catch (e) {
        setPlaylistError(e.message);
      }
      setLoading(false);
      return;
    }
    // fallback: legacy local
    try {
      const r = await fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ seed: selected })
      });
      const data = await r.json();
      setPlaylist(data.playlist);
    } catch (e) {
      setPlaylistError('Could not generate playlist. Try again.');
    }
    setLoading(false);
  }

  function addToDeezer() {
    setDeezerMsg('Playlist added to Deezer! (mock)');
  }

  React.useEffect(() => {
    fetchSongs();
  }, []);

  return (
    <div style={{ maxWidth: 1000, margin: '0 auto', padding: 32 }}>
      <h1 style={{ color: '#3f51b5' }}>Playlist Creator</h1>
      {error && <div style={{background:'#ffeaea',color:'#c00',padding:'10px 20px',borderRadius:7,marginBottom:16}}>{error}</div>}
      <h3>Step 1: Search Spotify and pick a Seed Song</h3>
      <SpotifySearch onSelect={async song => {
        setSelected(song);
        setFeatures(null);
        if (song && song.id) {
          setFeatures(null);
          try {
            const r = await fetch(`/spotify/features/${song.id}`);
            const data = await r.json();
            if (r.status !== 200) throw new Error(data.error || "No features");
            setFeatures(data);
          } catch (e) {
            setFeatures({ error: e.message });
          }
        }
      }} />
      {features && !features.error && <FeatureDisplay features={features} />}
      {features && features.error && <div style={{color:'#c00',marginBottom:18}}>Spotify Audio Features: {features.error}</div>}
      <div style={{margin:'32px 0',fontSize:14,color:'#888',fontWeight:400}}>OR try the legacy local catalog below (for demo/debug):</div>
      <input
        value={filter}
        onChange={e => setFilter(e.target.value)}
        placeholder="Search by song or artist in local catalog..."
        style={{padding:'9px 12px',marginBottom:18,fontSize:16,borderRadius:8,border:'1px solid #ccc',width:'100%',maxWidth:360}}
      />
      <SongList songs={songs} selectedId={selected && selected.id} selectSong={setSelected} filter={filter} />
      {selected && (
        <div style={{ margin: '30px 0' }}>
          <h3>Step 2: Generate Playlist by Mood/Energy</h3>
          <button disabled={loading} onClick={generatePlaylist} style={{ background: '#3f51b5', color: '#fff', border: 0, padding: '10px 18px', borderRadius: 7, cursor: 'pointer', fontWeight: 600 }}>
            {loading ? 'Generating...' : 'Generate Playlist'}
          </button>
        </div>
      )}
      {playlistError && <div style={{color:'#c00',marginBottom:18}}>{playlistError}</div>}
      {!!playlist.length && (
        <>
          <Playlist tracks={playlist} />
          <div style={{ marginTop: 20 }}>
            <button onClick={addToDeezer} style={{ background: '#25d366', color: '#fff', border: 0, padding: '8px 24px', borderRadius: 7, fontWeight: 600, cursor: 'pointer', fontSize: 18 }}>
              Add to Deezer (Mock)
            </button>
            {deezerMsg && <div style={{ fontWeight: 500, marginTop: 14, color: '#098d26', fontSize: 18 }}>{deezerMsg}</div>}
          </div>
        </>
      )}
    </div>
  );
}

export default App;
