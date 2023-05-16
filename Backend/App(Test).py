import tkinter as tk

import FrontEnd as FrontEnd

import Backend as Backend

from FrontEnd import MainPage


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

    # create a model
        model = Backend.CheckInAndOut

        # create a view and place it on the root window
        view = FrontEnd.MainPage
        view.grid(row=0, column=0, padx=10, pady=10)

    # create a controller
        #controller = Controller(model, view)

    # set the controller to view
        #view.set_controller(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()