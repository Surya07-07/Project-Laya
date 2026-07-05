class AICore:

    def __init__(
        self,
        router,
        memory,
        gateway,
        heart,
        guardian
    ):

        self.router = router
        self.memory = memory
        self.gateway = gateway
        self.heart = heart
        self.guardian = guardian

    def process(self, command):

        command = command.strip()

        if not command:
            return "Please say something."

        return self.router.route(command)