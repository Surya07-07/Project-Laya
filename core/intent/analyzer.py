class IntentAnalyzer:

    def analyze(self, command):

        command = command.strip().lower()

        if command.startswith("open "):
            return {"intent": "open_app", "target": command[5:].strip()}

        if command.startswith("calc "):
            return {"intent": "calculator", "expression": command[5:].strip()}

        if command.startswith("remember my name is"):
            return {"intent": "remember_name", "name": command[20:].strip()}

        if command == "what is my name":
            return {"intent": "recall_name"}

        return {"intent": "chat", "message": command}
