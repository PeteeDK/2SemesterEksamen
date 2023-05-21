from FrontEnd.LoginPage import View
from Backend.Login import Login


class Controller:

    def __init__(self):
        self.Login = Login()
        self.LoginPage = View(self)

    def main(self):
        self.LoginPage.main()

    def OnLogingButtonClicked(self):
        username = self.LoginPage.UserNameValue
        password = self.LoginPage.PasswordValue
        Login.Login(username,password)

if __name__ == '__main__':
    login = Controller()
    login.main()

