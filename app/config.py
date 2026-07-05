import json
from pathlib import Path


class Config:
    def __init__(self):
        config_file = Path("data") / "config.json"

        with open(config_file, "r", encoding="utf-8") as file:
            self.data = json.load(file)

    def get(self, *keys):
        value = self.data

        for key in keys:
            value = value[key]

        return value
