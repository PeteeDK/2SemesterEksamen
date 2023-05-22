import getpass
import itertools
from mysql.connector import connect


class Login:

    @staticmethod
    def LogIn():
        conn = connect(host='127.0.0.1', user='root', database='employee', password='meep')
        cursor = conn.cursor()
        id = input("Indtast dit Id: ")
        password = getpass.getpass("Indtast dit password: ")
        checkUnQuery =("SELECT id FROM employees")
        try:
            cursor.execute(checkUnQuery)
            listOfIdTuple = cursor.fetchall()
            listOfId = list(itertools.chain(*listOfIdTuple))
            if int(id) in listOfId:
                checkPwQuery = (f"SELECT password FROM employees where (`id` ={id})")
                try:
                    cursor.execute(checkPwQuery)
                    passwordlistTuple = cursor.fetchall()
                    listOfPw = [item for t in passwordlistTuple for item in t]
                    if password in listOfPw:
                        print("You are now logged in!")
                        return True
                    else:
                        print("Wrong password")
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)


