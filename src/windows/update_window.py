import tkinter as tk
from tkinter import ttk, messagebox
from src import database as db


class UpdateWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Обновити депозит')

        tk.Label(self, text='Обновити депозит', font=('Bitstream Charter', 16)).pack(pady=10)

        deposit_names = [name[0] for name in db.names_deposit()]

        if not deposit_names:
            messagebox.showerror("Помилка", "Немає доступних депозитів для оновлення.")
            self.destroy()  # Закриваємо вікно, якщо депозитів немає
            return

        # Назва депозиту
        tk.Label(self, text='Оберіть назву депозиту', font=('Bitstream Charter', 10)).pack(pady=5)
        self.name = ttk.Combobox(self, values=deposit_names, state="readonly")
        self.name.pack()
        self.name.bind("<<ComboboxSelected>>", self.update_banks)

        # Назва банку депозиту
        tk.Label(self, text='Оберіть назву банку', font=('Bitstream Charter', 10)).pack(pady=5)
        self.bank_name = ttk.Combobox(self, state="readonly")
        self.bank_name.pack()

        # Кнопка для підтвердження вибору
        tk.Button(self, text="Обрати", command=self.select, bg='green', fg='white').pack(pady=5)

    def update_banks(self, event=None):
        selected_deposit = self.name.get()
        if selected_deposit:
            # Отримати список банків для обраного депозиту
            deposit_bank_names = [bank_name[0] for bank_name in db.bank_name_deposit(selected_deposit)]
            self.bank_name['values'] = deposit_bank_names
            if deposit_bank_names:
                self.bank_name.current(0)  # Встановлюємо перший банк як вибраний за замовчуванням
            else:
                self.bank_name.set('')  # Очищаємо вибір, якщо немає банків

    def select(self):
        name = self.name.get()
        bank_name = self.bank_name.get()

        if not name or not bank_name:
            messagebox.showwarning("Помилка", "Оберіть депозит і банк!")
            return

        deposit_data = db.get_need_depo(name, bank_name)

        if deposit_data:
            EditWindow(self, name, bank_name, deposit_data)
        else:
            messagebox.showerror("Помилка", "Депозит не знайдено!")


class EditWindow(tk.Toplevel):
    def __init__(self, parent, name, bank_name, deposit_data):
        super().__init__(parent)
        self.title(f'Редагування депозиту: {name}')
        self.name = name
        self.bank_name = bank_name

        tk.Label(self, text=f"Редагування депозиту: {name}", font=('Bitstream Charter', 14)).pack(pady=10)

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
            tk.Label(self, text=label_text).pack()
            entry = tk.Entry(self)
            # Отримуємо значення з deposit_dict, якщо воно існує
            entry.insert(0, self.deposit_dict.get(key, ""))
            entry.pack()
            self.entries[key] = entry

        tk.Button(self, text="Зберегти зміни", command=self.save_changes, bg='blue', fg='white').pack(pady=10)


    def save_changes(self):
        updated_data = {term: entry.get() for term, entry in self.entries.items()}

        # Ігноруємо порожні значення
        filtered_data = {key: value for key, value in updated_data.items() if value}

        db.update_deposit(self.name, self.bank_name, filtered_data)
        messagebox.showinfo("Успіх!", "Оновлення відбулося!")
        self.destroy()
