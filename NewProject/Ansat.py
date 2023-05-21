from mysql.connector import connect
from NewProject.Person import Person


class Ansat():

    """
    def __init__(self, id, firstname, adress, phoneNr):
        super().__init__(firstname, adress, phoneNr)
        self._employeeId = id
        self._isAdmin = False

    """

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
                print(row)
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






    def UpdateEmployee(self):
        if self._isAdmin == True:
            Person._SetFirstName()
            Person._SetAdress()
            Person._SetPhoneNr()
        else:
            print("This user isn't an Admin")
