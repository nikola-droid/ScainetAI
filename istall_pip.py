import sys, os
from contextlib import contextmanager
import subprocess

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout


with suppress_stdout():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'vosk'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'sounddevice'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyttsx3'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'voice'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'simpleaudio-patched'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'scikit-learn'])