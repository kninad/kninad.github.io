// Store theme in localStorage
function setTheme(theme) {
  document.getElementById("theme-stylesheet").href = theme + ".css";
  localStorage.setItem("theme", theme);
}

// Toggle theme
function toggleTheme() {
  const current = localStorage.getItem("theme") || "light";
  const next = current === "light" ? "dark" : "light";
  setTheme(next);
}

document.addEventListener("DOMContentLoaded", () => {
  // Load saved theme
  const saved = localStorage.getItem("theme") || "light";
  setTheme(saved);

  // Add toggle button
  const btn = document.createElement("button");
  btn.innerText = "Toggle Theme";
  btn.style.position = "fixed";
  btn.style.bottom = "1em";
  btn.style.right = "1em";
  btn.style.padding = "0.5em 1em";
  btn.style.cursor = "pointer";
  btn.onclick = toggleTheme;
  document.body.appendChild(btn);
});
