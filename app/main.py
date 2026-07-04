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

    # Save information
    memory.remember("name", "Surya")
    memory.remember("favorite_color", "Blue")

    print()

    # Recall information
    print("Name:", memory.recall("name"))
    print("Favorite Color:", memory.recall("favorite_color"))

    print()

    print("✅ Memory Test Completed")
    print("Laya Core v0.3")


if __name__ == "__main__":
    main()