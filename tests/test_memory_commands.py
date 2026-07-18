from core.memory.commands import MemoryCommandProcessor

laya_memory = MemoryCommandProcessor()


commands = [
    "Laya show my memories",
    "Laya forget my city",
    "Laya lock memory",
    "Laya show my memories",
    "Laya unlock memory",
]


for command in commands:

    print("\nCOMMAND:")
    print(command)

    print(laya_memory.process(command))
