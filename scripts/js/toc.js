// TOC generation from headings
(function() {
  const toc = document.getElementById('toc');
  if (!toc) return;
  
  const headings = document.querySelectorAll('.content-area h2, .content-area h3');
  if (headings.length === 0) { toc.innerHTML = '<span style="color:var(--text-dim)">No sections</span>'; return; }
  
  let html = '';
  headings.forEach(h => {
    const id = h.id || h.textContent.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/-+$/, '');
    if (!h.id) h.id = id;
    const cls = h.tagName === 'H3' ? ' class="toc-h3"' : '';
    html += `<li${cls}><a href="#${id}">${h.textContent}</a></li>`;
  });
  toc.innerHTML = html;
})();
