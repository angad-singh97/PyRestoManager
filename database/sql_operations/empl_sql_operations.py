from database.sql_operations.sql_operations import connect_to_database


def listEmplSQL(username1):
    conn = connect_to_database('mydatabase.db')
    cursorObj = conn.cursor()
    cursorObj.execute("SELECT * from " + username1 + "_employees")
    rows = cursorObj.fetchall()
    if (len(rows) > 0):
        return rows
    else:
        return None


def addEmplSQL(username1, search_empl_name, search_empl_sal):
    conn = connect_to_database('mydatabase.db')
    cursorObj = conn.cursor()
    cursorObj.execute("INSERT INTO " + username1 + "_employees(name,salary) values(?,?)",
                      (search_empl_name, search_empl_sal,))
    cursorObj.execute("UPDATE restos SET emplcount = emplcount+1 where name=?", (username1,))
    conn.commit()
def deleteEmplSQL(uname, idVal, nmVal):
    conn = connect_to_database('mydatabase.db')
    cursorObj = conn.cursor()
    cursorObj.execute("SELECT * from " + uname + "_employees where id = ? AND name = ?",
                      (idVal, nmVal,))

    rows = cursorObj.fetchall()
    if (len(rows) > 0):
        cursorObj.execute("DELETE FROM " + uname + "_employees where id = ? AND name = ?",
                          (idVal, nmVal,))
        cursorObj.execute("UPDATE restos SET emplcount = emplcount-1 where name=?", (uname,))
        conn.commit()
        return True
    else:
        return False

def modifyEmplSQL(username, empl_id, empl_name, empl_salary):
    conn = connect_to_database('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM {}_employees WHERE id = ? AND name = ?".format(username),
                   (empl_id, empl_name,))
    rows = cursor.fetchall()

    if len(rows) > 0:
        cursor.execute("UPDATE {}_employees SET name=?, salary=? WHERE id=?".format(username),
                       (empl_name, empl_salary, empl_id,))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False