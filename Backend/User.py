from Person import Person


class User(Person):

    def __init__(self, name, adress, phoneNr, username, password):
        super().__init__(self, name, adress, phoneNr)

        isAdmin = False #If admin class is not needed