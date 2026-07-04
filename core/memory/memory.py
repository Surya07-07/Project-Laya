from core.memory.database import Database


class Memory:
    def __init__(self):
        self.database = Database()

    def load(self):
        self.database.initialize()
        print("📦 Memory Vault Loaded")