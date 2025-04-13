import src.microphone as microphone
import src.vosk_interface as vosk_interface

import pyaudio

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"{i}: {info['name']} (input channels: {info['maxInputChannels']})")
    print(f"  Default sample rate: {info['defaultSampleRate']}")
p.terminate()


audio, stream = microphone.init_microphone()
recognizer = vosk_interface.init_recognizer()

try:
    print("Listening for speech...")

    while True:
        audio_data = microphone.read_audio_chunk(stream)

        result = vosk_interface.transcribe_audio(recognizer, audio_data)

        if result:
            print("You said:", result)

except KeyboardInterrupt:
    print("Stopping...")

finally:
    microphone.close_microphone(audio, stream)
