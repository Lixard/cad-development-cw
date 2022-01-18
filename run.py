import tkinter as tk
from tkinter import ttk


class UI:
    def __init__(self) -> None:
        self._root = tk.TK()
        self._root.title("Курсовая по разработке САПР бАП-181 Борисов Максим")
        self._root.resizable(False, False)
        self._main_window()
        self._root.mainloop()

    def _main_window(self) -> None:
        pass
