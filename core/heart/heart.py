class Heart:
    def __init__(self):
        self.status = "Ready"

    def load(self):
        print("❤️ Heart Loaded")

    def decide(self, action: str):
        print(f"❤️ Thinking about: {action}")

        if action.lower() == "internet":
            return "Permission Required"

        return "Approved"