class IntentClassifier:

    def classify(self, command: str) -> str:

        text = command.lower().strip()

        if text.startswith("calc"):
            return "calculator"

        if text.startswith("remember"):
            return "memory"

        if text.startswith("what is my"):
            return "memory"

        if text.startswith("open"):
            return "automation"

        if text.startswith("close"):
            return "automation"

        if text.startswith("shutdown"):
            return "automation"

        if text.startswith("restart"):
            return "automation"

        return "ai"