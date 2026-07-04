class Guardian:
    def __init__(self):
        self.protection = True
        self.allowed_actions = [
            "open_app",
            "read_file",
            "remember",
            "speak"
        ]

    def load(self):
        print("🛡️ Guardian Loaded")

    def authorize(self, action):
        print(f"🛡️ Checking permission for: {action}")

        if action == "internet":
            return False

        if action in self.allowed_actions:
            return True

        return False