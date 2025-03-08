import tkinter as tk


class RemoveWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Видалити депозит')

        """
        WIDGETS HERE
        """
