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

        self.early_withdrawal_var = tk.IntVar(value=0)  # За замовчуванням - 0 (немає раннього виведення)

        tk.Label(self, text="Дострокове зняття дозволене?", font=('Bitstream Charter', 10)).pack(pady=10)
        tk.Radiobutton(self, text="Так", variable=self.early_withdrawal_var, value=1,
                       command=self.toggle_early_withdrawal).pack()
        tk.Radiobutton(self, text="Ні", variable=self.early_withdrawal_var, value=0,
                       command=self.toggle_early_withdrawal).pack()

        # Відсоткова ставка для 3-6 місяців
        tk.Label(self, text='Введіть відсоткову ставку по депозиту від 3 до 6 місяців',
                 font=('Bitstream Charter', 10)).pack(pady=10)
        self.interest_3_6 = tk.Entry(self)
        self.interest_3_6.pack()

        # Відсоткова ставка для 3-6 місяців, якщо є ранній вивід
        self.interest_3_6_early_label = tk.Label(self,
                                                 text='Введіть відсоткову ставку по депозиту від 3 до 6 місяців, якщо є ранній вивід',
                                                 font=('Bitstream Charter', 10))
        self.interest_3_6_early = tk.Entry(self)

        # Спочатку вони будуть приховані
        self.interest_3_6_early_label.pack_forget()
        self.interest_3_6_early.pack_forget()

        # Відсоткова ставка для 6-9 місяців
        tk.Label(self, text='Введіть відсоткову ставку по депозиту від 6 до 9 місяців',
                 font=('Bitstream Charter', 10)).pack(pady=10)
        self.interest_6_9 = tk.Entry(self)
        self.interest_6_9.pack()

        # Відсоткова ставка для 6-9 місяців, якщо є ранній вивід
        self.interest_6_9_early_label = tk.Label(self,
                                                 text='Введіть відсоткову ставку по депозиту від 6 до 9 місяців, якщо є ранній вивід',
                                                 font=('Bitstream Charter', 10))
        self.interest_6_9_early = tk.Entry(self)

        # Спочатку вони будуть приховані
        self.interest_6_9_early_label.pack_forget()
        self.interest_6_9_early.pack_forget()

        # Відсоткова ставка для 9-12 місяців
        tk.Label(self, text='Введіть відсоткову ставку по депозиту від 9 до 12 місяців',
                 font=('Bitstream Charter', 10)).pack(pady=10)
        self.interest_9_12 = tk.Entry(self)
        self.interest_9_12.pack()

        # Відсоткова ставка для 9-12 місяців, якщо є ранній вивід
        self.interest_9_12_early_label = tk.Label(self,
                                                  text='Введіть відсоткову ставку по депозиту від 9 до 12 місяців, якщо є ранній вивід',
                                                  font=('Bitstream Charter', 10))
        self.interest_9_12_early = tk.Entry(self)

        # Спочатку вони будуть приховані
        self.interest_9_12_early_label.pack_forget()
        self.interest_9_12_early.pack_forget()

        # Відсоткова ставка для 18 місяців
        tk.Label(self, text='Введіть відсоткову ставку по депозиту на 18 місяців', font=('Bitstream Charter', 10)).pack(
            pady=10)
        self.interest_18 = tk.Entry(self)
        self.interest_18.pack()

        # Відсоткова ставка для 18 місяців, якщо є ранній вивід
        self.interest_18_early_label = tk.Label(self,
                                                text='Введіть відсоткову ставку по депозиту на 18 місяців, якщо є ранній вивід',
                                                font=('Bitstream Charter', 10))
        self.interest_18_early = tk.Entry(self)

        # Спочатку вони будуть приховані
        self.interest_18_early_label.pack_forget()
        self.interest_18_early.pack_forget()

        # Відсоткова ставка для 24 місяців
        tk.Label(self, text='Введіть відсоткову ставку по депозиту на 24 місяці', font=('Bitstream Charter', 10)).pack(
            pady=10)
        self.interest_24 = tk.Entry(self)
        self.interest_24.pack()

        # Відсоткова ставка для 24 місяців, якщо є ранній вивід
        self.interest_24_early_label = tk.Label(self,
                                                text='Введіть відсоткову ставку по депозиту на 24 місяці, якщо є ранній вивід',
                                                font=('Bitstream Charter', 10))
        self.interest_24_early = tk.Entry(self)

        # Спочатку вони будуть приховані
        self.interest_24_early_label.pack_forget()
        self.interest_24_early.pack_forget()

        tk.Button(self, text='Submit', command=self.commit_deposit, bg='green', fg='white').pack(pady=10)

    def toggle_early_withdrawal(self):
        """Метод для приховання чи показу полів для раннього виведення в залежності від вибору користувача"""
        if self.early_withdrawal_var.get() == 1:
            # Якщо вибрано, що ранній вивід дозволений, показуємо додаткові поля для кожного періоду
            self.interest_3_6_early_label.pack(pady=10)
            self.interest_3_6_early.pack(pady=10)
            self.interest_6_9_early_label.pack(pady=10)
            self.interest_6_9_early.pack(pady=10)
            self.interest_9_12_early_label.pack(pady=10)
            self.interest_9_12_early.pack(pady=10)
            self.interest_18_early_label.pack(pady=10)
            self.interest_18_early.pack(pady=10)
            self.interest_24_early_label.pack(pady=10)
            self.interest_24_early.pack(pady=10)
        else:
            # Якщо вибрано, що ранній вивід не дозволений, ховаємо ці поля
            self.interest_3_6_early_label.pack_forget()
            self.interest_3_6_early.pack_forget()
            self.interest_6_9_early_label.pack_forget()
            self.interest_6_9_early.pack_forget()
            self.interest_9_12_early_label.pack_forget()
            self.interest_9_12_early.pack_forget()
            self.interest_18_early_label.pack_forget()
            self.interest_18_early.pack_forget()
            self.interest_24_early_label.pack_forget()
            self.interest_24_early.pack_forget()


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
            # Отримуємо значення відсоткових ставок для раннього виведення (якщо є)
            interest_3_6_early = self.interest_3_6_early.get() if self.early_withdrawal_var.get() == 1 else None
            interest_6_9_early = self.interest_6_9_early.get() if self.early_withdrawal_var.get() == 1 else None
            interest_9_12_early = self.interest_9_12_early.get() if self.early_withdrawal_var.get() == 1 else None
            interest_18_early = self.interest_18_early.get() if self.early_withdrawal_var.get() == 1 else None
            interest_24_early = self.interest_24_early.get() if self.early_withdrawal_var.get() == 1 else None

            # Додаємо депозит до бази даних через функцію з database.py
            database.add_deposit(name, bank_name, interest_3_6, interest_6_9, interest_9_12, interest_18, interest_24,
                                 self.early_withdrawal_var.get(), interest_3_6_early, interest_6_9_early,
                                 interest_9_12_early, interest_18_early, interest_24_early)

            # Повідомляємо про успіх
            messagebox.showinfo("Успіх", "Депозит успішно додано!")
        else:
            messagebox.showerror("Помилка", "Будь ласка, заповніть всі поля.")

