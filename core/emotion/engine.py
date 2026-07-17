from core.emotion.detector import EmotionDetector


class EmotionEngine:

    def __init__(self):

        self.detector = EmotionDetector()
        self.current = None

    def update(self, sentence):

        self.current = self.detector.detect(sentence)
        return self.current