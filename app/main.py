def main():
    print("=" * 40)
    print("        PROJECT IGRIS")
    print("             LAYA")
    print("=" * 40)
    print()

    modules = [
        "DNA",
        "Heart",
        "Guardian",
        "Memory",
        "Gateway"
    ]

    for module in modules:
        print(f"Loading {module:<10}...........OK")

    print()
    print("System Ready")
    print("Hello Surya.")
    print("Welcome to Laya!")
    print()

if __name__ == "__main__":
    main()