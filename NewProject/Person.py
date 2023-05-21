class Person():

    def __init__(self,firstname,adress,phoneNr):
        self._firstname = firstname
        self._adress = adress
        self._phoneNumber = phoneNr


#Getter and Setters

    def _GetFirstName(self):
        return self._firstname
    @staticmethod
    def _SetFirstName():
        _firstname = input("Indtast updateret navn: ")

    def _GetAdress(self):
        return self._adress
    @staticmethod
    def _SetAdress():
        _adress = input("Indtast updateret adress: ")

    def _GetPhoneNr(self):
        return self._phoneNumber
    @staticmethod
    def _SetPhoneNr():
        _phoneNumber = input("Indtast nyt telefon nummer: ")