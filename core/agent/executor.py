from core.automation.file_executor import FileExecutor
from core.automation.desktop_controller import DesktopController
from core.automation.memory_executor import MemoryExecutor


class Executor:


    def __init__(self):

        self.file = FileExecutor()
        self.desktop = DesktopController()
        self.memory = MemoryExecutor()



    def execute(self, tool, data):


        if tool == "file":

            return self.file.create_folder(
                "Laya_Test"
            )


        elif tool == "desktop":

            return self.desktop.open_app(
                data
            )


        elif tool == "type":

            return self.desktop.type_text(
                data
            )


        elif tool == "key":

            return self.desktop.press_key(
                data
            )


        elif tool == "memory":

            return self.memory.save(
                data
            )


        return {
            "success": False,
            "message": "Unknown tool"
        }
