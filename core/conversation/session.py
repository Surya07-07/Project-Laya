from datetime import datetime


class ConversationSession:

    def __init__(self):

        self.started = datetime.now()

        self.language = "en"

        self.emotion = "neutral"

        self.turns = 0

    def update_language(self, language):

        self.language = language

    def update_emotion(self, emotion):

        self.emotion = emotion

    def next_turn(self):

        self.turns += 1

    def summary(self):

        return {
            "language": self.language,
            "emotion": self.emotion,
            "turns": self.turns,
            "started": self.started.isoformat()
        }
