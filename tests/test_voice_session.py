import time

from core.voice.session import VoiceSession

session = VoiceSession(timeout=10)

session.start()

while True:

    print()

    print("Remaining:", session.remaining())

    if session.expired():

        session.stop()

        break

    time.sleep(1)
