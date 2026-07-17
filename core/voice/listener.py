class Listener:

    def __init__(self):

        self.active = False

    def start(self):

        self.active = True

        print("👂 Listener active")

    def stop(self):

        self.active = False

        print("👂 Listener stopped")
