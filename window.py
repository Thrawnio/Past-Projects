from tkinter import ttk
import ttkthemes


class GUIWindow:
    def __init__(self, width: int, height: int, title: str):
        self.width = width
        self.height = height

        self.window = ttkthemes.ThemedTk(theme="arc")
        self.window.title(title)
        self.window.geometry(f"{width}x{height}")

    def run(self):
        self.window.mainloop()
