import src.microphone as microphone
import src.vosk_interface as vosk_interface
import src.sentiment as sentiment
import src.dfplayer as dfplayer
import random
import time


audio, stream = microphone.init_microphone()
recognizer = vosk_interface.init_recognizer()

try:
    print("Listening for speech...")

    while True:
        audio_data = microphone.read_audio_chunk(stream)

        result = vosk_interface.transcribe_audio(recognizer, audio_data)

        if result and len(result) > 20:
            print(f"You said {result}")
            folder = sentiment.get_sentiment_folder(result)
            print(f"folder is {folder}")
            track = random.randint(1, 5) + (folder - 1) * 5
            print(f"playing track {track}")
            dfplayer.play_track(track)
            time.sleep(5)
            



            

except KeyboardInterrupt:
    print("Stopping...")

finally:
    microphone.close_microphone(audio, stream)
