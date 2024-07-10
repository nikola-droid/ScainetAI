import sys
import subprocess

def install():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install','vosk'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'sounddevice'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyttsx3'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'voice'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'simpleaudio'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'scikit-learn'])


