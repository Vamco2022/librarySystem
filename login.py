import tkinter as tk

import fileWork


def backHome():
    createFull.quit()
    signWindow.quit()


def createUserCall():
    global createFull
    userName = userNameInput.get()
    password = passwordInput.get()
    fileWork.writeLine(".\\lib\\user\\userNameList.txt", userName)
    fileWork.writeLine(".\\lib\\user\\passwordList.txt", password)
    fileWork.writeLine(".\\lib\\user\\permissionList.txt", permission.get())
    createFull = tk.Tk()
    createFull.title("successful to create user")
    createFull.geometry("300x200")
    tk.Label(createFull, text="successful to create user!").place(x=50, y=0)
    tk.Button(createFull, text="OK", command=backHome).place(x=80, y=150)
    createFull.mainloop()


def signIn():
    global permission, signWindow, userNameInput, passwordInput
    signWindow = tk.Tk()
    signWindow.title("create user")
    signWindow.geometry("300x300")
    textList = ['user type', 'user name', 'password']
    labelList = []
    permission = tk.IntVar()
    tk.Radiobutton(
        signWindow,
        text="admin",
        value=1,
        variable=permission
    ).place(x=100, y=50)
    tk.Radiobutton(
        signWindow,
        text="user",
        value=0,
        variable=permission
    ).place(x=180, y=50)
    for i in range(len(textList)):
        labelList.append(
            tk.Label(
                signWindow,
                text=textList[i]
            ).place(x=5, y=50 + (i * 50))
        )
    userNameInput = tk.Entry(
        signWindow
    )
    userNameInput.place(x=100, y=100)
    passwordInput = tk.Entry(
        signWindow,
        show='*'
    )
    passwordInput.place(x=100, y=150)
    tk.Button(
        signWindow,
        text="create user",
        command=createUserCall
    ).place(x=100, y=200)
    signWindow.mainloop()
