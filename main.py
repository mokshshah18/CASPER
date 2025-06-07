import os
import tempfile
from gtts import gTTS
from RealtimeSTT import AudioToTextRecorder
from ollama import chat, ChatResponse
import warnings

def speak_text(text):
    try:
        tts = gTTS(text=text, lang='en',tld='ca')
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            temp_path = fp.name
            tts.save(temp_path)

        os.system(f'afplay "{temp_path}"')  
        os.remove(temp_path)
    except Exception as e:
        print(f"TTS error: {e}")

def process_text(text):
    print(f"Transcribed Text: {text}")
    response: ChatResponse = chat(model='llama3.2', messages=[
        {'role': 'user', 'content': text},
    ])
    reply = response.message.content
    print(f"Ollama Response: {reply}")

    speak_text(reply)  # This will block until speech ends

if __name__ == '__main__':
    # Suppress urllib3 LibreSSL warning
    warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")
    print("Initializing recorder. Speak now...")
    recorder = AudioToTextRecorder()
    while True:
        recorder.text(process_text)
