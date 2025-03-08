import tkinter as tk
from tkinter import messagebox

import database as db

class RemoveWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Видалити депозит')

        tk.Label(self, text='Видалити депозит', font=('Bitstream Charter', 16)).pack(pady=10)

        # Назва депозиту
        tk.Label(self, text='Введіть назву депозиту', font=('Bitstream Charter', 10)).pack(pady=10)
        self.name = tk.Entry(self)
        self.name.pack()

        # Назва банку
        tk.Label(self, text='Введіть назву банку', font=('Bitstream Charter', 10)).pack(pady=10)
        self.bank_name = tk.Entry(self)
        self.bank_name.pack()

        # Delete
        tk.Button(self, text='Delete', command=self.commit, bg='red', fg='white').pack(pady=10)


    def commit(self):
        name = self.name.get()
        bank_name = self.bank_name.get()

        deleted_rows = db.remove_deposite(name, bank_name)

        if deleted_rows >= 1:
            messagebox.showinfo(title='Успіх!', message=f'Успішно видалено {deleted_rows} депозитів')
        else:
            messagebox.showerror(title='Помилка!', message='Видалення не виконалось')
