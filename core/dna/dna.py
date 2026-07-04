import json
from pathlib import Path


class DNA:
    def __init__(self):
        self.data = {}

    def load(self):
        dna_file = Path("data") / "dna.json"

        with open(dna_file, "r", encoding="utf-8") as file:
            self.data = json.load(file)

        print(f"🧬 DNA Loaded")
        print(f"Name    : {self.data['name']}")
        print(f"Version : {self.data['version']}")