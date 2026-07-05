from core.voice.audio import AudioRecorder
from core.voice.whisper_engine import WhisperEngine

audio = AudioRecorder()

engine = WhisperEngine()

filename = audio.record()

text = engine.transcribe(filename)

print()

print("You said:")

print(text)