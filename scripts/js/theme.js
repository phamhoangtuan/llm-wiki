// Theme toggle with localStorage persistence
(function() {
  const btn = document.getElementById('theme-toggle');
  if (!btn) return;
  
  const stored = localStorage.getItem('llm-wiki-theme');
  if (stored) document.documentElement.setAttribute('data-theme', stored);
  
  btn.addEventListener('click', function() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('llm-wiki-theme', next);
  });
})();
