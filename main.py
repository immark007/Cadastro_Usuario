from app.controllers.interface import UserApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = UserApp(root)
    root.mainloop()