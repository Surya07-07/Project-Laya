from core.memory.memory import Memory

memory = Memory()

memory.load()

memory.remember("my name", "Surya")

memory.remember("exam", "Tomorrow")

memory.remember("hello", "there")

print()

print(memory.recall("my name"))
