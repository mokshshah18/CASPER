from RealtimeSTT import AudioToTextRecorder
from ollama import chat, ChatResponse
import os
import warnings

def speak_text(text):
    try:
        os.system(f'say "{text}"')
    except Exception as e:
        print(f"Speech error: {e}")

def process_text(text):
    print(f"Transcribed Text: {text}")
    response: ChatResponse = chat(model='llama3.2', messages=[
        {'role': 'user', 'content': text},
    ])
    reply = response.message.content
    print(f"Ollama Response: {reply}")
    speak_text(reply)

if __name__ == '__main__':
    warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")
    print("Initializing recorder...")
    try:
        recorder = AudioToTextRecorder()
    except Exception as e:
        print(f"Error initializing recorder: {e}")
        exit(1)

    while True:
        try:
            recorder.text(process_text)
        except Exception as e:
            print(f"Recording error: {e}")
        #time.sleep(0.5)
