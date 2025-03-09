import tkinter as tk
from tkinter import messagebox

import database


class AddWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Додати депозит')

        tk.Label(self, text='Додати депозит', font=('Bitstream Charter', 16)).pack(pady=10)

        # Назва депозиту
        tk.Label(self, text='Вкажіть назву депозиту', font=('Bitstream Charter', 10)).pack(pady=10)
        self.name = tk.Entry(self)
        self.name.pack()

        # Назва банку депозиту
        tk.Label(self, text='Введіть назву банка', font=('Bitstream Charter', 10)).pack(pady=10)
        self.bank_name = tk.Entry(self)
        self.bank_name.pack()

        # Відсоткова ставка для 3-6 місяців
        tk.Label(self, text='Введіть відсоткову ставку по депозиту від 3 до 6 місяців',
                 font=('Bitstream Charter', 10)).pack(pady=10)
        self.interest_3_6 = tk.Entry(self)
        self.interest_3_6.pack()

        # Відсоткова ставка для 6-9 місяців
        tk.Label(self, text='Введіть відсоткову ставку по депозиту від 6 до 9 місяців',
                 font=('Bitstream Charter', 10)).pack(pady=10)
        self.interest_6_9 = tk.Entry(self)
        self.interest_6_9.pack()

        # Відсоткова ставка для 9-12 місяців
        tk.Label(self, text='Введіть відсоткову ставку по депозиту від 9 до 12 місяців',
                 font=('Bitstream Charter', 10)).pack(pady=10)
        self.interest_9_12 = tk.Entry(self)
        self.interest_9_12.pack()

        # Відсоткова ставка для 18 місяців
        tk.Label(self, text='Введіть відсоткову ставку по депозиту на 18 місяців', font=('Bitstream Charter', 10)).pack(
            pady=10)
        self.interest_18 = tk.Entry(self)
        self.interest_18.pack()

        # Відсоткова ставка для 24 місяців
        tk.Label(self, text='Введіть відсоткову ставку по депозиту на 24 місяці', font=('Bitstream Charter', 10)).pack(
            pady=10)
        self.interest_24 = tk.Entry(self)
        self.interest_24.pack()

        tk.Button(self, text='Submit', command=self.commit_deposit, bg='green', fg='white').pack(pady=10)


    def commit_deposit(self):
        """Комітить депозит у базу даних після перевірки полів"""
        name = self.name.get()
        bank_name = self.bank_name.get()
        interest_3_6 = self.interest_3_6.get()
        interest_6_9 = self.interest_6_9.get()
        interest_9_12 = self.interest_9_12.get()
        interest_18 = self.interest_18.get()
        interest_24 = self.interest_24.get()

        # Перевірка, чи всі обов'язкові поля заповнені
        if name and bank_name and interest_3_6 and interest_6_9 and interest_9_12 and interest_18 and interest_24:
            database.add_deposit(name, bank_name, interest_3_6, interest_6_9, interest_9_12, interest_18, interest_24)
            messagebox.showinfo("Успіх", "Депозит успішно додано!")
        else:
            messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля.")

