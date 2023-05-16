class Person:

    def __init__(self,id,name,adress,phoneNr):
        self.__Id = id
        self.__Name = name
        self.__Adress = adress
        self.__PhoneNr = phoneNr
        self.__CheckedInStatus = False

# Getter and setter
    def GetName(self):
        return self.__Name

    def SetName(self,newName):
        self.__Name = newName

    def GetAdress(self):
        return self.__Adress

    def SetAdress(self,newAdress):
        self.__Adress = newAdress

    def GetPhoneNr(self):
        return self.__PhoneNr

    def SetPhoneNr(self,newNumber):
        self.__PhoneNr = newNumber

    def GetCheckedInStatus(self):
        return self.__CheckedInStatus

    def SetCheckInStatusTo(self, x):
        self.__CheckedInStatus = x
