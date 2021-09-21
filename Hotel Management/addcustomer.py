import mysql.connector as connector
from prettytable import PrettyTable


def addcustomer():
    conn = connector.connect(host="localhost", user="root",
                             password="ishfaq", database="HOTEL")
    print("\n")
    print("-"*60)
    print("\n\n\tADD CUSTOMER MENU ")
    print("-"*60)
    temp_cursor = conn.cursor()
    name = input("\n\tEnter Customer Name : ")
    query = "INSERT INTO CUSTOMER(c_name) VALUES('{}')".format(name)
    temp_cursor.execute(query)
    conn.commit()
    print("-"*60)
    print("\n\tCustomer ADDED!")
    print("\n\n\t Returned to Main Menu")
    conn.close()
