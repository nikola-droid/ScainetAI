
import vosk
import pyaudio
import json
from vosk import Model, KaldiRecognizer

model = Model('./vosk-model-ru-0.10')
rec = KaldiRecognizer(model, 16000)
p=pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=16000)
stream.start_stream()

print('Ожидаю запроса')
def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data)>0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']

for text in listen():
    if text == "пока":
        quit()
    elif text =="привет":
        print('Слушаю')


