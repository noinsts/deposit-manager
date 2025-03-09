import customtkinter as ctk
from tkinter import ttk

from database import get_deposits

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class ListWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title('Список депозитів')
        self.geometry("1235x400")

        self.deposits = get_deposits()

        # Створюємо таблицю за допомогою ttk.Treeview
        self.tree = ttk.Treeview(self, columns=("ID", "Назва", "Банк", "3-6 міс.", "6-9 міс.", "9-12 міс.", "18 міс.", "24 міс."), show="headings")

        # Налаштовуємо заголовки колонок
        headers = ["ID", "Назва", "Банк", "3-6 міс.", "6-9 міс.", "9-12 міс.", "18 міс.", "24 міс."]
        for col, header in enumerate(headers):
            self.tree.heading(col, text=header)
            self.tree.column(col, width=150)  # Встановлюємо ширину колонок

        # Вставляємо дані в таблицю
        for deposit in self.deposits:
            self.tree.insert("", "end", values=deposit)

        self.tree.pack(padx=10, pady=10, fill="both", expand=True)