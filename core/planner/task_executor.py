from core.device.app_database import AppDatabase
from core.desktop.controller import DesktopController


class TaskExecutor:

    def __init__(self):

        self.apps = AppDatabase()

        self.apps.load()

        self.desktop = DesktopController()

    def execute(self, task):

        if task.action == "open":

            if self.apps.launch(task.target):

                return f"Opened {task.target}"

            return f"Couldn't open {task.target}"

        if task.action == "google":

            self.desktop.search_google(task.target)

            return "Google Search Opened"

        if task.action == "youtube":

            self.desktop.search_youtube(task.target)

            return "YouTube Search Opened"

        return "Unknown task"
