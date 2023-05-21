import Backend.ListOfUseresTest


class Login:

    def __init__(self):
        pass

    @staticmethod
    def Login(un,pw):
        username = un
        password = pw
        for x in Backend.ListOfUseresTest.ListOfUsers.listOfUsers:
            if x.username == un:
                if x.password == pw:
                    print("logged in")
            else:
                print("Error")


