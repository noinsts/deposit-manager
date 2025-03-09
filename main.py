import customtkinter as ctk
from windows.add_window import AddWindow
from windows.update_window import UpdateWindow
from windows.remove_window import RemoveWindow
from windows.calculate_window import CalculateWindow
from windows.list_window import ListWindow
import database as db

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор депозитів")
        self.geometry("300x350")  # Встановлюємо розмір вікна

        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text='Головне меню', font=('Arial', 18, 'bold')).pack(pady=10)

        buttons = {
            'Додати депозит': AddWindow,
            'Оновити депозит': UpdateWindow,
            'Видалити депозит': RemoveWindow,
            'Розрахувати депозит': CalculateWindow,
            'Список депозитів': ListWindow,
        }

        for text, window_class in buttons.items():
            ctk.CTkButton(frame, text=text, command=lambda cls=window_class: cls(self),
                           bg_color='#4A5568', fg_color='#4A5568', hover_color='#2D3748', text_color='white').pack(pady=5, fill="x")

if __name__ == "__main__":
    db.init_db()
    app = MainApp()
    app.mainloop()