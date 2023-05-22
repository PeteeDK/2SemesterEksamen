import NewProject.LogIn
from NewProject.Menu import *


class TestApp:



    while True:
        option = input("Tryk 1 for at logge ind "
                       "eller tryk på en vilkålig knap for at lukke programmet: ")
        if option == "1":
            if LogIn.Login.LogIn() == True:
                Menu.HovedeMenu()
                break
            else:
                exit()





