class IntentRouter:

    def detect(self, command):

        command = command.lower().strip()

        if command.startswith("remember"):
            return "memory"

        if command.startswith("what is my"):
            return "memory"

        if command.startswith("open"):
            return "automation"

        if command.startswith("calc"):
            return "skill"

        return "ai"
