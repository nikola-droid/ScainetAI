import pyttsx3
import voice

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)



def speaker(text):
	'''Озвучка текста'''
	engine.say(text)
	engine.runAndWait()

