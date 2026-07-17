from core.device.app_database import AppDatabase

db = AppDatabase()

db.scan()

print()

print("Smart App Finder Ready")

print()

while True:

    query = input("You : ")

    if query == "exit":

        break

    if db.launch(query):

        print("Laya : Opened!")

    else:

        print("Laya : I couldn't find that application.")
