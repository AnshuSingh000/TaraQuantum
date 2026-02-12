import pyttsx3

class TaraVoice:
    def __init__(self):
        # We don't initialize the engine here anymore to prevent it from getting stuck.
        print("🔊 Audio System: ONLINE")

    def speak(self, text):
        print(f"🗣️  TARA: {text}") 
        
        try:
            # Re-initialize the engine every time we speak (The "Reset" Fix)
            engine = pyttsx3.init()
            
            # Set properties again
            engine.setProperty('rate', 175)
            engine.setProperty('volume', 1.0)
            
            # Find female/Samantha voice
            voices = engine.getProperty('voices')
            for voice in voices:
                if "female" in voice.name.lower() or "samantha" in voice.name.lower():
                    engine.setProperty('voice', voice.id)
                    break
            
            # Speak and then destroy the engine
            engine.say(text)
            engine.runAndWait()
            
            # Explicitly stop the loop to free up memory
            engine.stop()
            
        except Exception as e:
            print(f"⚠️ Voice Error: {e}")