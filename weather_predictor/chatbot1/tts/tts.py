from gtts import gTTS 
import os

def text_to_speech(text):
    try:
        static_dir = os.path.join(os.getcwd(), "chatbot1", "static")
        if not os.path.exists(static_dir):
            os.makedirs(static_dir)  # Create static folder if missing

        filename = os.path.join(static_dir, "response.mp3")
        tts = gTTS(text=text, lang="en")
        tts.save(filename)

        return filename  # Return the file path
    except Exception as e:
        print("TTS Error:", e)
        return None  # Handle errors gracefully
