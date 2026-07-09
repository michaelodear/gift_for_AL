/* act3.js - resume across the click-through (GitHub Pages; localStorage works here) */
(function(){
  var KEY='act3_progress';
  var ORDER=['narration.html','clip1.html','panel_objection.html','clip2.html',
    'reveal1a.html','panel_dossiers.html','reveal1b.html','panel_decode.html',
    'accuse.html','reveal2.html','clip4.html','closer.html'];
  window.Act3={
    order:ORDER,
    mark:function(page){try{localStorage.setItem(KEY,JSON.stringify({page:page,t:Date.now()}));}catch(e){}},
    saved:function(){try{return JSON.parse(localStorage.getItem(KEY));}catch(e){return null;}},
    reset:function(){try{localStorage.removeItem(KEY);}catch(e){}}
  };
})();
