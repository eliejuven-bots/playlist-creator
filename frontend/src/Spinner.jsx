import React from 'react';
export default function Spinner() {
  return <div style={{display:'flex',justifyContent:'center',alignItems:'center',minHeight:56}}>
    <div style={{width:36,height:36,border:'5px solid #e3eaff',borderTopColor:'#3f51b5',borderRadius:'50%',animation:'spin 1s linear infinite'}} />
    <style>{`@keyframes spin{0%{transform:rotate(0deg);}100%{transform:rotate(360deg);}}`}</style>
  </div>;
}