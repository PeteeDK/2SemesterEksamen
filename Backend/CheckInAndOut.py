import User


class CheckInAndOut:

    def __init__(self):
        pass

    def CheckIn(self):
        User.User.SetCheckInStatusTo(self, True)

    def CheckOut(self):
        User.User.SetCheckInStatusTo(self, False)

    def CheckInStatus(self):
        if (User.User.GetCheckedInStatus(self) == True):
            print("Checked in")
        else:
            print("Not Checked in")
