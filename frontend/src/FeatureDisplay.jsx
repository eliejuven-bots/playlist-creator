import React from "react";
export default function FeatureDisplay({ features }) {
  if (!features) return null;
  return (
    <div style={{marginTop:22,marginBottom:18,padding:18,background:'#f8fafd',border:'1.5px solid #3f51b520',borderRadius:10,maxWidth:480}}>
      <h4 style={{margin:'0 0 10px 0',color:'#333'}}>Song Analysis (Spotify Audio Features)</h4>
      <div style={{display:'flex',gap:18,flexWrap:'wrap'}}>
        <div>Energy: <b>{features.energy}</b></div>
        <div>Danceability: <b>{features.danceability}</b></div>
        <div>Valence (Happiness): <b>{features.valence}</b></div>
        <div>Tempo: <b>{features.tempo}</b> BPM</div>
        <div>Acousticness: <b>{features.acousticness}</b></div>
        <div>Instrumentalness: <b>{features.instrumentalness}</b></div>
      </div>
    </div>
  );
}
