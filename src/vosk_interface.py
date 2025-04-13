from vosk import Model, KaldiRecognizer

model=Model("models/vosk-model-small-en-us-0.15")
rec = KaldiRecognizer(model, 16000)
print("Vosk is working")