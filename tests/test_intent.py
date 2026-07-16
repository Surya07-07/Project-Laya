from core.intent.classifier import IntentClassifier

classifier = IntentClassifier()

tests = [
    "calc 10+20",
    "remember my city is Hyderabad",
    "what is my city",
    "open notepad",
    "hello",
]

for command in tests:
    print(command, "->", classifier.classify(command))