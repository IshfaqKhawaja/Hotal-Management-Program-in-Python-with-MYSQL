import mysql.connector as connector
from prettytable import PrettyTable


def deleteroom():
    print("\n\t DELETE ROOM MENU")
    table = PrettyTable()
    table.field_names = [' ', 'Room No']
    conn = connector.connect(host="localhost", user="root",
                             password="ishfaq", database="HOTEL")
    temp_cursor = conn.cursor()
    query = "SELECT * from ROOM"
    temp_cursor.execute(query)
    print("\n\t SELECT ROOMS : ")
    j = 1
    rooms = []
    for i in temp_cursor:
        table.add_row([f"Press {j} ", f" {i[0]}"])
        j += 1
        rooms.append(i)
    print(table)
    try:
        choice = int(
            input("Enter Room No. to delete Or Any Key to return  : "))
        # print(rooms[choice-1][0])
        query = "DELETE FROM ROOM WHERE room_no = '{}'".format(
            rooms[choice-1][0])
        # print(query)
        temp_cursor.execute(query)
        conn.commit()
        print("\n\n\tRoom DELETED SUCCEFULLY!\n")
    except Exception:
        print("\n\n\tReturned!\n")
