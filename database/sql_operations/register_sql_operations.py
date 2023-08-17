# sql_operations.py

from database.sql_operations.sql_operations import connect_to_database


def register_user_sql(username_info, password_info):

    conn = connect_to_database('mydatabase.db')
    cursorObj = conn.cursor()

    cursorObj.execute("SELECT username,password from user_logins where username=?", (username_info,))
    rows = cursorObj.fetchall()

    if len(rows) > 0:
        return False  # User already exists
    else:
        cursorObj.execute("INSERT INTO user_logins(username,password) values(?,?)", (username_info, password_info,))
        cursorObj.execute("INSERT INTO restos(name,menucount,emplcount) values(?,0,0)", (username_info,))
        cursorObj.execute("CREATE TABLE " + username_info + "(id integer primary key autoincrement, name text NOT NULL,price int)")
        cursorObj.execute("CREATE TABLE " + username_info + "_employees(id integer primary key autoincrement, name text NOT NULL,salary int)")
        conn.commit()
        return True  # Registration success

# Rest of your sql_operations.py code...
