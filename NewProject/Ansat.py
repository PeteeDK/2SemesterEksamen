from mysql.connector import connect
from tabulate import tabulate


class Ansat():

    def CreateUser(self):
        conn = connect(host='127.0.0.1', user='root', database='employee', password='meep')
        cursor = conn.cursor()
        id = 1

        #Checking for next unused ID
        CheckForLastUsedId=(
            "SELECT id FROM employees"
        )
        try:
            cursor.execute(CheckForLastUsedId)
            result = cursor.fetchall()

            for row in result:
                id = id + 1
                #print(row) - test
        except Exception as e:
            print(e)

        name = input("Intast navnet på den nye bruger: ")
        adress = input("Intast adressen på den nye bruger: ")
        phoneNr = input("Indtast telefon nummeret på den nye bruger: ")

        #Inserting bit
        insertNewUser =(
            "INSERT INTO employees(id, name, adress, phonenr)"
            "VALUES (%s,%s,%s,%s)"
        )
        data = [id,name,adress,phoneNr]
        try:
            cursor.execute(insertNewUser,data)
            conn.commit()
            print("Data Inserted")
        except Exception as Error:
            print(Error)
        conn.close()


    def UpdateUser(self):
        conn = connect(host='127.0.0.1', user='root', database='employee', password='meep')
        cursor = conn.cursor()

        #This stores all the IDs
        IdList = []
        ListOfIds =("SELECT id FROM employees")
        try:
            cursor.execute(ListOfIds)
            IdList = cursor.fetchall()
        except Exception as e:
            print(e)


        #Prints all useres with ID and Name
        PrintAllUseres= (
            "SELECT id, name FROM employees"
        )
        try:
            cursor.execute(PrintAllUseres)
            result = cursor.fetchall()
            print(tabulate(result, headers=["ID", "Name"]))
        except Exception as e:
            print(e)

        print("\n")
        userThatNeedsUpdateId = input("Vælge venligest den bruger som du vil opdatere ved at indtaste ID: ")
        for x in IdList:
            if x == userThatNeedsUpdateId:
                # This inserts the String into a list so that it can be used in the SQL statement
                data = [userThatNeedsUpdateId]
                SelectUserForUpdate = ("SELECT * FROM employees WHERE id = %s")
                try:
                    cursor.execute(SelectUserForUpdate, data)
                    print("yay")
                except Exception as e:
                    print(e)
            else:
                print("NO")