import os
import webbrowser
import sys


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
	sys.exit()





