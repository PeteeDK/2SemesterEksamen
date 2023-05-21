from Backend import User


class ListOfUsers:
    listOfUsers = []

    def __init__(self):
        pass

    user1 = User.User("Jens", "Kbh", 2134, "JensMeister", "123456789")
    listOfUsers.append(user1)
    user2 = User.User("Bo", "Slagelse", "34897583475", "Bosen", "bo123")
    listOfUsers.append(user2)

    def getList(self):
        return self.listOfUsers
