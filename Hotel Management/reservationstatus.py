import mysql.connector as connector
from prettytable import PrettyTable


def reservationstatus():
    table = PrettyTable()
    table.field_names = ['Name',
                         'Date of Reservation', 'Room Alloted', 'Seats']
    conn = connector.connect(host="localhost", user="root",
                             password="ishfaq", database="HOTEL")
    temp_cursor = conn.cursor()
    query = "SELECT * from RESERVATION"
    temp_cursor.execute(query)
    reservations = []
    for i in temp_cursor:
        reservations.append(i)
    j = 0
    for i in reservations:
        query = "SELECT c_name FROM CUSTOMER WHERE c_id ={} LIMIT 1".format(
            i[0])
        temp_cursor.execute(query)
        name = temp_cursor.fetchone()
        reservations[j] = [name[0]]+list(i[1:])
        j += 1
    table.add_rows(reservations)
    print(table)
    conn.close()


if __name__ == "__main__":
    reservationstatus()
