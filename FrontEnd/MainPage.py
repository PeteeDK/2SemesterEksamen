from tkinter import ttk

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #Check in button
        self.checkIn_button = ttk.Button(text="Check In!",command=self.CheckIn_button_clicked)
        self.checkIn_button.grid(row =0, column=2)


        #check out button
        self.checkout_button = ttk.Button(text="Check Out!")
        self.checkout_button.grid(row=1, column=2)

        self.controller = None

    def CheckIn_button_clicked(self, controller):
        self.controller = controller
