import mysql.connector as connector


def addroom():
    conn = connector.connect(host="localhost", user="root",
                             password="ishfaq", database="HOTEL")
    temp_cursor = conn.cursor()
    print("\n")
    print("-"*60)
    print("\n\n\tADD ROOM MENU ")
    print("-"*60)
    room_no = input("\n\tEnter Room no : ")
    seats = input("Total seats in above room : ")
    query = f"INSERT INTO ROOM (room_no,seats) VALUES({room_no},{seats})"
    temp_cursor.execute(query)
    conn.commit()
    print("\n\n\tRoom ADDED!")
    print("\n\n\t Returned to Main Menu")
    conn.close()


if __name__ == "__main__":
    addroom()
