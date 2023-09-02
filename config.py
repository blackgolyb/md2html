# App config
css_files = [
    "./resources/css/main_style.css",
    "./github-markdown-css/github-markdown.css",
]

js_files = [
    # "./template_script.js",
]

template_file = "./resources/templates/main_template.html"

apps = [
    {"preority": 0, "app": "theme_switcher", "options": {"value_name": "value"}},
    "app_name",
]


# Python markdown config
extensions = [
    "fenced_code",
    "tables",
    "pymdownx.blocks.admonition",
    "pymdownx.tasklist",
    "pymdownx.magiclink",
    "pymdownx.tabbed",
    "pymdownx.betterem",
    # 'pymdownx.highlight',
    "pymdownx.superfences",
    "pymdownx.arithmatex",
    "pymdownx.tilde",
    "pymdownx.progressbar",
    "pymdownx.keys",
]

extensions_config = {
    "pymdownx.arithmatex": {
        "generic": True,
        # 'genhjeric': False,
    }
    # "pymdownx.inlinehilite": {
    #     "custom_inline": [
    #         {"name": "math", "class": "arithmatex", "format": arithmatex.arithmatex_inline_format(which="generic")}
    #     ]
    # }
}
