class PluginManager:

    def __init__(self):
        self.plugins = {}

    def register(self, name, plugin):
        self.plugins[name] = plugin

    def execute(self, name, *args):
        if name not in self.plugins:
            return f"Plugin '{name}' not found."

        return self.plugins[name].run(*args)

    def list_plugins(self):
        return list(self.plugins.keys())