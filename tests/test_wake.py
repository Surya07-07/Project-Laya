from core.voice.wake_detector import WakeDetector

detector = WakeDetector()


tests = ["hey laya", "Hey Leia", "hello laya", "hey layer", "good morning"]


for text in tests:

    result = detector.detect(text)

    print(text, "=>", result)
