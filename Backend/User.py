from CheckInAndOut import CheckInAndOut
from Person import Person


class User(Person,CheckInAndOut):

    def __init__(self, name, adress, phoneNr, username, password):
        super().__init__(name, adress, phoneNr)
