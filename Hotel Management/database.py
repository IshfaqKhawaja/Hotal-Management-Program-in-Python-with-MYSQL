def cursor():
    import mysql.connector as connector
    conn = connector.connect(
        host="localhost", user="root", password="ishfaq", database="HOTEL")
    return conn


if __name__ == '__main__':
    from connection import connection
    conn = connection()
    my_cursor = conn.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS HOTEL")
    conn.close()
