
import vosk
import json

MODEL_PATH = "models/vosk-model-small-en-us-0.15"
SAMPLE_RATE = 48000

def init_recognizer(model_path = MODEL_PATH, sample_rate=SAMPLE_RATE):
    """Initialize and return the Vosk model and recognizer."""
    model = vosk.Model(model_path)
    recognizer=vosk.KaldiRecognizer(model, sample_rate)
    return recognizer


def transcribe_audio(recognizer, audio_data):
    """Feed audio data to the recognizer and return the transcribed text if a full sentence is ready."""
    if recognizer.AcceptWaveform(audio_data):
        result = json.loads(recognizer.Result())
        return result.get("text", "")

    else:
        return None
