from NewProject import LogIn
from NewProject.Ansat import Ansat


class Menu:

    @staticmethod
    def LogInMenu():
        LogIn.Login().LogIn()


    @staticmethod
    def HovedeMenu():
        print(f"Velkommen til Hovede menuen")
        print("Her kan du vælge om du vil opdatere en bruger eller oprette en ny")
        option = input(" - 1 for at oprette en ny bruger\n"
                       " - 2 for at updatere en eksisterende brugeres info\n"
                       " - 3 for at lukke programmet\n")
        if option == 1:
            Ansat.CreateUser()
        elif option == 2:
            Ansat.UpdateUsersAdmin()
        elif option == 3:
            exit()