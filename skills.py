import os
import subprocess
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
	outFraze = ' '




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

def restart():
	data = [
		'Voice\lis\lisn.wav',
		'Voice\lis\out.wav',
		'Voice\lis\out_1.wav',
		'Voice\lis\out_2.wav',
		'Voice\lis\out_3.wav',
		'Voice\lis\out_4.wav',
		'Voice\lis\yes.wav',
	]
	r = random.choice(data)
	f_name = r
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()

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
	#os.system('start %USERPROFILE%\\Documents\\GitHub\\ScainetAI\\comands\\exit.exe')
	quit()


def telegram():
	data = [
		'Voice\lis\lisn.wav',
		'Voice\lis\out.wav',
		'Voice\lis\out_1.wav',
		'Voice\lis\out_2.wav',
		'Voice\lis\out_3.wav',
		'Voice\lis\out_4.wav',
		'Voice\lis\yes.wav',
	]
	r = random.choice(data)
	f_name = r
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()
	cmd = 'start %USERPROFILE%\AppData\Roaming\Telegram_Desktop\Telegram.exe'
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE)

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
	pass
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
	word_output_w = "https://yandex.ru/pogoda/moscow?ysclid=lyo5fqv42n298075757&lat=55.755863&lon=37.6177"
	webbrowser.open(word_output_w, new=2)


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

def install_pip():
	data = [
		'Voice\lis\yes.wav',
	]
	r = random.choice(data)
	f_name = r
	wave_obj = sa.WaveObject.from_wave_file(f_name)
	play = wave_obj.play()
	play.wait_done()
	play.stop()
	os.system('python %USERPROFILE%\\Documents\\GitHub\\ScainetAI\\istall_pip.py')
	print("\x1b[32m","Compleat")
