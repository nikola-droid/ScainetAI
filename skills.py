import os
import subprocess
import wave
import webbrowser
import simpleaudio as sa
import random
import time
from playsound3 import playsound



try:
	import requests		#pip install requests
except:
	pass


class MyGlobals(object):
	task = ' '
	outFraze = ' '

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
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)
	#os.system('start %USERPROFILE%\\Documents\\GitHub\\ScainetAI\\comands\\exit.exe')
	quit()


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

def dialog():
	data = [
		"Voice\lis\Fixed.wav",
		"Voice\lis\lisn_you.wav",
		"Voice\lis\pristupay.wav",
		"Voice\lis\Vipolnay.wav",
	]
	r = random.choice(data)
	playsound(r)

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
