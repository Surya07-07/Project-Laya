from core.memory.memory import Memory

memory = Memory()

memory.load()

memory.remember("my city", "Warangal")

memory.remember("favorite language", "Python")

memory.remember("exam", "Tomorrow")

print(memory.recall("my city"))

print()

for item in memory.database.all():
    print(item)
