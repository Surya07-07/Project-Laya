class PluginManager:

    def __init__(self):
        self.plugins = {}

    def register(self, name, plugin):
        self.plugins[name] = plugin

    def execute(self, name, *args):

        plugin = self.plugins.get(name)

        if plugin is None:
            return f"Plugin '{name}' not found."

        return plugin.run(*args)

    def available(self):
        return list(self.plugins.keys())
