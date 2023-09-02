from typing import Literal, Any
from .app import App


class AppsController:
    def __init__(self):
        self._apps = {}
        
    def get_apps_by_priority(self):
        for priority in self._apps:
            for app in self._apps[priority]:
                yield app
    
    def get_styles(self):
        styles = ''
        for app in self.get_apps_by_priority():
            styles += app.get_style()
            
        return styles
    
    def get_scripts(self):
        scripts = ''
        for app in self.get_apps_by_priority():
            scripts += app.get_scripts()
            
        return scripts
    
    def get_html(self):
        html = ''
        for app in self.get_apps_by_priority():
            html += app.get_html()
            
        return html
        
    def register_app(self, app: App, priority: int = 0) -> None:
        if isinstance(app, App):
            raise ValueError(f'app: {app} must be a chield of App class.')
        
        if priority not in self._apps:
            self._apps[priority] = []
            
        self._apps[priority].append(app)
        

app_options_type = dict[str, Any]
extended_app_type_for_apps_type = dict[
    Literal['priority', 'app', 'options'],
    App | app_options_type | int
]
apps_type = dict[App | extended_app_type_for_apps_type]

def register_apps(self, apps: apps_type, controller: AppsController):
    default_priority = 0
    
    for app_conf in apps:
        if issubclass(app_conf, App):
            app_cls = app_conf
            priority = default_priority
            
            app = app_cls()
            
        elif isinstance(app_conf, dict):
            priority = app_conf.get('priority', default=default_priority)
            options = app_conf.get('options', default={})
            app_cls = app_conf['app']
            
            app = app_cls(options)
            
            
        controller.register_app(app=app, priority=priority)
