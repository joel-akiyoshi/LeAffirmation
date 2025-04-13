import src.microphone as microphone
import src.vosk_interface as vosk_interface
import src.sentiment as sentiment


audio, stream = microphone.init_microphone()
recognizer = vosk_interface.init_recognizer()

try:
    print("Listening for speech...")

    while True:
        audio_data = microphone.read_audio_chunk(stream)

        result = vosk_interface.transcribe_audio(recognizer, audio_data)

        if result:
            print(f"You said {result}")
            print(f"Sorted into folder {sentiment.get_sentiment_folder(result)}")


            

except KeyboardInterrupt:
    print("Stopping...")

finally:
    microphone.close_microphone(audio, stream)
