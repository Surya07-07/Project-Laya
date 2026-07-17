from core.device.app_database import AppDatabase

db = AppDatabase()

apps = db.scan()

db.save()

print()

print("=" * 60)

print("Installed Applications")

print("=" * 60)

for i, app in enumerate(sorted(apps.keys())):

    print(f"{i+1:03}  {app}")

print()

print("Total:", len(apps))

print()

while True:

    command = input("Launch App (exit): ")

    if command.lower() == "exit":

        break

    if db.launch(command):

        print("✅ Application Started")

    else:

        print("❌ Application Not Found")
