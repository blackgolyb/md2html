import importlib

import config

from .app import App
from .contracts import AppContentProvider


class AppsContentCompositor(AppContentProvider):
    contents_functions = [
        "get_styles",
        "get_scripts",
        "get_html",
    ]

    def __init__(self):
        self._apps = {}
        for contents_functions in self.contents_functions:
            self.__register_contents_function(contents_functions)

    def get_apps_by_priority(self):
        for priority in self._apps:
            for app in self._apps[priority]:
                yield app

    def __register_contents_function(self, content_function):
        setattr(self, content_function, lambda: self._get_content(content_function))

    def _get_content(self, content_function, separator="\n\n"):
        content = ""
        for app in self.get_apps_by_priority():
            if not hasattr(app, content_function):
                continue
            content += getattr(app, content_function)() + separator

        return content

    def get_apps(self):
        return self._apps

    def register_app(self, app: App, priority: int = 0) -> None:
        if priority not in self._apps:
            self._apps[priority] = []

        self._apps[priority].append(app)

    def load_apps_from_dir(self):
        for app_settings in config.apps:
            if isinstance(app_settings, str):
                app_settings = {
                    "app": app_settings,
                    "priority": 0,
                }

            app_module = importlib.import_module(f"{config.apps_dir}.{app_settings['app']}")

            if not hasattr(app_module, "App"):
                print(f"Could not load the app: {app_settings}")

            app = app_module.App(**app_settings.get("options", {}))

            self.register_app(app=app, priority=app_settings["priority"])
