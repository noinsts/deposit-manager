import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

import database as db

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class CalculateWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Розрахувати депозит')

        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text='Підбір депозитів', font=('Arial', 18, 'bold')).pack(pady=10)

        self.entries = {}
        labels = {
            "bank_name": "Ваш банк",
            "term": "Термін депозиту (к-сть місяців)",
            "money": "Введіть суму"
        }

        for key, label_text in labels.items():
            ctk.CTkLabel(frame, text=label_text, font=('Arial', 12)).pack(pady=5)
            entry = ctk.CTkEntry(frame)
            entry.pack(pady=5)
            self.entries[key] = entry

        ctk.CTkButton(frame, text='Розрахувати', command=self.calculate, bg_color='#4A5568', fg_color='#4A5568', hover_color='#2D3748', text_color='white').pack(pady=10)

    def percent(self):
        bank_name = self.entries["bank_name"].get()
        term = self.entries["term"].get()

        if not bank_name:
            CTkMessagebox(title='Помилка!', message='Введіть назву банку', icon="warning")
            return None

        if not term:
            CTkMessagebox(title='Помилка', message='Введіть термін', icon="warning")
            return None

        try:
            term = int(term)
        except ValueError:
            CTkMessagebox(title='Помилка!', message='Термін має бути число', icon="warning")
            return None

        if 3 <= term < 6:
            interest_column = "interest_3_6"
        elif 6 <= term < 9:
            interest_column = "interest_6_9"
        elif 9 <= term <= 12:
            interest_column = "interest_9_12"
        elif 13 <= term <= 18:
            interest_column = "interest_18"
        elif 19 <= term <= 24:
            interest_column = "interest_24"
        else:
            CTkMessagebox(title="Помилка", message="Невірний термін депозиту", icon="cancel")
            return None

        try:
            results = db.percent(bank_name, interest_column)
        except Exception as e:
            CTkMessagebox(title="Помилка", message=f"Помилка бази даних: {e}", icon="cancel")
            return None

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
            CTkMessagebox(title=f"Помилка", message=f"Не вдалося знайти депозити в банку '{bank_name}' з терміном '{term}' місяців", icon="cancel")
            return None

    def calculate(self):
        money = self.entries["money"].get()

        if not money:
            CTkMessagebox(title='Помилка!', message='Введіть кількість грошей', icon="warning")
            return

        try:
            money = int(money)
        except ValueError:
            CTkMessagebox(title='Помилка!', message='Введіть гроші числом', icon="warning")
            return

        deposits_data = self.percent()

        if deposits_data:
            message = ""
            for deposit_data in deposits_data:
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
            CTkMessagebox(title='Знайдено депозит!', message=message, icon="check")
        else:
            CTkMessagebox(title="Помилка", message="Не вдалося розрахувати депозит", icon="cancel")