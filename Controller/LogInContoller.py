class Controller:

    def __init__(self, login, view):
        self.Login = login
        self.LoginPage = view

    def login(self):
        try:
            self.Login.Login()

        except TypeError as e:
            print(e)


