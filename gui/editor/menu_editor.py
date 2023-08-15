from database.sql_operations import add_menu_item, connect_to_database


def add_menu_sql():
    search_item = add_item_name.get()
    search_price = add_item_price.get()

    result_message = add_menu_item(username1, search_item, search_price)

    menu_error_label['text'] = result_message
    if "already exists" in result_message:
        menu_error_label['fg'] = "red"
    else:
        menu_error_label['fg'] = "green"
    menu_error_label['font'] = ("calibri", 11)
    additemnameval.delete(0, END)
    additempriceval.delete(0, END)


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


def delete_menu_sql():
    search_delete_item = delete_item_name.get()

    cursorObj.execute("SELECT * from " + username1 + " where name = ?", (search_delete_item,))

    rows = cursorObj.fetchall()

    if (len(rows) > 0):
        cursorObj.execute("DELETE FROM " + username1 + " where name=?", (search_delete_item,))
        cursorObj.execute("UPDATE restos SET menucount = menucount-1 where name=?", (username1,))
        con.commit()
        menu_error_label['text'] = "Item deleted successfully."
        menu_error_label['fg'] = "green"
        menu_error_label['font'] = ("calibri", 11)

    else:

        deleteitemnameval.delete(0, END)
        menu_error_label['text'] = "No such item."
        menu_error_label['fg'] = "red"
        menu_error_label['font'] = ("calibri", 11)


def menu_add_item_populate():
    menu_editor_screen.destroy()
    menu_editor_open()

    global add_item_name
    global add_item_price
    add_item_name = StringVar()
    add_item_price = StringVar()

    global additemnameval
    global additempriceval

    Label(menu_editor_screen, text="Item Name").pack()
    Label(menu_editor_screen, text="").pack()
    additemnameval = Entry(menu_editor_screen, textvariable=add_item_name)
    additemnameval.pack()
    Label(menu_editor_screen, text="").pack()
    Label(menu_editor_screen, text="Item Price").pack()
    Label(menu_editor_screen, text="").pack()
    additempriceval = Entry(menu_editor_screen, textvariable=add_item_price)
    additempriceval.pack()
    Label(menu_editor_screen, text="").pack()
    Button(menu_editor_screen, text="Add", command=add_menu_sql).pack()
    Label(menu_editor_screen, text="").pack()

    ########################## -----ADD/MODIFY POPULATE FUNCTIONS############################################


########################## DELETE POPULATE FUNCTIONS############################################
def menu_delete_item_populate():
    menu_editor_screen.destroy()
    menu_editor_open()

    global delete_item_name
    delete_item_name = StringVar()

    global deleteitemnameval

    Label(menu_editor_screen, text="Item Name").pack()
    Label(menu_editor_screen, text="").pack()
    deleteitemnameval = Entry(menu_editor_screen, textvariable=delete_item_name)
    deleteitemnameval.pack()
    Label(menu_editor_screen, text="").pack()
    Label(menu_editor_screen, text="").pack()
    Button(menu_editor_screen, text="Delete", command=delete_menu_sql).pack()
    Label(menu_editor_screen, text="").pack()


def menu_list_item_populate():
    menu_editor_screen.destroy()
    menu_editor_open()

    cursorObj.execute("SELECT * from " + username1)

    rows = cursorObj.fetchall()

    if (len(rows) > 0):
        tree = ttk.Treeview(menu_editor_screen, column=("Id", "Name", "Price"), show='headings')
        tree.heading("#1", text="ID")
        tree.heading("#2", text="NAME")
        tree.heading("#3", text="PRICE")
        for row in rows:
            print(row)
            tree.insert("", tk.END, values=row)
        tree.pack()

    else:

        print("No items added yet...")

def menu_editor_open():
    global menu_editor_screen
    menu_editor_screen = Toplevel(main_home_screen)
    menu_editor_screen.title("Menu Editor")
    menu_editor_screen.geometry("640x480")
    Label(menu_editor_screen, text="Welcome " + username1).pack()
    Label(menu_editor_screen, text="").pack()

    top = Frame(menu_editor_screen)
    top.pack(side=TOP)
    Button(menu_editor_screen, text="Add/Modify Items", command=menu_add_item_populate).pack(in_=top, side=LEFT)
    Label(menu_editor_screen, text="").pack()
    Button(menu_editor_screen, text="Remove Items", command=menu_delete_item_populate).pack(in_=top, side=LEFT)
    Label(menu_editor_screen, text="").pack()
    Button(menu_editor_screen, text="List Items", command=menu_list_item_populate).pack(in_=top, side=LEFT)
    global menu_error_label
    menu_error_label = Label(menu_editor_screen, text="")
    menu_error_label.pack()