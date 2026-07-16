from collections import deque
from datetime import datetime
from .message import Message


class ConversationHistory:

    def __init__(self, limit=20):
        self.messages = deque(maxlen=limit)

    def add_user(self, text):
        self.messages.append(
            Message("user", text, datetime.now())
        )

    def add_assistant(self, text):
        self.messages.append(
            Message("assistant", text, datetime.now())
        )

    def get_messages(self):
        return list(self.messages)

    def clear(self):
        self.messages.clear()