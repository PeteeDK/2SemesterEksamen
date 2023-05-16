import User


class CheckInAndOut:

    def CheckIn(self):
        User.User.SetCheckInStatusTo(self, True)

    def CheckOut(self):
        User.User.SetCheckInStatusTo(self, False)

    def IsCheckedIn(self):
        if (User.User.GetCheckedInStatus(self) == True):
            print("Checked in")
        else:
            print("Not Checked in")