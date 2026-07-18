import json
import os

from core.device.app_matcher import AppMatcher


class AppDatabase:

    def __init__(self):

        self.apps = {}

        self.locations = [
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
            os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"),
            os.path.join(os.path.expanduser("~"), "Desktop"),
        ]

    def scan(self):

        self.apps.clear()

        for location in self.locations:

            if not os.path.exists(location):
                continue

            for root, dirs, files in os.walk(location):

                for file in files:

                    if file.lower().endswith(".lnk"):

                        name = file[:-4].lower()

                        self.apps[name] = os.path.join(root, file)

        return self.apps

    def save(self):

        os.makedirs("data", exist_ok=True)

        with open("data/apps.json", "w", encoding="utf-8") as f:

            json.dump(self.apps, f, indent=4)

    def load(self):

        if not os.path.exists("data/apps.json"):

            return {}

        with open("data/apps.json", "r", encoding="utf-8") as f:

            self.apps = json.load(f)

        return self.apps

    def search(self, name):

        name = name.lower()

        # Exact match
        if name in self.apps:

            return self.apps[name]

        # Partial match
        for app in self.apps:

            if name in app:

                return self.apps[app]

        return None

    def launch(self, query):

        if not self.apps:
            self.load()

        matcher = AppMatcher(self)

        shortcut = matcher.find(query)

        if shortcut is None:
            return False

        try:
            os.startfile(shortcut)
            return True
        except Exception as e:
            print("Launch Error:", e)
            return False
