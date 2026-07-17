from core.memory.database import Database
from core.memory.ranker import MemoryRanker
from core.memory.types import MemoryType
from core.memory.semantic import SemanticMemory
from core.memory.extractor import MemoryExtractor
from core.memory.extractor import MemoryExtractor


class Memory:

    def __init__(self):
        self.database = Database()
        self.ranker = MemoryRanker()
        self.semantic = SemanticMemory()
        self.extractor = MemoryExtractor()

    def load(self):
        self.database.initialize()
        print("📦 Memory Vault Loaded")

    def remember(self, key, value):

        text = f"{key} {value}"

        memory_type = self.ranker.classify(text)

        if memory_type == MemoryType.IGNORE:
            print("⚪ Ignored Memory")
            return

        importance = {
            "permanent": 10,
            "important": 8,
            "temporary": 5,
            "ignore": 0
        }

        self.database.save(
            key=key,
            value=value,
            memory_type=memory_type.value,
            importance=importance[memory_type.value]
        )

        print(f"💾 Saved ({memory_type.value}): {key}")

    def learn(self, sentence):

        result = self.extractor.extract(sentence)

        if result is None:
            return

        key, value = result

        self.remember(key, value)

    def recall(self, question):

        key = self.semantic.find_key(question)

        if key:
            value = self.database.get(key)

            if value:
                return value

        return self.database.get(question)