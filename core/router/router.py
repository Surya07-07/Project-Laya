from core.automation.system import SystemAutomation


class TaskRouter:

    def __init__(self, brain, plugin_manager):

        self.brain = brain
        self.plugins = plugin_manager
        self.system = SystemAutomation()

    def route(self, command):

        command = command.strip()

        lower = command.lower()

        # Calculator
        if lower.startswith("calc "):
            expression = command[5:]
            return self.plugins.execute(
                "calculator",
                expression
            )

        # Open Applications
        if lower.startswith("open "):
            app = command[5:].strip()
            return self.system.open_app(app)

        # Memory
        if lower.startswith("remember"):
            return self.brain.execute(command)

        if lower == "what is my name":
            return self.brain.execute(command)

        # Everything else goes to AI
        return self.brain.execute(command)