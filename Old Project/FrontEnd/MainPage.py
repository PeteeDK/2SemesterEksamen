from tkinter import ttk

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # UserName
        self.userNameLable = ttk.Label(text='')  # gør så den bruger username fra Person klassen
        self.userNameLable.grid(row=0, column=0)

        # Checkin_status
        self.userStatus = ttk.Button(text="Check the status", command=self.CheckInStatus_button_clicked)
        self.userStatus.grid(row=1, column=0)

        # Check in button
        self.checkIn_button = ttk.Button(text="Check In!", command=self.CheckIn_button_clicked)
        self.checkIn_button.grid(row=0, column=2)

        # check out button
        self.checkout_button = ttk.Button(text="Check Out!")
        self.checkout_button.grid(row=1, column=2)

        self.controller = None

    def SetController(self, controller):
        self.controller = controller

    def CheckIn_button_clicked(self):
        if self.controller:
            self.controller.CheckIn()

    def CheckInStatus_button_clicked(self):
        if self.controller:
            self.controller.CheckInStatus()
