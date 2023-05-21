import getpass
import mysql.connector


class Login:


    def OpenConnection(self):
        self._cnx = mysql.connector.connect(user='root',
                                      password = "meep",
                                      host='127.0.0.1',
                                      database='employee')

    def CloseConnection(self):
        self._cnx.close()

    @staticmethod
    def LogIn():
        id = input("Indtast dit Id")
        password = getpass.getpass("Indtast dit password")


