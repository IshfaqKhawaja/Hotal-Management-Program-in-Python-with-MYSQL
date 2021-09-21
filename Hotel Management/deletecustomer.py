import mysql.connector as connector
from prettytable import PrettyTable


def deletecustomer():
    print("\n\tDELETE CUSTOMER MENU")
    table = PrettyTable()
    table.field_names = ['  ', 'Customer Name']
    conn = connector.connect(host="localhost", user="root",
                             password="ishfaq", database="HOTEL")
    temp_cursor = conn.cursor()
    query = "SELECT * from CUSTOMER"
    temp_cursor.execute(query)
    print("\n\tSELECT CUSTOMER : ")
    customers = []
    j = 1
    for i in temp_cursor:
        table.add_row([f"Press {j} ", f" {i[0]}"])
        j += 1
        customers.append(i)
    print(table)
    # print(customers[choice-1][0])
    try:
        choice = int(input("Enter ID of Customer to DELETE : "))
        query = "DELETE FROM CUSTOMER WHERE c_id = {}".format(
            customers[choice-1][1])
        # print(query)
        temp_cursor.execute(query)
        conn.commit()
        print("\n\n\tCUSTOMER DELETED SUCCEFULLY!\n")
    except Exception:
        print("\n\n\tReturned!\n")
