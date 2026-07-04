from core.automation.system import SystemAutomation


class TaskRouter:

    def __init__(self, brain, plugin_manager):

        self.brain = brain
        self.plugin_manager = plugin_manager
        self.system = SystemAutomation()

    def route(self, command):

        command = command.strip()

        if command.startswith("calc "):

            expression = command[5:]

            return self.plugin_manager.execute(
                "calculator",
                expression
            )

        if command.startswith("open "):

            app = command[5:].strip()

            return self.system.open_app(app)

        return self.brain.execute(command)