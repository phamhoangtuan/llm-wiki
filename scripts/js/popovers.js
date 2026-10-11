// Popover previews on wikilinks using Tippy.js
(function() {
  if (typeof tippy === 'undefined') return;
  
  // Load concepts metadata
  fetch('../meta/concepts.json')
    .then(r => r.json())
    .then(data => {
      const links = document.querySelectorAll('a.wiki-link');
      
      links.forEach(link => {
        const href = link.getAttribute('href');
        if (!href) return;
        const slug = href.split('/').pop()?.replace('.html', '');
        if (!slug || !data.concepts[slug]) return;
        
        const meta = data.concepts[slug];
        tippy(link, {
          content: `<div class="popover-wrapper">
            <div class="popover-header">
              <div class="popover-category">${meta.category || 'Concept'}</div>
              <div class="popover-title">${meta.title}</div>
            </div>
            <div class="popover-body">${meta.definition || ''}</div>
            <div class="popover-footer"><a href="${href}" class="popover-more">Read more →</a></div>
          </div>`,
          allowHTML: true,
          interactive: true,
          maxWidth: 380,
          placement: 'auto',
          delay: [200, 100],
          animation: 'shift-away',
        });
      });
    })
    .catch(() => {});
})();
