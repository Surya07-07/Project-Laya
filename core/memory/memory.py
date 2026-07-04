from core.memory.database import Database


class Memory:
    def __init__(self):
        self.database = Database()

    def load(self):
        self.database.initialize()
        print("📦 Memory Vault Loaded")

    def remember(self, key, value):
        self.database.save(key, value)
        print(f"💾 Saved: {key}")

    def recall(self, key):
        return self.database.get(key)