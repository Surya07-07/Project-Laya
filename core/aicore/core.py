class AICore:

    def __init__(
        self,
        router,
        memory,
        gateway,
        heart,
        guardian,
        skill_manager
    ):

        self.router = router
        self.memory = memory
        self.gateway = gateway
        self.heart = heart
        self.guardian = guardian
        self.skills = skill_manager

    def process(self, command):

        response = self.skills.execute(command)

        if response is not None:
            return response

        return self.router.route(command)