import sys
from pathlib import Path

from .contracts import AppContentProvider


def read_inner_files_and_concat(directory: Path, separator: str = "\n\n") -> str:
    content = ""
    for item in directory.iterdir():
        if not item.is_file():
            continue
        content += item.read_text() + separator
    return content


class App(AppContentProvider):
    CSS_FOLDER = "css"
    JS_FOLDER = "js"
    RESOURCES_FOLDER = "resources"
    resources_folder: Path

    def __init__(self):
        app_file_path = sys.modules[self.__class__.__module__].__file__
        self.resources_folder = Path(app_file_path).parent / self.RESOURCES_FOLDER

    def get_styles(self):
        return read_inner_files_and_concat(self.resources_folder / self.CSS_FOLDER)

    def get_scripts(self):
        return read_inner_files_and_concat(self.resources_folder / self.JS_FOLDER)

    def get_html(self):
        return ""
