import tkinter as tk
import threading
import time

reminders = []


def start_recognition():
    threading.Thread().start()


def chat_response(user_input):
    responses = {
        "привет": "Привет! Как я могу помочь?",
        "как дела?": "У меня всё отлично, а у тебя?",
        "пока": "До свидания! Береги себя!",
    }

    response = responses.get(user_input.lower(), "Извини, я не понимаю.")
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
        for reminder in reminders:
            reminder_time, message = reminder
            if current_time >= reminder_time:
                reminder_area.config(state=tk.NORMAL)
                reminder_area.insert(tk.END, f"Напоминание: {message}\n")
                reminder_area.config(state=tk.DISABLED)
                reminders.remove(reminder)


# Создаем главное окно
root = tk.Tk()
root.title("Голосовой помощник")
root.geometry("500x400")

# Заголовок
label = tk.Label(root, text="Добро пожаловать в голосовой помощник!", font=("Arial", 14))
label.pack(pady=10)

# Область для отображения чата
chat_area = tk.Text(root, state=tk.DISABLED, height=10, width=60)
chat_area.pack(pady=10)
chat_area.tag_config('user', foreground='blue')
chat_area.tag_config('bot', foreground='green')

# Поле ввода для сообщений
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Кнопка для отправки сообщения
send_button = tk.Button(root, text="Отправить", command=send_message)
send_button.pack(pady=10)

# Напоминание
reminder_label = tk.Label(root, text="Введите время в секундах:")
reminder_label.pack(pady=5)

reminder_time_entry = tk.Entry(root, width=10)
reminder_time_entry.pack(pady=5)

reminder_message_label = tk.Label(root, text="Введите сообщение напоминания:")
reminder_message_label.pack(pady=5)

reminder_message_entry = tk.Entry(root, width=40)
reminder_message_entry.pack(pady=5)

set_reminder_button = tk.Button(root, text="Установить напоминание", command=set_reminder)
set_reminder_button.pack(pady=10)

# Область для напоминаний
reminder_area = tk.Text(root, state=tk.DISABLED, height=5, width=60)
reminder_area.pack(pady=10)

# Запускаем поток для проверки напоминаний
threading.Thread(target=check_reminders, daemon=True).start()

# Запускаем главный цикл
root.mainloop()