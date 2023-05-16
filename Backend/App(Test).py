import tkinter as tk
import FrontEnd as FrontEnd
from FrontEnd import MainPage


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('CheckInSystem')

        # create a view and place it on the root window
        mainpage = FrontEnd.MainPage.View(self)
        mainpage.grid(row=2, column=2, padx=100, pady=100)


if __name__ == '__main__':
    app = App()
    app.mainloop()

