class ActionRouter:


    def __init__(self):

        self.routes = {

            "create_folder":
            "file",


            "open_application":
            "desktop",


            "memory_save":
            "memory",


            "search":
            "browser"

        }



    def route(self, intent):

        tool = self.routes.get(
            intent,
            "unknown"
        )


        return tool
