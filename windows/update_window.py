import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

import database as db

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class UpdateWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Обновити депозит')

        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text='Обновити депозит', font=('Arial', 18, 'bold')).pack(pady=10)

        deposit_names = [name[0] for name in db.names_deposit()]
        deposit_bank_names = [bank_name[0] for bank_name in db.bank_name_deposit()]

        # Назва депозиту
        ctk.CTkLabel(frame, text='Оберіть назву депозиту', font=('Arial', 12)).pack(pady=5)
        self.name = ctk.CTkComboBox(frame, values=deposit_names, state="readonly")
        self.name.pack(pady=5)

        # Назва банку депозиту
        ctk.CTkLabel(frame, text='Оберіть назву банку', font=('Arial', 12)).pack(pady=5)
        self.bank_name = ctk.CTkComboBox(frame, values=deposit_bank_names, state="readonly")
        self.bank_name.pack(pady=5)

        # Кнопка для підтвердження вибору
        ctk.CTkButton(frame, text="Обрати", command=self.select, bg_color='#4A5568', fg_color='#4A5568', hover_color='#2D3748', text_color='white').pack(pady=10)

    def select(self):
        name = self.name.get()
        bank_name = self.bank_name.get()

        if not name or not bank_name:
            CTkMessagebox(title="Помилка", message="Оберіть депозит і банк!", icon="warning")
            return

        deposit_data = db.get_need_depo(name, bank_name)

        if deposit_data:
            EditWindow(self, name, bank_name, deposit_data)
        else:
            CTkMessagebox(title="Помилка", message="Депозит не знайдено!", icon="cancel")

class EditWindow(ctk.CTkToplevel):
    def __init__(self, parent, name, bank_name, deposit_data):
        super().__init__(parent)
        self.title(f'Редагування депозиту: {name}')
        self.name = name
        self.bank_name = bank_name

        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text=f"Редагування депозиту: {name}", font=('Arial', 18, 'bold')).pack(pady=10)

        self.entries = {}
        labels = {
            "interest_3_6": "Відсоток 3-6 міс.",
            "interest_6_9": "Відсоток 6-9 міс.",
            "interest_9_12": "Відсоток 9-12 міс.",
            "interest_18": "Відсоток 18 міс.",
            "interest_24": "Відсоток 24 міс."
        }

        # Використовуємо deposit_data напряму, оскільки це вже словник
        self.deposit_dict = deposit_data

        for key, label_text in labels.items():
            ctk.CTkLabel(frame, text=label_text, font=('Arial', 12)).pack(pady=5)
            entry = ctk.CTkEntry(frame)
            # Отримуємо значення з deposit_dict, якщо воно існує
            entry.insert(0, self.deposit_dict.get(key, ""))
            entry.pack(pady=5)
            self.entries[key] = entry

        ctk.CTkButton(frame, text="Зберегти зміни", command=self.save_changes, bg_color='#4A5568', fg_color='#4A5568', hover_color='#2D3748', text_color='white').pack(pady=10)

    def save_changes(self):
        updated_data = {term: entry.get() for term, entry in self.entries.items()}

        # Ігноруємо порожні значення
        filtered_data = {key: value for key, value in updated_data.items() if value}

        db.update_deposit(self.name, self.bank_name, filtered_data)
        CTkMessagebox(title="Успіх!", message="Оновлення відбулося!", icon="check")
        self.destroy()