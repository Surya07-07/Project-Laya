from core.intent.analyzer import IntentAnalyzer
from core.automation.system import SystemAutomation


class TaskRouter:

    def __init__(self, brain, plugin_manager):

        self.brain = brain
        self.plugin_manager = plugin_manager
        self.system = SystemAutomation()

        self.intent = IntentAnalyzer()

    def route(self, command):

        data = self.intent.analyze(command)

        intent = data["intent"]

        if intent == "calculator":
            return self.plugin_manager.execute(
                "calculator",
                data["expression"]
            )

        if intent == "open_app":
            return self.system.open_app(
                data["target"]
            )

        if intent == "remember_name":
            return self.brain.execute(
                f"remember my name is {data['name']}"
            )

        if intent == "recall_name":
            return self.brain.execute(
                "what is my name"
            )

        return self.brain.execute(
            data["message"]
        )