from typing import Protocol


class AppContentProvider(Protocol):
    def get_styles(self):
        ...

    def get_scripts(self):
        ...

    def get_html(self):
        ...
