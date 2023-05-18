from Person import Person

class User(Person):

    def __init__(self, name, adress, phoneNr, username, pw):
        super().__init__(self, name, adress)

        isAdmin = False   #If admin class is not needed

        self.userName = username
        self.password = pw
        self.Stillingsbetegnelse = None
        self.ID = None

