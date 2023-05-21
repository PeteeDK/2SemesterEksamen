from Backend.Person import Person


class Admin(Person):

    def __int__(self, name, adress, phoneNr, username, password):
        super().__init__(self,name,adress,phoneNr)