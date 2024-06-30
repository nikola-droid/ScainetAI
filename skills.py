import os
import webbrowser
import simpleaudio as sa
import random
import time



try:
	import requests		#pip install requests
except:
	pass


class MyGlobals(object):
	task = ' '



def browser():

	word_input = MyGlobals.task
	word_output = "https://yandex.ru/search/?text=" + word_input
	webbrowser.open(word_output, new=2)




def game():
	data = [
		'Voice\game\game.wav',
		'Voice\lis\yes.wav',
	]
	r = random.choice(data)
	f_name = r
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()
	os.system('start python %USERPROFILE%\\Documents\\GitHub\\ScainetAI\\comands\\love.py')

def offpc():
	data = [
		'Voice\offpc\stop.wav',
		'Voice\lis\yes.wav',
	]
	r = random.choice(data)
	f_name = r
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()

	os.system('shutdown /s /t 10 ')

def passive():
	'''Функция заглушка при простом диалоге с ботом'''
	pass

def passive_1():
	'''Функция заглушка при простом диалоге с ботом'''

	pass

def offBot():
	data = [
		'Voice\offbot\slip.wav',
		'Voice\lis\yes.wav',
	]
	r = random.choice(data)
	f_name = r
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()
	os.system('start %USERPROFILE%\\Documents\\GitHub\\ScainetAI\\comands\\exit.exe')

def wife():
	data = [
		'Voice\wife\wife.wav',
		'Voice\wife\wife_1.wav',
		'Voice\wife\wife_2.wav',
		'Voice\wife\wife_3.wav',
	]
	r = random.choice(data)
	f_name = r
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()
	os.system('start python %USERPROFILE%\\Documents\\GitHub\\ScainetAI\\comands\\love.py')

def hi():
	f_name = 'Voice\Activ\hi.wav'
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()

def dialog():
	data = [
		'Voice\dialog\dialog.wav',
		'Voice\dialog\dialog_1.wav',
		'Voice\dialog\dialog_2.wav',
	]
	r = random.choice(data)
	f_name = r
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()

def lisn():
	data = [
		 'Voice\lis\lisn.wav',
		'Voice\lis\out.wav',
		'Voice\lis\out_1.wav',
		'Voice\lis\out_2.wav',
		'Voice\lis\out_3.wav',
		'Voice\lis\out_4.wav',
		'Voice\lis\yes.wav',
	]
	r=random.choice(data)
	f_name = r
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()

def times():
	data = [
		'Voice\Time\Time.wav',
	]
	r = random.choice(data)
	f_name = r
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()

def mem():
	data = [
		'Voice\mem\lol.wav',
		'Voice\mem\lol_1.wav',
		'Voice\mem\lol_2.wav',
		'Voice\mem\mem.wav',
		'Voice\mem\mem_1.wav',
		'Voice\mem\mem_2.wav',
	]
	r = random.choice(data)
	f_name = r
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()

def music():
	data = [
		'Voice\lis\yes.wav',
		'Voice\music\music.wav',
	]
	r = random.choice(data)
	f_name = r
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()
	os.system('start %USERPROFILE%\AppData\Local\Programs\YandexMusic\Яндекс_Музыка.exe')



def openexe():
	data = [
		'Voice\openexe\open_1.wav',
		'Voice\lis\yes.wav',
	]
	r = random.choice(data)
	f_name = r
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()

def weather():
	data = [
		'Voice\weather\weather.wav',
		'Voice\lis\yes.wav',

	]
	r = random.choice(data)
	f_name = r
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()

def cool():
	data = [
		'Voice\cool\cool.wav',
		'Voice\lis\yes.wav',
	]
	r = random.choice(data)
	f_name = r
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()
