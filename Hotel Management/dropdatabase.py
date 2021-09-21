if __name__ == '__main__':
    from connection import connection
    conn = connection()
    my_cursor = conn.cursor()
    my_cursor.execute("DROP DATABASE HOTEL")
    conn.commit()
    conn.close()
