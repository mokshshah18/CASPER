from RealtimeSTT import AudioToTextRecorder
from ollama import chat, ChatResponse
import os
import warnings
import threading

done = threading.Event()

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
    done.set()  # Signal that this run is done

if __name__ == '__main__':
    warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")
    try:
        recorder = AudioToTextRecorder()
    except Exception as e:
        print(f"Error initializing recorder: {e}")
        exit(1)

    while True:
        done.clear()  # Reset signal
        try:
            recorder.text(process_text)
            done.wait()  # Wait until `process_text()` finishes
        except Exception as e:
            print(f"Recording error: {e}")
