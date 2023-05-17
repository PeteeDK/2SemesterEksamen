from Person import Person


class User(Person):

    def __init__(self, name, adress, phoneNr, username, pw, stillingsbetegnelse, id):
        super().__init__(self, name, adress, phoneNr)

        isAdmin = False   #If admin class is not needed

        self.userName = username
        self.password = pw
        self.Stillingsbetegnelse = stillingsbetegnelse
        self.ID = id

