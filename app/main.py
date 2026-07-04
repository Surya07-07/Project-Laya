from core.dna.dna import DNA
from core.heart.heart import Heart
from core.guardian.guardian import Guardian
from core.memory.memory import Memory
from core.gateway.gateway import Gateway


def main():
    print("=" * 45)
    print("          PROJECT IGRIS")
    print("               LAYA")
    print("=" * 45)
    print()

    # Initialize Core Modules
    dna = DNA()
    heart = Heart()
    guardian = Guardian()
    memory = Memory()
    gateway = Gateway()

    # Load Core Modules
    dna.load()
    heart.load()
    guardian.load()
    memory.load()
    gateway.load()

    print()

    # Test Heart Decision Engine
    decision = heart.decide("internet")
    print(f"Decision: {decision}")

    print()
    print("✅ System Ready")
    print("Hello Surya!")
    print("Laya Core v0.1 is running.")


if __name__ == "__main__":
    main()