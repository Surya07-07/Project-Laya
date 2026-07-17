from core.guardian.guardian import Guardian


guardian = Guardian()


tests = [

    "I prefer Python",

    "My password is 12345",

    "My favorite movie is Interstellar"

]


for item in tests:

    result = guardian.check_memory(item)

    print(
        item,
        "=>",
        result
    )