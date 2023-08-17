import sqlite3

def connect_to_database(database_name):
    return sqlite3.connect(database_name)

def modify_employee(username, empl_id, empl_name, empl_salary):
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
        return "Updated employee data successfully."
    else:
        conn.close()
        return "No such employee exists. Please try again."
