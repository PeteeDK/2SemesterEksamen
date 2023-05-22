from mysql.connector import connect
from tabulate import tabulate

import NewProject.LogIn


class Ansat():

    def CreateUser(self):
        conn = connect(host='127.0.0.1', user='root', database='employee', password='meep')
        cursor = conn.cursor()
        id = 1

        # Checking for next unused ID
        CheckForLastUsedId = (
            "SELECT id FROM employees"
        )
        try:
            cursor.execute(CheckForLastUsedId)
            result = cursor.fetchall()

            for row in result:
                id = id + 1
        except Exception as e:
            print(e)

        name = input("Intast navnet på den nye bruger: ")
        adress = input("Intast adressen på den nye bruger: ")
        phoneNr = input("Indtast telefon nummeret på den nye bruger: ")
        password = input("Indtast et password for den nyebruger: ")

        # Inserting bit
        insertNewUser = (
            "INSERT INTO employees(id, name, adress, phonenr,password)"
            "VALUES (%s,%s,%s,%s,%S)"
        )
        data = [id, name, adress, phoneNr,password]
        try:
            cursor.execute(insertNewUser, data)
            conn.commit()
            print("Data Inserted")
        except Exception as Error:
            print(Error)
        conn.close()

    def UpdateUsersAdmin(self):
        conn = connect(host='127.0.0.1', user='root', database='employee', password='meep')
        cursor = conn.cursor()
        IdListOfTuples = []
        IdList = []

        # This stores all the IDs
        ListOfIds = ("SELECT id FROM employees")
        try:
            cursor.execute(ListOfIds)
            IdListOfTuples = cursor.fetchall()
        except Exception as e:
            print(e)

        for element in IdListOfTuples:
            intElement = int(element[0])
            IdList.append(intElement)

        # Prints all useres with ID and Name
        PrintAllUseres = (
            "SELECT id, name FROM employees"
        )
        try:
            cursor.execute(PrintAllUseres)
            result = cursor.fetchall()
            print(tabulate(result, headers=["ID", "Name"]))
        except Exception as e:
            print(e)

        print("\n")
        userThatNeedsUpdateId = int(input("Vælge venligest den bruger som du vil opdatere ved at indtaste ID: "))

        for item in IdList:
            if item == userThatNeedsUpdateId:
                # This inserts the String into a list so that it can be used in the SQL statement
                data = [userThatNeedsUpdateId]

                # ToString
                for x in data:
                    dataToString = str(x)

                SelectUserForUpdate = ("SELECT * FROM employees WHERE id = %s")
                try:
                    cursor.execute(SelectUserForUpdate, data)
                    userInfo = cursor.fetchall()
                    print(tabulate(userInfo, headers=["Navn", "Adresse", "Tlf"]))
                    print("Hvad vil du opdatere? ")
                    whatNeedsUpdating = input("Opdatere navn tryk: 1\n"
                                              "Opdatere adresse tryk: 2\n"
                                              "Opdatere telefon nummer tryk: 3\n")
                    if whatNeedsUpdating == "1":
                        newName = input("Intast det nye navn: ")
                        updateNameQuery = (
                            f"update employee.employees Set name = '{newName}' Where (`id` = '{dataToString}');"
                        )
                        try:
                            cursor.execute(updateNameQuery)
                            conn.commit()
                        except Exception as e:
                            print(e)
                    elif whatNeedsUpdating == "2":
                        newAdresse = input("Intast den nye adresse: ")
                        updateAdressQuery = (
                            f"update employee.employees Set adress = '{newAdresse}' Where (`id` = '{dataToString}');"
                        )
                        try:
                            cursor.execute(updateAdressQuery)
                            conn.commit()
                        except Exception as e:
                            print(e)
                    elif whatNeedsUpdating == "3":
                        newPhoneNr = input("Indtast det nye telefon nummer: ")
                        updatePhoneQuery =(
                            f"update employee.employees Set phonenr = '{newPhoneNr}' Where (`id` = '{dataToString}');"
                        )
                        try:
                            cursor.execute(updatePhoneQuery)
                            conn.commit()
                            print("Telefon nummer updateret")
                        except Exception as e:
                            print(e)
                except Exception as e:
                    print(e)

    @staticmethod
    def GetEmployeName():
        conn = connect(host='127.0.0.1', user='root', database='employee', password='meep')
        cursor = conn.cursor()
        getNameQuery = (f"SELECT ´name´ FROM employees WHERE ´id´ = {NewProject.LogIn.Login().GetID()}")
        try:
            cursor.execute(getNameQuery)
            conn.commit()
        except Exception as e:
            print(e)