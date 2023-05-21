import tkinter as tk
from tkinter import ttk


class View(tk.Tk):

    PAD = 20

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Checkin system")
        self._make_Main_Frame()

        self._UsernameLabel()
        self._UsernameInput()
        self._UserNameValue = tk.StringVar()

        self._PasswordLabel()
        self._PasswordEntry()
        self._PasswordValue = tk.StringVar()

        self._LoginButton()

    def _make_Main_Frame(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(padx=self.PAD,pady=self.PAD)

    def _make_lableFrame(self):
        outerFrame = ttk.Frame(self.frame)
        outerFrame.pack()


    def _UsernameLabel(self):
        usernameLabel = ttk.Label(text="Username: ")
        usernameLabel.pack()

    def _UsernameInput(self):
        self.username = ttk.Entry(textvariable=self._UserNameValue)
        self.username.pack()

    def _PasswordLabel(self):
        passwordLabel = ttk.Label(text="Password: ")
        passwordLabel.pack()

    def _PasswordEntry(self):
        self.passwordEntry = ttk.Entry(textvariable=self._PasswordValue)
        self.passwordEntry.pack()

    def _LoginButton(self):
        loginbutton = ttk.Button(
            text="Login",
            command=self.controller.OnLogingButtonClicked
        )
        loginbutton.pack()

    def main(self):
        self.mainloop()

    @property
    def PasswordValue(self):
        return self._PasswordValue

    @property
    def UserNameValue(self):
        return self._UserNameValue