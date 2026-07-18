import subprocess


class AppLauncher:

    APPS = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "cmd": "cmd.exe",
        "explorer": "explorer.exe",
    }

    def open(self, app):

        app = app.lower()

        if app not in self.APPS:

            return False

        subprocess.Popen(self.APPS[app])

        return True
