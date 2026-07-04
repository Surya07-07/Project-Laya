class DecisionEngine:

    def decide(self, command):

        command = command.lower().strip()

        if command.startswith("open "):
            return "automation"

        if command.startswith("calc "):
            return "calculator"

        if command.startswith("remember"):
            return "memory"

        if command == "what is my name":
            return "memory"

        return "ai"