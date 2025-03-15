from pathlib import Path

PROJECT_PATH = Path(__file__).absolute().parent
RESOURCES_PATH = PROJECT_PATH / "resources"

css_files = [
    RESOURCES_PATH / "css/main_style.css",
    RESOURCES_PATH / "css/theme_markdown.css",
]

js_files = [
    RESOURCES_PATH / "js/MathJax_init.js",
]

template_file = RESOURCES_PATH / "templates/main_template.html"

apps_dir = "apps"
apps = [
    # {"preority": 0, "app": "app", "options": {"value_name": "value"}},
    "theme_switcher",
]


# Python markdown config
extensions = [
    "fenced_code",
    "tables",
    "attr_list",
    "pymdownx.blocks.admonition",
    "pymdownx.details",
    "pymdownx.tasklist",
    "pymdownx.magiclink",
    "pymdownx.tabbed",
    "pymdownx.betterem",
    # 'pymdownx.highlight',
    "pymdownx.superfences",
    "pymdownx.arithmatex",
    "pymdownx.tilde",
    "pymdownx.progressbar",
    "pymdownx.emoji",
    "pymdownx.keys",
]

extensions_config = {
    "pymdownx.arithmatex": {
        "generic": True,
    }
    # "pymdownx.inlinehilite": {
    #     "custom_inline": [
    #         {"name": "math", "class": "arithmatex", "format": arithmatex.arithmatex_inline_format(which="generic")}
    #     ]
    # }
}
