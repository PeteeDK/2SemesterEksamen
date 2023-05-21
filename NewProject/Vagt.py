import datetime


class Vagt:

    def CheckIn(self,empId):
        self._employeeId = empId
        self._checkInDateAndTime = datetime.datetime.now()

    def GetCheckInDateAndTime(self):
        self.fixedtime = self._checkInDateAndTime.strftime("%d/%m/%Y at %H:%M o'clock")
        print(f"Employee nr: {self._employeeId} checked in: {self.fixedtime}")