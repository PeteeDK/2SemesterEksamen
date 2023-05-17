import FrontEnd as FrontEnd
import Backend as Backend


class Controller:
    def __init__(self, checkInAndOut, view):
        Backend.CheckInAndOut = checkInAndOut
        FrontEnd.MainPage = view



    def CheckIn(self):

        try:
            self.CheckIn()

        except: pass



