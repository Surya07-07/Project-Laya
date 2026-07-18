from core.memory.privacy.permission import MemoryPermission

permission = MemoryPermission()


tests = ["I prefer Python", "My bank account number is 123456"]


for item in tests:

    result = permission.check(item)

    print(item)

    print(result)

    print()
