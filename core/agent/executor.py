import os
import subprocess
import webbrowser

from core.device.app_database import AppDatabase


class GoalExecutor:

    def __init__(self):

        self.apps = AppDatabase()

        self.apps.load()

    def execute(self, goal):

        results = []

        for task in goal.tasks:

            task_lower = task.lower()

            # -------------------------
            # VS Code
            # -------------------------

            if "vs code" in task_lower:

                if self.apps.launch("visual studio code"):

                    results.append("Opened VS Code")

                else:

                    results.append("VS Code not found")

                continue

            # -------------------------
            # Git Bash
            # -------------------------

            if "git bash" in task_lower:

                try:

                    subprocess.Popen("git-bash.exe")

                    results.append("Opened Git Bash")

                except Exception:

                    results.append("Git Bash not found")

                continue

            # -------------------------
            # Ollama
            # -------------------------

            if "ollama" in task_lower:

                try:

                    subprocess.Popen("ollama serve")

                    results.append("Started Ollama")

                except Exception:

                    results.append("Unable to start Ollama")

                continue

            # -------------------------
            # Project Folder
            # -------------------------

            if "project folder" in task_lower:

                path = os.getcwd()

                os.startfile(path)

                results.append("Opened Project Folder")

                continue

            # -------------------------
            # Browser
            # -------------------------

            if "browser" in task_lower:

                webbrowser.open("https://google.com")

                results.append("Opened Browser")

                continue

            # -------------------------
            # Notes
            # -------------------------

            if "notes" in task_lower:

                self.apps.launch("notepad")

                results.append("Opened Notes")

                continue

            # -------------------------
            # PDF
            # -------------------------

            if "pdf" in task_lower:

                results.append("PDF Reader Placeholder")

                continue

            # -------------------------
            # Spotify
            # -------------------------

            if "spotify" in task_lower:

                if self.apps.launch("spotify"):

                    results.append("Opened Spotify")

                else:

                    results.append("Spotify not installed")

                continue

            results.append(f"Skipped: {task}")

        return results
