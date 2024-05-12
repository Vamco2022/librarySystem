import tkinter as tk

import login


def signCall():
    login.signIn()


class welcome:
    def __init__(self):
        global welcomeWindow
        welcomeWindow = tk.Tk()
        welcomeWindow.title("Welcome to library system")
        welcomeWindow.geometry("500x300")
        tk.Button(
            welcomeWindow,
            text="sign in",
            command=signCall
        ).place(x=50, y=200)
        welcomeWindow.mainloop()


welcome()
