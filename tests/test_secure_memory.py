from core.memory.service import MemoryService


memory = MemoryService()


tests = [

    "My name is Surya",

    "I prefer Python",

    "My password is 12345",

    "My favorite movie is Interstellar"

]


for item in tests:

    result = memory.remember_sentence(item)

    print("\nINPUT:")
    print(item)

    print("RESULT:")
    print(result)