import json
import sys
import queue
import tempfile
from datetime import datetime
import sounddevice as sd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import vosk

import words


from gtts import gTTS
from skills import *

# Инициализация очереди
sample_queue = queue.Queue()

# Инициализация голосовой модели
model = vosk.Model('model-small')
new_file, filename = tempfile.mkstemp()

device = sd.default.device
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])

print("\x1b[32m", 'Готов к работе')


def audio_callback(indata, frames, time, status):
    """Добавляет в очередь семплы из потока."""
    sample_queue.put(bytes(indata))


def open_gui():
    """Запускает GUI."""
    retcode = subprocess.call([sys.executable, "GUI.py"])
    if retcode != 0:
        sys.exit(126)


def play_time_based_sound():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    if current_time > "00:00:00" and current_time < "12:00:00":
        playsound(os.path.join("Voice", "Activ", "Time_3-12.wav"))
    if current_time > "12:00:00" and current_time < "18:00:00":
        playsound(os.path.join("Voice", "Activ", "audio_time_12-6.wav"))
    if current_time >= "18:00:00" and current_time < "24:00:00":
        playsound(os.path.join("Voice", "Activ", "audio_time_6-3.wav"))


open_gui()
play_time_based_sound()

def speak(text):
    tts = gTTS(text=text, lang='ru')
    filename = "response.mp3"
    tts.save(filename)
    os.system("start " + filename)  # Windows

def recognize(data, vectorizer, clf):
    TRIGGERS = {'джарвис', 'спать', 'джервис'}

    trg = TRIGGERS.intersection(data.split())
    if not trg:
        return

    data = data.replace(list(trg)[0], '')

    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    # Вместо voice.speaker
   # speak(answer.replace(func_name, ''))

    MyGlobals.task = data[15:]
    MyGlobals.outFraze = data

    func_name = answer.split()[0]
    exec(func_name + '()')



def main():
    """Основная функция для обучения и прослушивания."""
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set

    # Постоянная прослушка микрофона
    with sd.RawInputStream(samplerate=samplerate, blocksize=48000, device=device[0], dtype='int16', channels=1,
                           callback=audio_callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = sample_queue.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)
            else:
                print("\x1b[0m", rec.PartialResult())


if __name__ == '__main__':
    main()
