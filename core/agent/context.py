class AgentContext:

    def __init__(self):

        self.command = ""

        self.memory = None

        self.emotion = "neutral"

        self.intent = "chat"

        self.response = ""

    def reset(self):

        self.command = ""
        self.memory = None
        self.emotion = "neutral"
        self.intent = "chat"
        self.response = ""
