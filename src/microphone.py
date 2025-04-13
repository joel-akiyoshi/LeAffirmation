# microphone.py

import pyaudio

def init_microphone(rate=48000, chunk_size=8192, channels=1):
    """Init mic and return Audio, and audio Stream"""
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk_size,
                    input_device_index=0)
    return p, stream


def read_audio_chunk(stream: pyaudio.Stream):
    """Read a chunk of audio from the stream."""
    try: 
        return stream.read(8192, exception_on_overflow=False)
    except IOError:
        print("Input overflowed, skipping the chunk")
        return b''
    


def close_microphone(p, stream):
    """Close the audio stream and cleanup."""
    stream.stop_stream()
    stream.close()
    p.terminate()
