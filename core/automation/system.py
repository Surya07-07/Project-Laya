import subprocess
import platform


class SystemAutomation:

    def __init__(self):
        self.apps = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
            "cmd": "cmd.exe",
            "explorer": "explorer.exe"
        }

    def open_app(self, app_name):

        if platform.system() != "Windows":
            return "Automation currently supports Windows only."

        app = self.apps.get(app_name.lower())

        if app is None:
            return f"Unknown application: {app_name}"

        try:
            subprocess.Popen(app)
            return f"Opening {app_name}..."

        except Exception as error:
            return f"Failed: {error}"