import tkinter as tk

from Backend.User import User


user1 = User("jens","KBH","+4500000","JensManden","2134435")

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        startUp = None

        # create a view and place it on the root window
       # mainpage = FrontEnd.MainPage.View(self)
        #mainpage.grid(row=2, column=2, padx=100, pady=100)


