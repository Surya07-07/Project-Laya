from core.conversation.history import ConversationHistory


class Gateway:

    def __init__(self):

        self.history = ConversationHistory()

    def load(self):

        print("🌐 Gateway Loaded")
