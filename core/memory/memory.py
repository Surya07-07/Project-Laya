from core.memory.database import Database
from core.memory.ranker import MemoryRanker
from core.memory.types import MemoryType


class Memory:

    def __init__(self):

        self.database = Database()
        self.ranker = MemoryRanker()

    def load(self):

        self.database.initialize()

        print("📦 Memory Vault Loaded")

    def remember(self, key, value):

        text = f"{key} {value}"

        memory_type = self.ranker.classify(text)

        if memory_type == MemoryType.IGNORE:

            print("⚪ Ignored Memory")

            return

        self.database.save(key, value)

        print(
            f"💾 Saved ({memory_type.value}): {key}"
        )

    def recall(self, key):

        return self.database.get(key)