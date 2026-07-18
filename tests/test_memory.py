from core.memory.memory import Memory

memory = Memory()

memory.load()

memory.learn("My name is Surya")

print(memory.recall("name"))
