
class Controller:
    def __init__(self, checkInAndOut, view):
        self.CheckInAndOut = checkInAndOut
        self.MainPage = view

    def CheckIn(self):
        try:
            self.CheckInAndOut.CheckIn()

        except:
            pass

    def CheckInStatus(self):
        try:
            self.CheckInAndOut.CheckInStatus()
        except:
            pass
