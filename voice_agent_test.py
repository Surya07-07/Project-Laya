from core.voice.agent_bridge import VoiceAgentBridge
from core.voice.speech_recognizer import SpeechRecognizer



laya = VoiceAgentBridge()

speech = SpeechRecognizer()



print("""
=========================
      PROJECT IGRIS
          LAYA

      REAL VOICE MODE
=========================
""")


while True:


    text = speech.transcribe()


    if not text:

        continue



    print(
        "\n🎤 Heard:",
        text
    )


    if text.lower() in [
        "exit",
        "quit"
    ]:

        break



    result = laya.process_voice(
        text
    )


    print(
        "\nLaya:"
    )

    print(
        result
    )
