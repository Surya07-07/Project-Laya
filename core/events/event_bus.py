class EventBus:

    def __init__(self):
        self.listeners = {}

    def subscribe(self, event, callback):

        if event not in self.listeners:
            self.listeners[event] = []

        self.listeners[event].append(callback)

    def publish(self, event, data=None):

        callbacks = self.listeners.get(event, [])

        for callback in callbacks:
            callback(data)
