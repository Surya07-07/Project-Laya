from core.memory.memory import Memory

memory = Memory()
memory.load()

memory.learn("My favorite movie is Interstellar")
memory.learn("My city is Hyderabad")

print(memory.recall("favorite_movie"))
print(memory.recall("city"))
