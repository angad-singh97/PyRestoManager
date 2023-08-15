import sqlite3
from sqlite3 import Error


def sql_connection():
    try:

        con = sqlite3.connect('../mydatabase.db')

        return con

    except Error:

        print(Error)


def initialize_database(con):
    cursorObj = con.cursor()

    cursorObj.execute(
        "CREATE TABLE IF NOT EXISTS  restos(id INTEGER PRIMARY KEY,name TEXT NOT NULL,menucount INTEGER NOT NULL,emplcount INTEGER NOT NULL)")

    cursorObj.execute("CREATE TABLE IF NOT EXISTS user_logins(username text PRIMARY KEY, password text)")

    con.commit()


if __name__ == "__main__":
    initialize_database(sql_connection())
