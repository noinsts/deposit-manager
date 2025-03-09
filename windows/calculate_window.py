import tkinter as tk
from tkinter import messagebox

import database as db


class CalculateWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Розрахувати депозит')

        tk.Label(self, text='Підбір депозитів', font=('Bitstream Charter', 14)).pack(pady=10)

        self.entries = {}
        labels = {
            "bank_name" : "Ваш банк",
            "term" : "Термін депозиту (к-сть місяців)",
            "money" : "Введіть суму"
        }

        for key, label_text in labels.items():
            tk.Label(self, text=label_text).pack()
            entry = tk.Entry(self)
            entry.pack()
            self.entries[key] = entry

        tk.Button(self, text='Розрахувати', command=self.calculate, bg='red', fg='white').pack(pady=10)


    def percent(self):
        bank_name = self.entries["bank_name"].get()
        term = int(self.entries["term"].get())

        if not bank_name:
            messagebox.showwarning(title='Помилка!', message='Введіть назву банку')
            return

        if not term:
            messagebox.showwarning(title='Помилка', message='Введіть термін')

        try:
            term = int(term)
        except ValueError:
            messagebox.showwarning(title='Помилка!', message='Термін має бути число')
            return

        if 3 <= term < 6:
            interest_column = "interest_3_6"
        elif 6 <= term < 9:
            interest_column = "interest_6_9"
        elif 9 <= term <= 12:
            interest_column = "interest_9_12"
        elif 13 <= term < 18:
            interest_column = "interest_18"
        elif 19 <= term < 24:
            interest_column = "interest_24"
        else:
            messagebox.showerror("Помилка", "Невірний термін депозиту")
            return

        results = db.percent(bank_name, interest_column)

        if results:
            deposit_data = []
            for result in results:
                interest_rate, deposit_name = result
                deposit_data.append({
                    "deposit_name": deposit_name,
                    "bank_name": bank_name,
                    "interest_rate": interest_rate
                })
            return deposit_data
        else:
            messagebox.showerror("Помилка", "Не вдалося знайти депозити з такими даними")
            return None


    def calculate(self):
        money = self.entries["money"].get()

        if not money:
            messagebox.showwarning(title='Помилка!', message='Введіть кількість грошей')
            return

        try:
            money = int(money)
        except ValueError:
            messagebox.showwarning(title='Помилка!', message='Введіть гроші числом')
            return

        deposits_data = self.percent()

        if deposits_data:
            message = ""
            for deposit_data in deposits_data:  # Ітеруємо по списку депозитів
                interest_rate = deposit_data["interest_rate"]
                deposit_name = deposit_data["deposit_name"]
                bank_name = deposit_data["bank_name"]
                profit = money / 100 * interest_rate

                message += (
                    f"Депозит: {deposit_name}\n"
                    f"Банк: {bank_name}\n"
                    f"Відсоткова ставка: {interest_rate}%\n"
                    f"Сума вкладу: {money} грн.\n"
                    f"Прибуток: {profit:.2f} грн.\n\n"
            )
            messagebox.showinfo(title='Знайдено депозит!', message=message)
        else:
            messagebox.showerror("Помилка", "Не вдалося розрахувати депозит")


