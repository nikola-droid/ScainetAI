import os
import subprocess
import webbrowser
from playsound3 import playsound
import tkinter as tk
import random
import threading


try:
	import requests		#pip install requests
except:
	pass


class MyGlobals(object):
	task = ' '


def browser():
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)
	word_input = MyGlobals.task
	word_output = "https://yandex.ru/search/?text=" + word_input
	webbrowser.open(word_output, new=2)

def browser_1():
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)
	word_output = "https://ya.ru/"
	webbrowser.open(word_output, new=2)

def game():
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)
	os.system('start python %USERPROFILE%\\Documents\\GitHub\\ScainetAI\\comands\\love.py')

def offpc():
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)
	os.system('shutdown /s /t 10 ')

def passive():
	'''Функция заглушка при простом диалоге с ботом'''
	pass

def passive_1():
	'''Функция заглушка при простом диалоге с ботом'''

	pass

def restart():
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)

def offBot():
	data = [
		"Voice\lis\Fixed.wav",
		#"Voice\lis\lisn_you.wav",
		#"Voice\lis\pristupay.wav",
		#"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)
	os.system('start %USERPROFILE%\\Documents\\GitHub\\ScainetAI\\comands\\exit.exe')
	exit()


def telegram():
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)
	cmd = 'start %USERPROFILE%\AppData\Roaming\Telegram_Desktop\Telegram.exe'
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE)

def wife():
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)
	os.system('start python %USERPROFILE%\\Documents\\GitHub\\ScainetAI\\comands\\love.py')

def hi():
	playsound("Voice\Activ\Time_3-12.wav")



def lisn():
	pass
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r=random.choice(data)
	playsound(r)

def times():
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)

def mem():
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)

def music():
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)
	os.system('start %USERPROFILE%\AppData\Local\Programs\YandexMusic\Яндекс_Музыка.exe')

def openexe():
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)

def weather():
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)
	word_output_w = "https://yandex.ru/pogoda/moscow?ysclid=lyo5fqv42n298075757&lat=55.755863&lon=37.6177"
	webbrowser.open(word_output_w, new=2)

def cool():
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)

def install_pip():
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)
	os.system('python %USERPROFILE%\\Documents\\GitHub\\ScainetAI\\istall_pip.py')
	print("\x1b[32m","Compleat")

#Moduls

# Инициализация основного окна
root = tk.Tk()

# Переменная для хранения состояния чекбокса
var = tk.BooleanVar()


def check_status():
	# Проверяем состояние чекбокса и выводим его в консоль
	print(f"Чекбокс выбран: {var.get()}")


def blocking():
	# Возвращаем состояние чекбокса для использования в других функциях
	return var.get()


def dialog():
	print(f"Состояние blocking: {blocking()}")  # Это для отладки, чтобы увидеть текущее значение

	if not blocking():  # Или if blocking() == False:
		print("Модуль не выбран")
	else:
		print("Модуль активирован")

		# Здесь укажи свои звуковые файлы
		data = [
			"Voice/lis/Fixed.wav",
			"Voice/lis/lisn_you.wav",
			"Voice/lis/pristupay.wav",
			"Voice/lis/Vipolnay.wav",
		]

		r = random.choice(data)  # Выбираем случайный файл из списка
		playsound(r)  # Проигрываем выбранный звук

		# Импортируем модуль, если это необходимо
		from Moduls.Modul_dialog import Modul_dialog # Убедись, что это корректный путь

		# Запускаем новый поток для работы с диалогом
		thread = threading.Thread(target=Modul_dialog, args=("Первый поток",))
		thread.start()


# Создаем Checkbutton
checkbox = tk.Checkbutton(root, text="Dialog", variable=var, command=check_status)
checkbox.pack()

# Добавим кнопку для запуска диалога
start_button = tk.Button(root, text="Запустить диалог", command=dialog)
start_button.pack()

# Запуск основного цикла приложения
root.mainloop()
