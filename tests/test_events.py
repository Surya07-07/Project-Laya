import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.events.event_bus import EventBus

bus = EventBus()


def hello(data):
    print("Event:", data)


bus.subscribe("test", hello)

bus.publish("test", "Laya Started")
