from sklearn.feature_extraction.text import CountVectorizer  # pip install scikit-learn
from sklearn.linear_model import LogisticRegression
import sounddevice as sd  # pip install sounddevice
import vosk  # pip install vosk
import json
import queue
import voice
import words
import tempfile
from skills import *
import logging

logging.getLogger("vosk").setLevel(logging.WARNING)
key = input("Password  ")

while key!="1234":
    key = input("Password  ")

if key =="1234":
    print("\x1b[32m", "Good")
    print("\x1b[0m", "...Начало загрузки....")
    s = "█"
    for i in range(101):
        time.sleep(0.05)
        print('\r', 'Запуск', i * s, str(i), '%', end='')
    print("\x1b[32m", "\nЗагрузка завершена")


q = queue.Queue()





model = vosk.Model('model-small')  # голосовую модель vosk нужно поместить в папку с файлами проекта
new_file, filename = tempfile.mkstemp()

device = sd.default.device
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])  # получаем частоту микрофона


print("\x1b[32m",'Готов к работе')


def callback(indata, frames, time, status):
    '''
    Добавляет в очередь семплы из потока.
    вызывается каждый раз при наполнении blocksize
    в sd.RawInputStream'''

    q.put(bytes(indata))






hi()

from skills import *
def recognize(data, vectorizer, clf):

    TRIGGERS = {'скайнет', 'спать'}

    # проверяем есть ли имя бота в data, если нет, то return
    trg = TRIGGERS.intersection(data.split())
    if not trg:
        return

    # удаляем имя бота из текста
    data.replace(list(trg)[0], '')


    # получаем вектор полученного текста
    # сравниваем с вариантами, получая наиболее подходящий ответ
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    # получение имени функции из ответа из data_set
    func_name = answer.split()[0]

    voice.speaker(answer.replace(func_name, ''))

    MyGlobals.task = data[15:]

    # запуск функции из skills
    exec(func_name + '()')






def main():
    '''
    Обучаем матрицу ИИ
    и постоянно слушаем микрофон
    '''

    # Обучение матрицы на data_set модели
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))


    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set
    # постоянная прослушка микрофона
    with sd.RawInputStream(samplerate=samplerate, blocksize=56000, device=device[0], dtype='int16',
                           channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)
            else:
                print("\x1b[0m",rec.PartialResult())








if __name__ == '__main__':
    main()



