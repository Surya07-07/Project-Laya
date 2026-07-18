from core.memory.ranker import MemoryRanker

ranker = MemoryRanker()


tests = [
    "My name is Surya",
    "I have an exam tomorrow",
    "Current task install packages",
    "Random information",
]


for item in tests:

    result = ranker.rank(item)

    print(item, "=>", result)
