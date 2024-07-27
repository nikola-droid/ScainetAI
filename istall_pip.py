import sys
import subprocess

def install_requirements():
    # Устанавливаем библиотеки из requirements.txt
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'freeze', '>', 'requirements.txt'])


install_requirements()