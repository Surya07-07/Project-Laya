import pyautogui
import subprocess


class DesktopController:


    def __init__(self):

        self.apps = {

            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
            "cmd": "cmd.exe",
            "terminal": "wt.exe",
            "explorer": "explorer.exe"

        }



    def open_app(self, app):

        app = app.lower().strip()


        for word in [
            "open",
            "launch",
            "start",
            "you:"
        ]:

            app = app.replace(
                word,
                ""
            )


        app = app.strip()


        try:

            command = self.apps.get(
                app,
                app
            )


            subprocess.Popen(
                command,
                shell=True
            )


            return {

                "success": True,

                "message":
                f"Opened {app}"

            }


        except Exception as e:


            return {

                "success": False,

                "error": str(e)

            }



    def type_text(self, text):

        try:

            pyautogui.write(
                text,
                interval=0.05
            )

            return {

                "success": True,

                "message":
                "Text typed"

            }


        except Exception as e:

            return {

                "success": False,

                "error": str(e)

            }



    def press_key(self, key):

        try:

            pyautogui.press(
                key
            )

            return {

                "success": True,

                "message":
                f"Pressed {key}"

            }


        except Exception as e:

            return {

                "success": False,

                "error": str(e)

            }
