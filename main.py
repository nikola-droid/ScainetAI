import codecs
import wave

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
import time





q = queue.Queue()

model = vosk.Model('vosk-model-small')  # голосовую модель vosk нужно поместить в папку с файлами проекта
new_file, filename = tempfile.mkstemp()

device = sd.default.device
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])  # получаем частоту микрофона



def callback(indata, frames, time, status):
    '''
    Добавляет в очередь семплы из потока.
    вызывается каждый раз при наполнении blocksize
    в sd.RawInputStream'''

    q.put(bytes(indata))

print('Готов к работе')

hi()

def recognize(data, vectorizer, clf):

    TRIGGERS = {'скайнет'}

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
    text = ""
    # постоянная прослушка микрофона
    with sd.RawInputStream(samplerate=samplerate, blocksize=48000, device=device[0], dtype='int16',
                           channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data=q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)
                mylist = rec.Result()
                with open('data.json', 'w') as f:
                    json.dump(mylist, f)

            else:
                f=open(r'comands\text.txt','r+', encoding='utf-8')
                f.write(rec.PartialResult())
                print(rec.PartialResult())






def browser():
    word_input = open(r'comands\text.txt', 'r+', encoding='utf-8')
    word_input.readline()
    word_input.readline()
    word_input = word_input.readline()
    word_input = word_input[15:-1]
    for i in range(0, len(word_input)):
        if word_input[i] == " ":        word_input = word_input[0:i] + "+" + word_input[i + 1:len(word_input)]
    word_output = "https://yandex.ru/search/?text=" + word_input
    webbrowser.open(word_output, new=1)



if __name__ == '__main__':
    main()



