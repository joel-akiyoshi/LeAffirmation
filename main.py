import src.microphone as microphone
import src.vosk_interface as vosk_interface
import src.sentiment as sentiment

import random

audio, stream = microphone.init_microphone()
recognizer = vosk_interface.init_recognizer()

try:
    print("Listening for speech...")

    while True:
        audio_data = microphone.read_audio_chunk(stream)

        result = vosk_interface.transcribe_audio(recognizer, audio_data)

        if result and random.randint(1, 2) == 1:
            folder = sentiment.get_sentiment_folder(result)
            print(f"result is '{result}', folder is {folder}")
            

except KeyboardInterrupt:
    print("Stopping...")

finally:
    microphone.close_microphone(audio, stream)
