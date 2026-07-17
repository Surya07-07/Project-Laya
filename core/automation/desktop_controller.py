import pyautogui
import subprocess


class DesktopController:


    def __init__(self):

        self.apps = {

            "notepad":
            "notepad.exe",

            "calculator":
            "calc.exe",

            "paint":
            "mspaint.exe",

            "cmd":
            "cmd.exe",

            "terminal":
            "wt.exe",

            "explorer":
            "explorer.exe"

        }



    def open_app(self, app):

        try:

            app = app.lower().strip()


            # Remove command words
            remove_words = [
                "open",
                "launch",
                "start"
            ]


            for word in remove_words:

                app = app.replace(
                    word,
                    ""
                )


            app = app.strip()



            if app in self.apps:

                command = self.apps[app]

            else:

                command = app



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

        pyautogui.write(
            text,
            interval=0.05
        )


        return {

            "success": True,

            "message":
            "Text typed"

        }



    def press_key(self, key):

        pyautogui.press(
            key
        )


        return {

            "success": True,

            "message":
            f"Pressed {key}"

        }
