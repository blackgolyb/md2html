if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.documentElement.classList.add("dark")
    content_element.classList.add("dark")
} else {
    document.documentElement.classList.add("light")
    content_element.classList.add("light")
}
