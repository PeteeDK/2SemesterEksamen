from NewProject import LogIn
from NewProject.Ansat import Ansat


class Menu:

    @staticmethod
    def LogInMenu():
        LogIn.Login().LogIn()


    @staticmethod
    def HovedeMenu():
        print(f"Velkommen til Hovede menuen {Ansat.GetEmployeName()}")