from core.memory.memory import Memory

memory = Memory()

memory.load()

memory.remember("city", "Warangal")
memory.remember("name", "Surya")

print(memory.recall("Where do I live?"))
print(memory.recall("What is my hometown?"))
print(memory.recall("What is my name?"))
