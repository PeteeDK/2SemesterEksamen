import tkinter as ttk
from tkinter import *
class View(ttk.Frame):

    def __init__(self,parent):
        super().__init__(parent)

        # Username label
        self.usernameLabel = ttk.Label(text="Username: ")
        self.usernameLabel.grid(row=0, column=0)

        # Username input
        self.username = Entry()
        self.username.grid(row=0,column=1)

        # Password label
        self.passwordLabel = ttk.Label(text="Password: ")
        self.passwordLabel.grid(row=1,column=0)

        # Password entry
        self.passwordEntry = ttk.Entry()
        self.passwordEntry.grid(row=1,column=1)

        #Login Button
        self.loginbutton = ttk.Button(text="Log in", command=self.Login_clicked)
        self.loginbutton.grid(row=2, column=1)

        self.controller = None

    def SetController(self,controller):
        self.controller = controller

    def Login_clicked(self):
        if self.controller:
            self.controller.Login()
