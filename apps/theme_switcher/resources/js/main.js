const theme_changer = document.querySelector(".theme-changer");

const content_element = document.querySelector(".markdown-body");

function toggleDarkMode() {
  if (document.documentElement.classList.contains("light")) {
    document.documentElement.classList.remove("light");
    document.documentElement.classList.add("dark");
    content_element.classList.remove("light");
    content_element.classList.add("dark");
  } else if (document.documentElement.classList.contains("dark")) {
    document.documentElement.classList.remove("dark");
    document.documentElement.classList.add("light");
    content_element.classList.remove("dark");
    content_element.classList.add("light");
  }
}

theme_changer.addEventListener("click", toggleDarkMode);

// Auto select theme with css "prefers-color-scheme" option
if (
  window.matchMedia &&
  window.matchMedia("(prefers-color-scheme: dark)").matches
) {
  document.documentElement.classList.add("dark");
  content_element.classList.add("dark");
} else {
  document.documentElement.classList.add("light");
  content_element.classList.add("light");
}
