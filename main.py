import tkinter as tk
from windows.add_window import AddWindow
from windows.update_window import UpdateWindow
from windows.remove_window import RemoveWindow
from windows.calculate_window import CalculateWindow
from windows.list_window import ListWindow
import database as db


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор депозитів")

        tk.Label(self, text='Головне меню', font=('Arial', 16)).pack(pady=10)
        tk.Button(self, text='Додати депозит', command=self.open_add_deposit).pack(fill="x")
        tk.Button(self, text='Оновити депозит', command=self.open_update_deposit).pack(fill="x")
        tk.Button(self, text='Видалити депозит', command=self.open_remove_window).pack(fill="x")
        tk.Button(self, text='Розрахувати депозит', command=self.open_calculate_window).pack(fill="x")
        tk.Button(self, text='Список депозитів', command=self.open_list_window).pack(fill="x")

    def open_add_deposit(self):
        AddWindow(self)

    def open_update_deposit(self):
        UpdateWindow(self)

    def open_remove_window(self):
        RemoveWindow(self)

    def open_calculate_window(self):
        CalculateWindow(self)

    def open_list_window(self):
        ListWindow(self)


if __name__ == "__main__":
    db.init_db()
    app = MainApp()
    app.mainloop()

"""
Python Version: 3.12
Made with ❤️ and ChatGPT
"""
