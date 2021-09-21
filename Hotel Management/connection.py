import mysql.connector as connector


def connection():
    conn = connector.connect(host="localhost", user="root", password="ishfaq")
    return conn
