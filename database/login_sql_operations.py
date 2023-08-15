# sql_operations.py

from database.sql_operations import connect_to_database


def login_user_sql(username, password):

    conn = connect_to_database('mydatabase.db')
    cursorObj = conn.cursor()

    cursorObj.execute("SELECT username,password from user_logins where username=?", (username,))

    rows = cursorObj.fetchall()
    print(rows)
    print(type(rows))

    if (len(rows) > 0):
        if str(rows[0][1]) == password:
            return 0
        else:
            return 1
    else:
        return 2

# Rest of your sql_operations.py code...
