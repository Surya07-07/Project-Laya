import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.memory.classifier import MemoryClassifier

classifier = MemoryClassifier()


def test_memory():

    result = classifier.classify("My name is Surya")

    print(result)


if __name__ == "__main__":
    test_memory()
