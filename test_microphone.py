import sounddevice as sd

print("🎤 Available microphones:")
print(sd.query_devices())

print("\nRecording for 5 seconds...")
audio = sd.rec(int(5 * 16000), samplerate=16000, channels=1)

sd.wait()

print("✅ Recording completed")
