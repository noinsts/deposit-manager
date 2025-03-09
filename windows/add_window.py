import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

import database

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class AddWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Додати депозит')

        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text='Додати депозит', font=('Arial', 18, 'bold')).pack(pady=10)

        labels = {
            'Вкажіть назву депозиту': ctk.CTkEntry(frame),
            'Введіть назву банка': ctk.CTkEntry(frame),
            'Введіть відсоткову ставку по депозиту від 3 до 6 місяців': ctk.CTkEntry(frame),
            'Введіть відсоткову ставку по депозиту від 6 до 9 місяців': ctk.CTkEntry(frame),
            'Введіть відсоткову ставку по депозиту від 9 до 12 місяців': ctk.CTkEntry(frame),
            'Введіть відсоткову ставку по депозиту на 18 місяців': ctk.CTkEntry(frame),
            'Введіть відсоткову ставку по депозиту на 24 місяці': ctk.CTkEntry(frame),
        }
        self.entries = labels

        for text, entry in labels.items():
            ctk.CTkLabel(frame, text=text, font=('Arial', 12)).pack(pady=5)
            entry.pack(pady=5)

        ctk.CTkButton(frame, text='Зберегти', command=self.commit_deposit, bg_color='#4A5568', fg_color='#4A5568', hover_color='#2D3748', text_color='white').pack(pady=10)

    def commit_deposit(self):
        """Комітить депозит у базу даних після перевірки полів"""
        name = self.entries['Вкажіть назву депозиту'].get()
        bank_name = self.entries['Введіть назву банка'].get()
        interest_3_6 = self.entries['Введіть відсоткову ставку по депозиту від 3 до 6 місяців'].get()
        interest_6_9 = self.entries['Введіть відсоткову ставку по депозиту від 6 до 9 місяців'].get()
        interest_9_12 = self.entries['Введіть відсоткову ставку по депозиту від 9 до 12 місяців'].get()
        interest_18 = self.entries['Введіть відсоткову ставку по депозиту на 18 місяців'].get()
        interest_24 = self.entries['Введіть відсоткову ставку по депозиту на 24 місяці'].get()

        # Перевірка, чи всі обов'язкові поля заповнені
        if name and bank_name and interest_3_6 and interest_6_9 and interest_9_12 and interest_18 and interest_24:
            database.add_deposit(name, bank_name, interest_3_6, interest_6_9, interest_9_12, interest_18, interest_24)
            CTkMessagebox(title="Успіх", message="Депозит успішно додано!", icon="check")
        else:
            CTkMessagebox(title="Помилка", message="Будь ласка, заповніть всі поля.", icon="cancel")