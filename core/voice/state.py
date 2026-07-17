from enum import Enum


class VoiceState(Enum):

    SLEEPING = "sleeping"

    LISTENING = "listening"

    THINKING = "thinking"

    SPEAKING = "speaking"

    STOPPED = "stopped"
