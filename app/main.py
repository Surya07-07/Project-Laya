from core.dna.dna import DNA
from core.guardian.guardian import Guardian
from core.heart.heart import Heart
from core.memory.memory import Memory
from core.gateway.gateway import Gateway
from core.brain.processor import CommandProcessor


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

    brain = CommandProcessor(memory, heart)

    print("\nLaya Ready.")
    print("Type 'exit' to quit.\n")

    while True:

        command = input("You: ")

        if command.lower() == "exit":
            print("Laya: Goodbye!")
            break

        response = brain.execute(command)

        print("Laya:", response)


if __name__ == "__main__":
    main()