class ActionRouter:


    def __init__(self):

        self.routes = {

            "create_folder":"file",

            "open_application":"desktop",

            "type_text":"type",

            "press_key":"key",

            "memory_save":"memory"

        }



    def route(self,intent):

        return self.routes.get(
            intent,
            "unknown"
        )
