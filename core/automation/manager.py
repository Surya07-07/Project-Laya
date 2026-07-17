from core.automation.app_launcher import AppLauncher
from core.automation.browser import Browser
from core.automation.system import SystemAutomation


class AutomationManager:

    def __init__(self):

        self.apps = AppLauncher()

        self.browser = Browser()

        self.system = SystemAutomation()

    def handle(self, command):

        cmd = command.lower()

        if cmd.startswith("open "):

            app = cmd.replace("open ", "")

            if self.apps.open(app):

                return f"Opening {app}"

            if "." in app:

                self.browser.open(app)

                return f"Opening {app}"

            return "Application not found."

        return None
