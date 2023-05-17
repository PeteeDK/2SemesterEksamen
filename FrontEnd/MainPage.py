from tkinter import ttk

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #UserName
        self.userNameLable = ttk.Label(text="jens") #gør så den bruger username fra Person klassen
        self.userNameLable.grid(row=0, column= 0)

        #Check in status
        self.userStatus = ttk.Label(text="Check in status:")
        self.userStatus.grid(row=1, column=0)

        #Check in button
        self.checkIn_button = ttk.Button(text="Check In!",command=self.CheckIn_button_clicked)
        self.checkIn_button.grid(row =0, column=2)


        #check out button
        self.checkout_button = ttk.Button(text="Check Out!")
        self.checkout_button.grid(row=1, column=2)

        #MessageLabele
        self.lable = ttk.Label(self, text='')

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.lable['text'] = message
        self.lable['foreground'] = 'red'
        self.lable['foreground'] = 'red'

    def CheckIn_button_clicked(self):




