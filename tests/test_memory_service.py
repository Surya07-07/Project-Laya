from core.memory.service import MemoryService

memory = MemoryService()


print(memory.remember("favorite_language", "Python"))


print("Recall:", memory.recall("favorite_language"))


print("All memories:")

for item in memory.memories():
    print(item)
