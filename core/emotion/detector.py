from core.emotion.types import Emotion


class EmotionDetector:

    def detect(self, text):

        text = text.lower()

        if any(word in text for word in (
            "happy",
            "great",
            "awesome",
            "good",
            "fantastic",
            "wonderful"
        )):
            return Emotion.HAPPY

        if any(word in text for word in (
            "sad",
            "cry",
            "depressed",
            "upset"
        )):
            return Emotion.SAD

        if any(word in text for word in (
            "angry",
            "mad",
            "furious"
        )):
            return Emotion.ANGRY

        if any(word in text for word in (
            "stress",
            "stressed",
            "anxious",
            "exam"
        )):
            return Emotion.STRESSED

        if any(word in text for word in (
            "excited",
            "can't wait"
        )):
            return Emotion.EXCITED

        return Emotion.NEUTRAL