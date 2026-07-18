class Goal:

    def __init__(self, description):
        self.description = description
        self.steps = []
        self.status = "created"
        self.risk = "unknown"
        self.permission_required = False

    def add_step(self, step):
        self.steps.append(step)

    def update_status(self, status):
        self.status = status

    def show(self):
        return {
            "goal": self.description,
            "steps": self.steps,
            "status": self.status,
            "risk": self.risk,
            "permission": self.permission_required,
        }
