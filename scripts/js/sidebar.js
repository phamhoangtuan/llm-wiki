// Sidebar navigation populated from concepts.json
(function() {
  const nav = document.getElementById('sidebar-nav');
  if (!nav) return;
  
  fetch('../meta/concepts.json')
    .then(r => r.json())
    .then(data => {
      const cats = {};
      for (const [slug, meta] of Object.entries(data.concepts || {})) {
        const cat = meta.category || 'Uncategorized';
        if (!cats[cat]) cats[cat] = [];
        cats[cat].push({ slug, title: meta.title, href: meta.url });
      }
      
      const sorted = Object.entries(cats).sort((a, b) => {
        if (a[0] === 'Foundation') return -1;
        if (b[0] === 'Foundation') return 1;
        return a[0].localeCompare(b[0]);
      });
      
      const currentSlug = window.location.pathname.split('/').pop()?.replace('.html', '') || '';
      
      let html = '';
      for (const [cat, items] of sorted) {
        html += '<details class="sidebar-category" open>';
        html += `<summary><span class="caret">▶</span> ${cat}</summary>`;
        html += '<ul class="sidebar-links">';
        for (const item of items) {
          const cls = item.slug === currentSlug ? ' active' : '';
          html += `<li><a href="../concepts/${item.slug}.html" class="${cls}">${item.title}</a></li>`;
        }
        html += '</ul></details>';
      }
      nav.innerHTML = html;
    })
    .catch(() => {
      nav.innerHTML = '<p style="color:var(--text-dim);font-size:0.78rem;padding:0.5rem;">Navigate via <a href="../index.html">Index</a></p>';
    });
  
  // Sidebar resize
  const sidebar = document.querySelector('.sidebar');
  const handle = document.querySelector('.sidebar-resize-handle');
  if (!sidebar || !handle) return;
  
  const saved = localStorage.getItem('llm-wiki-sidebar-width');
  if (saved) sidebar.style.setProperty('--sidebar-width', saved + 'px');
  
  let resizing = false;
  handle.addEventListener('mousedown', function(e) { resizing = true; e.preventDefault(); });
  document.addEventListener('mousemove', function(e) {
    if (!resizing) return;
    const w = Math.max(180, Math.min(500, e.clientX));
    sidebar.style.setProperty('--sidebar-width', w + 'px');
  });
  document.addEventListener('mouseup', function() {
    if (resizing) {
      resizing = false;
      const w = parseInt(getComputedStyle(sidebar).width);
      localStorage.setItem('llm-wiki-sidebar-width', w);
    }
  });
  
  // Mobile sidebar toggle
  const toggle = document.getElementById('sidebar-toggle');
  const overlay = document.getElementById('sidebar-overlay');
  if (toggle && overlay) {
    toggle.addEventListener('click', function() {
      sidebar.classList.toggle('open');
      overlay.classList.toggle('show');
    });
    overlay.addEventListener('click', function() {
      sidebar.classList.remove('open');
      overlay.classList.remove('show');
    });
  }
})();
