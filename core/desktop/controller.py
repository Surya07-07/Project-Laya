import os
import webbrowser
import subprocess
import pyautogui


class DesktopController:

    def open_folder(self, folder):

        folders = {
            "desktop": os.path.join(os.path.expanduser("~"), "Desktop"),
            "downloads": os.path.join(os.path.expanduser("~"), "Downloads"),
            "documents": os.path.join(os.path.expanduser("~"), "Documents"),
            "pictures": os.path.join(os.path.expanduser("~"), "Pictures"),
            "videos": os.path.join(os.path.expanduser("~"), "Videos")
        }

        folder = folder.lower()

        if folder in folders:

            os.startfile(folders[folder])

            return True

        return False

    def search_google(self, query):

        webbrowser.open(
            "https://www.google.com/search?q=" + query
        )

    def search_youtube(self, query):

        webbrowser.open(
            "https://www.youtube.com/results?search_query=" + query
        )

    def open_github(self):

        webbrowser.open("https://github.com")

    def screenshot(self):

        image = pyautogui.screenshot()

        image.save("data/screenshot.png")

        return "data/screenshot.png"

    def lock_pc(self):

        subprocess.run(
            "rundll32.exe user32.dll,LockWorkStation"
        )
