if __name__ == "__main__":
    import mysql.connector as connector
    conn = connector.connect(
        host="localhost", user="root", password="ishfaq", database="HOTEL")
    temp_cursor = conn.cursor()
    temp_cursor.execute(
        "CREATE TABLE IF NOT EXISTS ROOM (room_no varchar(20) primary key,seats int)")
    temp_cursor.execute(
        "CREATE TABLE IF NOT EXISTS CUSTOMER (c_name varchar(20) ,c_id int primary key auto_increment)")
    temp_cursor.execute(
        "CREATE TABLE IF NOT EXISTS RESERVATION(c_id int, date varchar(20), room_no varchar(20) , seats int, FOREIGN KEY(c_id) REFERENCES CUSTOMER(c_id) on delete cascade, FOREIGN KEY(room_no) REFERENCES ROOM(room_no) on delete cascade)")
    conn.close()
    print("All Tables Created!")
