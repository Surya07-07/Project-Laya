from core.dna.dna import DNA
from core.heart.heart import Heart
from core.guardian.guardian import Guardian
from core.memory.memory import Memory
from core.gateway.gateway import Gateway


def main():
    print("=" * 50)
    print("             PROJECT IGRIS")
    print("                  LAYA")
    print("=" * 50)
    print()

    dna = DNA()
    guardian = Guardian()
    heart = Heart(guardian)
    memory = Memory()
    gateway = Gateway()

    dna.load()
    guardian.load()
    heart.load()
    memory.load()
    gateway.load()

    print()

    actions = [
        "open_app",
        "remember",
        "internet",
        "delete_file"
    ]

    for action in actions:
        result = heart.decide(action)
        print(f"{action:15} -> {result}")

    print()
    print("✅ System Ready")
    print("Laya Core v0.2")


if __name__ == "__main__":
    main()