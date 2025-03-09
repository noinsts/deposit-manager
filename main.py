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

        buttons = {
            'Додати депозит': AddWindow,
            'Оновити депозит': UpdateWindow,
            'Видалити депозит': RemoveWindow,
            'Розрахувати депозит': CalculateWindow,
            'Список депозитів': ListWindow,
        }

        for text, window_class in buttons.items():
            tk.Button(self, text=text, command=lambda cls=window_class: cls(self)).pack(fill="x")


if __name__ == "__main__":
    db.init_db()
    app = MainApp()
    app.mainloop()

"""
Python Version: 3.12
Made with ❤️ and ChatGPT
"""
