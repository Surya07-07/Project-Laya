from core.automation.app_indexer import AppIndexer
from core.automation.browser import Browser


class AutomationManager:

    def __init__(self):

        self.browser = Browser()

        self.indexer = AppIndexer()

        print("🔍 Scanning installed applications...")

        count = len(self.indexer.scan())

        print(f"✅ {count} applications indexed")

    def handle(self, command):

        command = command.lower().strip()

        if command.startswith("open "):

            target = command[5:]

            if "." in target:

                self.browser.open(target)

                return f"Opening {target}"

            if self.indexer.launch(target):

                return f"Opening {target}"

            return f"I couldn't find '{target}'."

        return None
