from core.conversation.context import ConversationContext
from core.conversation.session import ConversationSession


class ConversationManager:

    def __init__(self):

        self.session = ConversationSession()

        self.context = ConversationContext()

    def user(self, text):

        self.session.next_turn()

        self.context.add("User", text)

    def assistant(self, text):

        self.context.add("Laya", text)

    def language(self, code):

        self.session.update_language(code)

    def emotion(self, emotion):

        self.session.update_emotion(emotion)

    def prompt(self):

        return self.context.build()

    def info(self):

        return self.session.summary()
