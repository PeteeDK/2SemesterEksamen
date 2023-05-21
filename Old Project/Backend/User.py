from Backend import Person


class User(Person.Person):

    def __init__(self, name, adress, phoneNr, un, pw):
        Person.Person.__init__(self, name, adress, phoneNr)
        self.username = un
        self.password = pw

