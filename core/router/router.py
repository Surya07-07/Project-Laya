from core.automation.system import SystemAutomation
from core.brain.decision import DecisionEngine


class TaskRouter:

    def __init__(self, brain, plugin_manager):

        self.brain = brain
        self.plugins = plugin_manager
        self.system = SystemAutomation()

        self.decision = DecisionEngine()

    def route(self, command):

        task = self.decision.decide(command)

        if task == "automation":

            return self.system.open_app(command[5:].strip())

        if task == "calculator":

            return self.plugins.execute("calculator", command[5:])

        if task == "memory":

            return self.brain.execute(command)

        return self.brain.execute(command)
