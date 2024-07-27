import tkinter as tk
import threading
import time
import random

reminders = []

def chat_response(user_input):
    responses = {
        "привет": [
            "Привет, солнечный лучик! ☀ Как твои дела?",
            "Здравствуй! Что нового в твоей жизни?",
            "Хей, как настроение? ",
        ],
        "как дела?": [
            "У меня всё отлично, а ты как? ",
            "Живу и радуюсь! А у тебя как дела?",
            "Супер! Готова общаться! А как у тебя? ",
        ],
        "пока": [
            "До встречи! Надеюсь, скоро увидимся! ",
            "Пока-пока! Не забывай возвращаться! ",
            "Увидимся позже! Береги себя! ",
        ],
        "что делаешь?": [
            "Отвечаю на твои вопросы и радуюсь жизни! ",
            "Волнуюсь о мире и жду, когда ты напишешь! ",
            "Я всегда на связи для тебя! А что ты делаешь?",
        ],
        "расскажи анекдот": [
            "Почему компьютер не может танцевать? Потому что у него слишком много байтов! ",
            "Какой любимый напиток робота? Кофе с процессором! ",
            "Почему кошка сидит на компьютере? Она хочет быть мышкой! ",
        ],
    }

    # Получаем список ответов для пользовательского ввода и выбираем случайный
    response_list = responses.get(user_input.lower(), ["Извини, я не понимаю. "])
    response = random.choice(response_list)  # Выбираем случайный ответ
    return response

def send_message():
    user_input = entry.get()
    if user_input.strip():
        response = chat_response(user_input)
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"Вы: {user_input}\n", 'user')
        chat_area.insert(tk.END, f"Бот: {response}\n", 'bot')
        chat_area.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

def set_reminder():
    time_input = reminder_time_entry.get()
    message_input = reminder_message_entry.get()

    if time_input.strip() and message_input.strip():
        try:
            reminder_time = int(time_input)
            reminders.append((time.time() + reminder_time, message_input))
            reminder_area.config(state=tk.NORMAL)
            reminder_area.insert(tk.END,
                                 f"Напоминание установлено: через {reminder_time} секунд, сообщение: '{message_input}'\n")
            reminder_area.config(state=tk.DISABLED)
            reminder_time_entry.delete(0, tk.END)
            reminder_message_entry.delete(0, tk.END)
        except ValueError:
            reminder_area.config(state=tk.NORMAL)
            reminder_area.insert(tk.END, "Пожалуйста, введите корректное время в секундах.\n")
            reminder_area.config(state=tk.DISABLED)

def check_reminders():
    while True:
        time.sleep(1)  # Проверяем каждую секунду
        current_time = time.time()
        for reminder in reminders[:]:  # Проходим по копии списка
            reminder_time, message = reminder
            if current_time >= reminder_time:
                reminder_area.config(state=tk.NORMAL)
                reminder_area.insert(tk.END, f"Напоминание: {message}\n")
                reminder_area.config(state=tk.DISABLED)
                reminders.remove(reminder)

# Создаем главное окно
root = tk.Tk()
root.title("Голосовой помощник")
root.geometry("500x500")

# Заголовок
label = tk.Label(root, text="Добро пожаловать в голосовой помощник!", font=("Arial", 14))
label.pack(pady=10)

# Область для отображения чата
chat_area = tk.Text(root, state=tk.DISABLED, height=10, width=60)
chat_area.pack(pady=10)
chat_area.tag_config('user', foreground='blue')
chat_area.tag_config('bot', foreground='green')

def enter_pressed(event):
    send_message()

# Поле ввода для сообщений
entry = tk.Entry(root, width=40)
entry.pack()
entry.bind('<Return>', enter_pressed)

# Кнопка отправки сообщения
send_button = tk.Button(root, text="Отправить", command=send_message)
send_button.pack(pady=5)

# Заголовок для напоминаний
reminder_label = tk.Label(root, text="Установить напоминание (в секундах):", font=("Arial", 12))
reminder_label.pack(pady=10)

# Поле ввода времени напоминания
reminder_time_entry = tk.Entry(root, width=10)
reminder_time_entry.pack(pady=5)

# Поле ввода текста напоминания
reminder_message_entry = tk.Entry(root, width=30)
reminder_message_entry.pack(pady=5)

# Кнопка для установки напоминания
set_reminder_button = tk.Button(root, text="Установить напоминание", command=set_reminder)
set_reminder_button.pack(pady=5)

# Область для отображения напоминаний
reminder_area = tk.Text(root, state=tk.DISABLED, height=10, width=60)
reminder_area.pack(pady=10)

# Запуск потока для проверки напоминаний
reminder_thread = threading.Thread(target=check_reminders, daemon=True)
reminder_thread.start()

# Запуск главного цикла программы
root.mainloop()

