import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

import database as db

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class RemoveWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Видалити депозит')

        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text='Видалити депозит', font=('Arial', 18, 'bold')).pack(pady=10)

        labels = {
            'Введіть назву депозиту': ctk.CTkEntry(frame),
            'Введіть назву банку': ctk.CTkEntry(frame)
        }

        self.entries = labels

        for text, entry in labels.items():
            ctk.CTkLabel(frame, text=text, font=('Arial', 12)).pack(pady=5)
            entry.pack(pady=5)

        ctk.CTkButton(frame, text='Видалити', command=self.commit, bg_color='#E53E3E', fg_color='#E53E3E', hover_color='#C53030', text_color='white').pack(pady=10)

    def commit(self):
        name = self.entries["Введіть назву депозиту"].get()
        bank_name = self.entries["Введіть назву банку"].get()

        if not name or not bank_name:
            CTkMessagebox(title='Помилка!', message='Введіть назву депозиту та банку', icon="cancel")
            return

        deleted_rows = db.remove_deposite(name, bank_name)

        if deleted_rows >= 1:
            CTkMessagebox(title='Успіх!', message=f'Успішно видалено {deleted_rows} депозитів', icon="check")
        else:
            CTkMessagebox(title='Помилка!', message='Видалення не виконалось', icon="cancel")