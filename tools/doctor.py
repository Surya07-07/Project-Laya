import json
import os
import sqlite3
import urllib.request

print("=" * 60)
print("              PROJECT LAYA DOCTOR")
print("=" * 60)

passed = 0
failed = 0


def check(name, condition):

    global passed, failed

    if condition:
        print(f"✓ {name}")
        passed += 1
    else:
        print(f"✗ {name}")
        failed += 1


# ---------------------------------
# Config
# ---------------------------------

config_exists = os.path.exists("data/config.json")
check("Config File", config_exists)

if config_exists:

    try:

        with open("data/config.json", "r", encoding="utf-8") as f:
            json.load(f)

        check("Config JSON", True)

    except Exception:

        check("Config JSON", False)


# ---------------------------------
# Memory
# ---------------------------------

db_exists = os.path.exists("data/memory.db")
check("Memory Database", db_exists)

if db_exists:

    try:

        sqlite3.connect("data/memory.db").close()
        check("SQLite", True)

    except Exception:

        check("SQLite", False)


# ---------------------------------
# Directories
# ---------------------------------

folders = ["logs", "data", "settings", "core", "plugins", "skills", "tests"]

for folder in folders:

    check(folder, os.path.exists(folder))


# ---------------------------------
# Ollama
# ---------------------------------

try:

    urllib.request.urlopen("http://127.0.0.1:11434/api/version", timeout=2)

    check("Ollama Server", True)

except Exception:

    check("Ollama Server", False)


# ---------------------------------
# Models
# ---------------------------------

if config_exists:

    try:

        with open("data/config.json", "r") as f:

            cfg = json.load(f)

        model = cfg["ai"]["model"]

        print()
        print("Configured Model :", model)

    except Exception:

        print("Unable to read configured model.")

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)

print(f"Passed : {passed}")
print(f"Failed : {failed}")

if failed == 0:
    print("\n🎉 Laya is healthy.")
else:
    print("\n⚠ Some checks failed.")
