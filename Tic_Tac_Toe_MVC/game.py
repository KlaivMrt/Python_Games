import tkinter as tk
from controller import Controller
from view import StartPanel

if __name__ == '__main__':

    start = tk.Tk()
    StartPanel(start)
    start.mainloop()


    root = tk.Tk()
    root.counter = 0
    root.geometry('300x300')
    root.resizable(False, False)

    top = tk.Toplevel(root)
    top.resizable(False, False)

    Controller(root, top)

    root.mainloop()
