from core.memory.memory import Memory

memory = Memory()
memory.load()

conversation = [
    "My name is Surya",
    "My city is Hyderabad",
    "My favorite movie is Interstellar",
    "I prefer Python",
]

for sentence in conversation:
    memory.learn(sentence)

print(memory.recall("name"))
print(memory.recall("city"))
print(memory.recall("favorite_movie"))
print(memory.recall("preference"))
