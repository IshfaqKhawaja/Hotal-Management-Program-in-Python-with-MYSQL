import mysql.connector as connector
from prettytable import PrettyTable


def customers():
    table = PrettyTable()
    print("\n")
    print("-"*60)
    print("\tCUSTOMERS STATUS ")
    print("-"*60)
    table.field_names = ['Name', 'ID']
    conn = connector.connect(host="localhost", user="root",
                             password="ishfaq", database="HOTEL")
    temp_cursor = conn.cursor()
    query = "SELECT * from CUSTOMER"
    temp_cursor.execute(query)
    for i in temp_cursor:
        table.add_row(i)
    print(table)
    conn.close()
