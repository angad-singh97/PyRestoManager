import sqlite3

def connect_to_database(database_name):
    return sqlite3.connect(database_name)

def add_menu_item(username, item_name, item_price):
    conn = connect_to_database('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name,price FROM {} WHERE name = ?".format(username), (item_name,))
    rows = cursor.fetchall()

    if len(rows) > 0:
        cursor.execute("UPDATE {} SET name=?, price=? WHERE name=?".format(username), (item_name, item_price, item_name))
        conn.commit()
        conn.close()
        return "Item already exists. Updated values successfully."
    else:
        cursor.execute("INSERT INTO {}(name, price) VALUES (?, ?)".format(username), (item_name, item_price))
        cursor.execute("UPDATE restos SET menucount = menucount+1 WHERE name=?", (username,))
        conn.commit()
        conn.close()
        return "Item Added Successfully."


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
