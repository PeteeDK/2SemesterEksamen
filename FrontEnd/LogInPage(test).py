from tkinter import ttk

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


        self.label = ttk.Label(self, text='MainPage')
        self.label.grid(row=1, column=0)

        self.CheckIn_button = ttk.Button(self, text="Check in", command= self.Checkin_button.clicked)

        self.controller = None

    def CheckIn_button_clicked(self, controller):
        self.controller = controller

