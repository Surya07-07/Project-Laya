from core.emotion.engine import EmotionEngine

engine = EmotionEngine()

tests = [
    "I am happy today",
    "I feel sad",
    "I am stressed about exams",
    "I am angry",
    "I am excited"
]

for text in tests:
    print(text, "->", engine.update(text).value)