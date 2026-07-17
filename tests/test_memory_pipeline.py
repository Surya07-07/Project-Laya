from core.memory.service import MemoryService


memory = MemoryService()


tests = [

    "My name is Surya",

    "My city is Hyderabad",

    "I prefer Python",

    "My favorite movie is Interstellar"

]


for sentence in tests:

    result = memory.remember_sentence(sentence)

    print(sentence)

    print(result)

    print()