from core.automation.app_indexer import AppIndexer

apps = AppIndexer()

database = apps.scan()

print()

print("Installed Apps")

print("=" * 50)

for i, app in enumerate(sorted(database.keys())[:100]):

    print(i + 1, app)

print()

while True:

    name = input("Open App (exit to quit): ")

    if name == "exit":
        break

    if apps.launch(name):

        print("Opened.")

    else:

        print("Not found.")
