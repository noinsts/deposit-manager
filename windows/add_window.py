import tkinter as tk
from tkinter import messagebox

import database


class AddWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Додати депозит')

        tk.Label(self, text='Додати депозит', font=('Bitstream Charter', 16)).pack(pady=10)

        labels = {
            'Вкажіть назву депозиту': tk.Entry(self),
            'Введіть назву банка': tk.Entry(self),
            'Введіть відсоткову ставку по депозиту від 3 до 6 місяців': tk.Entry(self),
            'Введіть відсоткову ставку по депозиту від 6 до 9 місяців': tk.Entry(self),
            'Введіть відсоткову ставку по депозиту від 9 до 12 місяців': tk.Entry(self),
            'Введіть відсоткову ставку по депозиту на 18 місяців': tk.Entry(self),
            'Введіть відсоткову ставку по депозиту на 24 місяці': tk.Entry(self),
        }
        self.entries = labels

        for text, entry in labels.items():
            tk.Label(self, text=text, font=('Bitstream Charter', 10)).pack()
            entry.pack()

        tk.Button(self, text='Submit', command=self.commit_deposit, bg='green', fg='white').pack(pady=10)

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
            messagebox.showinfo("Успіх", "Депозит успішно додано!")
        else:
            messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля.")

