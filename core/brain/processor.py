class CommandProcessor:
    def __init__(self, memory, heart):
        self.memory = memory
        self.heart = heart

    def execute(self, command):
        command = command.strip().lower()

        if command == "who are you":
            return "I am Laya, your private AI assistant."

        if command == "remember my name":
            if self.heart.decide("remember") == "Approved":
                self.memory.remember("name", "Surya")
                return "I'll remember your name."

        if command == "what is my name":
            name = self.memory.recall("name")
            if name:
                return f"Your name is {name}."
            return "I don't know your name yet."

        if command == "internet":
            return self.heart.decide("internet")

        return "Sorry, I don't understand that command yet."