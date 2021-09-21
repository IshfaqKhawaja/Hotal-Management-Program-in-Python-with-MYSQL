import mysql.connector as connector
from prettytable import PrettyTable


def rooms():
    table = PrettyTable()
    print("\n")
    print("-"*60)
    print("\tROOMS STATUS ")
    print("-"*60)
    table.field_names = ['Room No', 'Seats']
    conn = connector.connect(host="localhost", user="root",
                             password="ishfaq", database="HOTEL")
    temp_cursor = conn.cursor()
    query = "SELECT * from ROOM"
    temp_cursor.execute(query)
    for i in temp_cursor:
        table.add_row(i)
    print(table)
    conn.close()
