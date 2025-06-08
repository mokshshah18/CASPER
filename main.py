import os
import tempfile
from gtts import gTTS
from RealtimeSTT import AudioToTextRecorder
from ollama import chat, ChatResponse
import pyttsx3
import warnings

def speak_text(text):
    # tts = gTTS(text=text, lang='en',tld='ca')
    # with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
    #     temp_path = fp.name
    #     tts.save(temp_path)

    # os.system(f'afplay "{temp_path}"')  
    # os.remove(temp_path)
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        print("not working")
        
def process_text(text):
    print(f"Transcribed Text: {text}")
    response: ChatResponse = chat(model='llama3.2', messages=[
        {'role': 'user', 'content': text},
    ])
    reply = response.message.content
    print(f"Ollama Response: {reply}")
    speak_text(reply)  # This will block until speech ends

if __name__ == '__main__':
    warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")
    print("Initializing recorder. Speak now...")
    recorder = AudioToTextRecorder()
    engine = pyttsx3.init()
    while True:
        recorder.text(process_text)
