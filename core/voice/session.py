import time


class VoiceSession:

    def __init__(self, timeout=20):

        self.timeout = timeout

        self.active = False

        self.last_activity = 0

    def start(self):

        self.active = True

        self.last_activity = time.time()

        print("🟢 Voice Session Started")

    def stop(self):

        self.active = False

        print("😴 Voice Session Ended")

    def touch(self):

        self.last_activity = time.time()

    def expired(self):

        if not self.active:

            return True

        return (time.time() - self.last_activity) > self.timeout

    def remaining(self):

        if not self.active:

            return 0

        return max(
            0,
            int(
                self.timeout -
                (time.time() - self.last_activity)
            )
        )
