from core.automation.file_executor import FileExecutor


class Executor:


    def __init__(self):

        self.file = FileExecutor()



    def execute(self, action, data):


        if action == "create_folder":

            return self.file.create_folder(
                data
            )


        elif action == "list_folder":

            return self.file.list_folder(
                data
            )


        else:

            return {
                "success": False,
                "message": "Unknown action"
            }
