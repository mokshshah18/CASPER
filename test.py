from RealtimeTTS import TextToAudioStream, SystemEngine
import logging


logging.basicConfig(level=logging.DEBUG)    
engine = SystemEngine()  # Ensure proper initialization of your TTS engine
stream = TextToAudioStream(engine)
stream.feed("Hello world! How are you today?")
stream.play(log_synthesized_text=True)
stream.play_async()