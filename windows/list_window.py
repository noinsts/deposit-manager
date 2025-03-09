import tkinter as tk

from database import get_deposits

class ListWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title('Список депозитів')
        self.geometry("1235x400")

        self.deposits = get_deposits()

        # Створюємо заголовки колонок
        headers = ["ID", "Назва", "Банк", "3-6 міс.", "6-9 міс.", "9-12 міс.", "18 міс.", "24 міс."]
        for col, header in enumerate(headers):
            label = tk.Label(self, text=header, font=("Bitstream Charter", 10), relief="solid", width=20)
            label.grid(row=0, column=col, padx=5, pady=5)

        # Виводимо депозити в таблицю
        for row, deposit in enumerate(self.deposits, start=1):
            for col, value in enumerate(deposit):
                label = tk.Label(self, text=value, font=("Bitstream Charter", 10), relief="solid", width=20)
                label.grid(row=row, column=col, padx=5, pady=5)
