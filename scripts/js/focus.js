// Focus mode toggle
(function() {
  const btn = document.getElementById('focus-toggle');
  if (!btn) return;
  
  btn.addEventListener('click', function() {
    document.body.classList.toggle('focus-mode');
    btn.textContent = document.body.classList.contains('focus-mode') ? '⊞' : '⛶';
  });
})();
