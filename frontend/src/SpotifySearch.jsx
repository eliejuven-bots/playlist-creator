import React, { useState } from "react";

export default function SpotifySearch({ onSelect }) {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const search = async () => {
    setError("");
    setResults([]);
    if (!query.trim()) return;
    setLoading(true);
    try {
      const r = await fetch(`/spotify/search?q=${encodeURIComponent(query)}`);
      const data = await r.json();
      if (r.status !== 200) throw new Error(data.error || "API error");
      setResults(data.results);
    } catch (e) {
      setError(e.message);
    }
    setLoading(false);
  };

  return (
    <div style={{marginBottom:32}}>
      <div style={{ display: "flex", gap: 8 }}>
        <input
          type="text"
          value={query}
          maxLength={60}
          onChange={e => setQuery(e.target.value)}
          onKeyDown={e => e.key === "Enter" && search()}
          placeholder="Search all Spotify songs..."
          style={{ padding: "10px 12px", borderRadius: 8, border: "1px solid #ccc", width:320,fontSize:17}}
        />
        <button
          disabled={loading || !query.trim()}
          onClick={search}
          style={{ padding: "10px 18px",borderRadius:7, border:0, background: "#3f51b5", color: "#fff",fontWeight:600 }}>
          {loading ? "Searching..." : "Search"}
        </button>
      </div>
      {error && <div style={{ color: "#c00", marginTop: 12 }}>{error.includes("key") ?
        <span>API key missing! Fill <b>SPOTIFY_CLIENT_ID</b> in <b>.env</b> (see README instructions).</span> : error}</div>}
      <div style={{ margin: "20px 0"}}>
        {results.length > 0 && (
          <div style={{display:'flex',flexWrap:'wrap',gap:16}}>
            {results.map(song => (
              <div
                key={song.id}
                onClick={() => onSelect(song)}
                style={{padding:12,borderRadius:8,background:'#fafbff',border:'1.5px solid #3f51b545',cursor:'pointer',transition:'box-shadow 0.15s',width:275,boxShadow:'0 2px 8px #e1e1fb'}}>
                <div style={{fontWeight:'bold',fontSize:17}}>{song.title}</div>
                <div style={{fontSize:15,color:'#3f51b5'}}>{song.artist}</div>
                <div style={{fontSize:13,color:'#555',marginTop:3}}>{song.album}</div>
                {song.cover && <img src={song.cover} alt="cover" style={{width:64,height:64,marginTop:6,borderRadius:6}}/>}
                {song.preview_url && <audio controls style={{width:'100%',marginTop:6}} src={song.preview_url}></audio>}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
