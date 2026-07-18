from core.voice.agent_bridge import VoiceAgentBridge
from core.voice.speech_recognizer import SpeechRecognizer
from core.voice.voice_response import LayaVoice
from core.voice.wake_word import WakeWordDetector

wake = WakeWordDetector()

speech = SpeechRecognizer()

brain = VoiceAgentBridge()

voice = LayaVoice()


print("""
=========================
       PROJECT IGRIS
           LAYA

      FULL VOICE MODE
=========================
""")


while True:

    if wake.detected():

        voice.speak("Yes, I am listening")

        command = speech.transcribe()

        print("Command:", command)

        if command:

            result = brain.process_voice(command)

            message = str(result)

            voice.speak("Task completed")

            print(result)
