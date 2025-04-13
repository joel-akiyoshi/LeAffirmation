import src.microphone as microphone
import src.vosk_interface as vosk_interface
import src.sentiment as sentiment
import src.dfplayer as dfplayer
import random
import time

FOREVER_TRACK = 29
NUM_TRACKS = 32

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

            if folder == 4:  # play a meme
                dfplayer.play_track(random.randint(25, 32))

            elif folder == 5:  # handle forever case
                dfplayer.play_track(FOREVER_TRACK)

            elif folder == 6:  # handle play all case
                for track in range(NUM_TRACKS):
                    dfplayer.play_track(track)
                    time.sleep(5)

            else: 
                track = random.randint(1, NUM_TRACKS // 4) + (folder - 1) * 5
                dfplayer.play_track(track)

            time.sleep(5)
            

except KeyboardInterrupt:
    print("Stopping...")

finally:
    microphone.close_microphone(audio, stream)
