# main.py
from gui import MyGUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = MyGUI(root)
    root.mainloop()
