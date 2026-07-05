from core.voice.audio import AudioRecorder
from core.voice.whisper_engine import WhisperEngine


class VoiceService:

    def __init__(self):
        self.recorder = AudioRecorder()
        self.engine = WhisperEngine()

    def listen(self):

        filename = self.recorder.record()

        text = self.engine.transcribe(filename)

        return text