class Heart:
    def __init__(self, guardian):
        self.guardian = guardian

    def load(self):
        print("❤️ Heart Loaded")

    def decide(self, action):
        print(f"❤️ Thinking about: {action}")

        if self.guardian.authorize(action):
            return "Approved"

        return "Permission Required"
