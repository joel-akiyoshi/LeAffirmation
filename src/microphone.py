# microphone.py

import pyaudio
import numpy as np

def init_microphone(rate=16000, chunk_size=1024, channels=1):
    """Init mic and return Audio, and audio Stream"""
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk_size)
    return p, stream


def read_audio_chunk(stream):
    """Read a chunk of audio from the stream."""
    audio_data = stream.read(1024)
    return audio_data


def close_microphone(p, stream):
    """Close the audio stream and cleanup."""
    stream.stop_stream()
    stream.close()
    p.terminate()
