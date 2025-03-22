import tkinter as tk
from tkinter import messagebox

from src import database as db


class RemoveWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Видалити депозит')

        tk.Label(self, text='Видалити депозит', font=('Bitstream Charter', 16)).pack(pady=10)

        labels = {
            'Введіть назву депозиту': tk.Entry(self),
            'Введіть назву банку' : tk.Entry(self)
        }

        self.entries = labels

        for text, entry in labels.items():
            tk.Label(self, text=text, font=('Bitstream Charter', 10))
            entry.pack()

        # Delete
        tk.Button(self, text='Delete', command=self.commit, bg='red', fg='white').pack(pady=10)


    def commit(self):
        name = self.entries["Введіть назву депозиту"].get()
        bank_name = self.entries["Введіть назву банку"].get()

        if not name or not bank_name:
            messagebox.showerror(title='Помилка!', message='Введіть назву депозиту та банку')
            return

        deleted_rows = db.remove_deposite(name, bank_name)

        if deleted_rows >= 1:
            messagebox.showinfo(title='Успіх!', message=f'Успішно видалено {deleted_rows} депозитів')
        else:
            messagebox.showerror(title='Помилка!', message='Видалення не виконалось')
