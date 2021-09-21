import mysql.connector as connector
import sys
from prettytable import PrettyTable


def addreservation():
    conn = connector.connect(host="localhost", user="root",
                             password="ishfaq", database="HOTEL")

    temp_cursor = conn.cursor()
    temp_cursor.execute("SELECT * from CUSTOMER")
    customers = []
    for i in temp_cursor:
        customers.append(i)
    print("\n")
    print("-"*60)
    print("\tRESERVATION MENU ")
    print("-"*60)
    table = PrettyTable()
    table.field_names = [' ', 'Names']
    print("\n\n\tSelect a Customer whose Reservation is to made!")
    j = 1
    for i in customers:
        table.add_row([f"Press {j} for", f" {i[0]}"])
        j += 1
    print(table)
    customer_id = int(input("\n\n\tPlease Select one Among above : "))
    try:
        c_id = customers[customer_id-1][1]
    except Exception:
        print("\n\n\tWrong Selection Returned!")
    # print(c_id)
    date = input("\n\n\tPlease enter date of Reservation format dd/mm/yyyy : ")
    # print(date)

    # CHECK IF ALREADY RESERVED OR NOT ON THIS DATE
    query = "SELECT * FROM RESERVATION WHERE date='{}' and c_id = {}".format(
        date, c_id)
    temp_cursor.execute(query)
    flag = 0
    update = 0
    for i in temp_cursor:
        flag = 1
        print(
            "\n\n\tRESERVATION ALREADY MADE on {} for {} seats".format(date, i[3]))
        print("\n\n\tWould u like to update Reservation? Press 1 else press 0: ")
        update = int(input("\n\t ->"))
        if update != 1:
            print("\n\nRESERVATION MAINTAINED")
            return
        break
    seats = int(input("\n\n\tSeats Required : "))

    # SELECT A ROOM ON BEST FIT BASIS
    rooms = []
    temp_cursor.execute("SELECT * from ROOM ORDER BY seats asc")
    for i in temp_cursor:
        # print(i)
        rooms.append(i)
    room_no = ''
    for i in rooms:
        query = "SELECT * FROM RESERVATION WHERE room_no = '{}' and date = '{}' LIMIT 1".format(
            i[0], date)
        temp_cursor.execute(query)
        row = temp_cursor.fetchone()
        if row is not None:
            continue
        if i[1] >= seats:
            room_no = i[0]
            break

    # IF UPDATION IS NOT POSSIBLE:
    if update == 1 and room_no == '':
        print("\n\n\tReservation can't be updated on {} for {} seats, Would You like to maintain previous reservation?, then press 1 else 0 : ".format(date, seats))
        maintain = int(input('\n\n\t->'))
        if maintain != 1:
            query = "DELETE FROM RESERVATION where c_id = {} and date ='{}'".format(
                c_id, date)
            temp_cursor.execute(query)
            conn.commit()
            print("\n\n\tRESERVATION DELETED!")
            return
        else:
            print("\n\n\tPREVIOUS RESERVATION MAINTAINED!")
            return

    # MAKE A RESERVATION
    if room_no:
        #c_id, room_no, seats
        if update == 1:
            query = "UPDATE RESERVATION SET room_no = '{}' , seats = {} where c_id={} and date='{}'".format(
                room_no, seats, c_id, date)
        else:
            query = "INSERT INTO RESERVATION(c_id,date,room_no,seats) VALUES({},'{}','{}',{})".format(
                c_id, date, room_no, seats)
        # print(query)
        temp_cursor.execute(query)
        conn.commit()
        if update == 1:
            print("\n\n\tReservation Updated for {} on {}".format(
                customers[customer_id-1][0], date))
        else:
            print("\n\n\tReservation made for {} on {}".format(
                customers[customer_id-1][0], date))

    else:
        print("\n\n\tNo room available on this date, Please select a different date or different number of seats!")
    conn.close()


if __name__ == "__main__":
    addreservation()
