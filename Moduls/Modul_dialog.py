import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
import time
from datetime import datetime, timedelta
import pygame
import os

reminders = []

def set_reminder():
    message = reminder_message_entry.get()
    reminder_time = reminder_time_entry.get()

    # Проверяем, ввели ли сообщение и время
    if not message or not reminder_time:
        messagebox.showwarning("Пустое поле", "Пожалуйста, заполните оба поля.")
        return

    try:
        reminder_time = datetime.strptime(reminder_time, '%H:%M')
        now = datetime.now()
        reminder_time = reminder_time.replace(year=now.year, month=now.month, day=now.day)

        if reminder_time < now:
            reminder_time += timedelta(days=1)  # Если время прошло

        reminders.append((reminder_time, message))
        update_reminder_area()
        messagebox.showinfo("Успех!", f"Напоминание установлено на {reminder_time.strftime('%H:%M')}!")
        reminder_message_entry.delete(0, tk.END)  # Очищаем поле
        reminder_time_entry.delete(0, tk.END)  # Очищаем поле времени

    except ValueError:
        messagebox.showerror("Ошибка!", "Пожалуйста, введите время в формате HH:MM.")

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('hi.wav')  # Убедись, что у тебя есть файл звука
    pygame.mixer.music.play()

def check_reminders():
    while True:
        now = datetime.now()
        for reminder in reminders:
            if reminder[0] <= now:
                play_sound()
                show_custom_reminder(reminder[1])
                reminders.remove(reminder)
                update_reminder_area()
        time.sleep(10)

def update_reminder_area():
    reminder_area.config(state=tk.NORMAL)
    reminder_area.delete(1.0, tk.END)
    for i, reminder in enumerate(reminders):
        reminder_area.insert(tk.END, f"{i}: {reminder[0].strftime('%Y-%m-%d %H:%M')} - {reminder[1]}\n")
    reminder_area.config(state=tk.DISABLED)

def delete_reminder():
    index = simpledialog.askinteger("Удалить напоминание", "Введите номер напоминания:\n(например, 0 для первого)", maxvalue=len(reminders) - 1)
    if index is not None and 0 <= index < len(reminders):
        reminders.pop(index)
        update_reminder_area()
        messagebox.showinfo("Удаление", "Напоминание удалено.")
    else:
        messagebox.showerror("Ошибка", "Неверный номер напоминания.")

def show_custom_reminder(message):
    reminder_window = tk.Toplevel()
    reminder_window.title("Напоминание!")
    reminder_window.geometry("500x500")

    label = tk.Label(reminder_window, text=message, font=("Times New Roman", 25))
    label.pack(pady=20)

    close_button = tk.Button(reminder_window, text="Закрыть", command=reminder_window.destroy)
    close_button.pack(pady=10)

    reminder_window.attributes("-topmost", True)
    reminder_window.mainloop()

# Основное окно
root = tk.Tk()
root.title("Напоминалки")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

header = tk.Label(root, text="Установи свое напоминание!", font=("Helvetica", 18), bg="#f0f0f0", fg="#4CAF50")
header.pack(pady=10)

reminder_message_entry = tk.Entry(root, font=("Helvetica", 14), width=40, bg="#e3e3e3")
reminder_message_entry.pack(pady=5)

# Поле для ввода времени напоминания
reminder_time_entry = tk.Entry(root, font=("Helvetica", 14), width=10, bg="#e3e3e3")
reminder_time_entry.pack(pady=5)  # Исправлено здесь
reminder_time_entry.insert(0, "0Ч:0M")

# Создание кнопок для установки и удаления напоминания
set_button = tk.Button(root, text="Установить напоминание", command=set_reminder, bg="#4CAF50", fg="white",
                       font=("Helvetica", 14))
set_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить напоминание", command=delete_reminder, bg="#F44336", fg="white",
                          font=("Helvetica", 14))
delete_button.pack(pady=5)

# Поле для отображения установленных напоминаний
reminder_area = tk.Text(root, font=("Helvetica", 12), width=50, height=10, bg="#e3e3e3", state=tk.DISABLED)
reminder_area.pack(pady=10)

# Запускаем поток для проверки напоминаний
threading.Thread(target=check_reminders, daemon=True).start()

root.mainloop()


if __name__ == "__main__":
    pygame.init()
    root.mainloop()
