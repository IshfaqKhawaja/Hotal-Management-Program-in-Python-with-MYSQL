import mysql.connector as connector
from prettytable import PrettyTable


def edit_room():
    conn = connector.connect(host="localhost", user="root",
                             password="ishfaq", database="HOTEL")

    temp_cursor = conn.cursor()
    table = PrettyTable()
    table.field_names = [' ', 'Room No', 'Seats']
    temp_cursor = conn.cursor()
    query = "SELECT * from ROOM"
    temp_cursor.execute(query)
    print("\n")
    print("-"*60)
    print("\tEDIT ROOM MENU ")
    print("-"*60)
    print("\n\n\tSELECT ROOMS : ")
    j = 1
    rooms = []
    print("\n\n\tPlease Select Room which you want to edit! : ")
    for i in temp_cursor:
        table.add_row([f"Press {j} ", f" {i[0]}", f"{i[1]}"])
        j += 1
        rooms.append(i)
    print(table)
    try:
        choice = int(
            input("\n\n\tEnter Room No to Update or Any Other Key to Return : "))
        # print(rooms[choice-1][0])
        seats = int(input("\n\tEnter Total Seats in Room :  "))
        query = "UPDATE ROOM SET seats = {} WHERE room_no = '{}'".format(
            seats, rooms[choice-1][0])
        # print(query)
        temp_cursor.execute(query)
        conn.commit()
        print("\n\n\tRoom Updated SUCCEFULLY!")
    except Exception:
        print("\n\n\tReturned!")


def edit_customer():
    conn = connector.connect(host="localhost", user="root",
                             password="ishfaq", database="HOTEL")

    temp_cursor = conn.cursor()
    table = PrettyTable()
    table.field_names = ['  ', 'Customer Name']
    query = "SELECT * from CUSTOMER"
    temp_cursor.execute(query)
    print("\n")
    print("-"*60)
    print("\tEDIT CUSTOMER MENU ")
    print("-"*60)
    print("\n\n\tSELECT ROOMS : ")
    print("\n\n\tPlease Select the Customer Which You want To Edit : ")
    j = 1
    customers = []
    for i in temp_cursor:
        table.add_row([f"Press {j} ", f" {i[0]}"])
        j += 1
        customers.append(i)
    print(table)
    try:
        choice = int(input(
            "\n\n\tEnter the Number You Want to Edit of Any Other Key To Return to Main Menu: "))
        name = input("\n\n\tEnter New Name : ")
        query = "UPDATE CUSTOMER SET c_name = '{}' WHERE c_id = {}".format(
            name, customers[choice-1][1])
        # print(query)
        temp_cursor.execute(query)
        conn.commit()
        print("\n\n\tCustomer Updated SUCCEFULLY!")
    except Exception:
        print("\n\n\tReturned!")


if __name__ == "__main__":
    edit_room()
