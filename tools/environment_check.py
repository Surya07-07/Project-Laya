import importlib

packages = ["ollama", "sqlite3", "requests"]

print("=" * 50)
print("PROJECT LAYA ENVIRONMENT CHECK")
print("=" * 50)

for package in packages:

    try:
        importlib.import_module(package)
        print(f"✓ {package}")

    except Exception as e:
        print(f"✗ {package}")
        print(e)

print()
print("Environment check complete.")
