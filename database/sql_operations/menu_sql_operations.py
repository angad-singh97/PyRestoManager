from database.sql_operations.sql_operations import connect_to_database

def addMenuItemSQL(username, item_name, item_price):
    conn = connect_to_database('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name,price FROM {} WHERE name = ?".format(username), (item_name,))
    rows = cursor.fetchall()

    if len(rows) > 0:
        cursor.execute("UPDATE {} SET name=?, price=? WHERE name=?".format(username),
                       (item_name, item_price, item_name))
        conn.commit()
        conn.close()
        return "Item already exists. Updated values successfully."
    else:
        cursor.execute("INSERT INTO {}(name, price) VALUES (?, ?)".format(username), (item_name, item_price))
        cursor.execute("UPDATE restos SET menucount = menucount+1 WHERE name=?", (username,))
        conn.commit()
        conn.close()
        return "Item Added Successfully."

def deleteMenuItemSQL(username1, itemname1):
    conn = connect_to_database('mydatabase.db')
    cursorObj = conn.cursor()
    cursorObj.execute("SELECT * from " + username1 + " where name = ?", (itemname1,))

    rows = cursorObj.fetchall()

    if (len(rows) > 0):
        cursorObj.execute("DELETE FROM " + username1 + " where name=?", (itemname1,))
        cursorObj.execute("UPDATE restos SET menucount = menucount-1 where name=?", (username1,))
        conn.commit()
        return True
    else:
        return False

def listMenuItemSQL(username1):
    conn = connect_to_database('mydatabase.db')
    cursorObj = conn.cursor()
    cursorObj.execute("SELECT * from " + username1)

    rows = cursorObj.fetchall()

    if (len(rows) > 0):
        return rows
    else:
        return None