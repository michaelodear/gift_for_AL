/* act3.js — resume across the click-through. Pages mark bare filenames;
   the root index.html prepends "act3/". localStorage works on GitHub Pages. */
(function(){
  var KEY='act3_progress';
  var ORDER=['narration.html','clip1.html','panel_objection.html','clip2.html',
    'panel_dossiers.html','reveal1b.html','panel_decode.html','reveal2.html',
    'clip4.html','closer.html','gidget.html'];
  window.Act3={ order:ORDER,
    mark:function(p){try{localStorage.setItem(KEY,JSON.stringify({page:p,t:Date.now()}));}catch(e){}},
    saved:function(){try{return JSON.parse(localStorage.getItem(KEY));}catch(e){return null;}},
    reset:function(){try{localStorage.removeItem(KEY);}catch(e){}} };
})();
