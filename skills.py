import os
import webbrowser
import sys
import wave
import simpleaudio as sa
import simpleaudio.functionchecks as fc


try:
	import requests		#pip install requests
except:
	pass

def browser():
	'''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

	webbrowser.open('https://www.youtube.com', new=2)


def game():
	'''Нужно разместить путь к exe файлу любого вашего приложения'''


def offpc():
	#Эта команда отключает ПК под управлением Windows

	#os.system('shutdown \s')
	print('пк был бы выключен, но команде # в коде мешает;)))')


def passive():
	'''Функция заглушка при простом диалоге с ботом'''
	pass

def offBot():
	os.system('start %USERPROFILE%\\Documents\\GitHub\\ScainetAI\\comands\\exit.exe')

def wife():
	os.system('start python %USERPROFILE%\\Documents\\GitHub\\ScainetAI\\comands\\love.py')

def hi():
	f_name = 'Voice\hi.wav'
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()




