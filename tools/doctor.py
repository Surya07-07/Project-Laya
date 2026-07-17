import os
import sqlite3

print("=" * 50)
print("PROJECT LAYA DOCTOR")
print("=" * 50)

print()

# -----------------------
# Config
# -----------------------

if os.path.exists("data/config.json"):
    print("✓ Config Found")
else:
    print("✗ Missing data/config.json")

# -----------------------
# Memory
# -----------------------

if os.path.exists("data/memory.db"):

    print("✓ Memory Database Found")

    try:

        sqlite3.connect("data/memory.db").close()

        print("✓ Memory Database OK")

    except Exception as e:

        print("✗ Memory Error")
        print(e)

else:

    print("✗ Memory Database Missing")

# -----------------------
# Logs
# -----------------------

if os.path.exists("logs"):

    print("✓ Logs Folder")

else:

    print("✗ Logs Folder Missing")

# -----------------------
# Settings
# -----------------------

if os.path.exists("settings"):

    print("✓ Settings Folder")

else:

    print("✗ Settings Folder Missing")

print()

print("Doctor Finished.")
