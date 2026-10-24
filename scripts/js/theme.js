/* Hallmark · component: theme-toggle · genre: modern-minimal · theme: Cobalt
 * states: default · hover · focus · active
 * contrast: pass */

// Theme toggle with localStorage persistence + SVG icon swap
(() => {
	const btn = document.getElementById("theme-toggle");
	if (!btn) return;

	const html = document.documentElement;
	const sunIcon = btn.querySelector(".icon-sun");
	const moonIcon = btn.querySelector(".icon-moon");

	const stored = localStorage.getItem("llm-wiki-theme");
	if (stored) html.setAttribute("data-theme", stored);

	function updateIcons(theme) {
		if (!sunIcon || !moonIcon) return;
		if (theme === "light") {
			sunIcon.style.display = "none";
			moonIcon.style.display = "block";
		} else {
			sunIcon.style.display = "block";
			moonIcon.style.display = "none";
		}
	}

	// Initial icon state
	updateIcons(html.getAttribute("data-theme") || "dark");

	btn.addEventListener("click", () => {
		const current = html.getAttribute("data-theme");
		const next = current === "light" ? "dark" : "light";
		html.setAttribute("data-theme", next);
		localStorage.setItem("llm-wiki-theme", next);
		updateIcons(next);
	});
})();
