import os
import subprocess


class AppIndexer:

    def __init__(self):

        self.apps = {}

    def scan(self):

        locations = [

            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",

            os.path.expandvars(
                r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"
            )
        ]

        self.apps.clear()

        for root in locations:

            if not os.path.exists(root):
                continue

            for path, dirs, files in os.walk(root):

                for file in files:

                    if file.lower().endswith(".lnk"):

                        name = file[:-4].lower()

                        self.apps[name] = os.path.join(path, file)

        return self.apps

    def search(self, query):

        query = query.lower()

        for name in self.apps:

            if query == name:

                return self.apps[name]

        for name in self.apps:

            if query in name:

                return self.apps[name]

        return None

    def launch(self, query):

        shortcut = self.search(query)

        if shortcut is None:

            return False

        os.startfile(shortcut)

        return True
