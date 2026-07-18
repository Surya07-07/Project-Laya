from core.memory.service import MemoryService

memory = MemoryService()


tests = ["My favorite language is Python", "My bank account number is 123456"]


for item in tests:

    print("\nINPUT:")
    print(item)

    result = memory.remember_sentence(item)

    print("RESULT:")
    print(result)
