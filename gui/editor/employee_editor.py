from tkinter import Toplevel, Label, Button, TOP, ttk, LEFT
from tkinter.ttk import Frame

from database.sql_operations import connect_to_database


def add_empl_sql():
    search_empl_name = add_empl_name.get()
    search_empl_sal = add_empl_sal.get()

    cursorObj.execute("INSERT INTO " + username1 + "_employees(name,salary) values(?,?)",
                      (search_empl_name, search_empl_sal,))
    cursorObj.execute("UPDATE restos SET emplcount = emplcount+1 where name=?", (username1,))
    print("Item added successfully.")
    con.commit()

    addemplnameval.delete(0, END)
    addemplsalval.delete(0, END)
    empl_error_label['text'] = "Item Added Successfully."
    empl_error_label['fg'] = "green"
    empl_error_label['font'] = ("calibri", 12)


def mod_empl_sql():
    search_empl_id = mod_empl_id.get()
    search_empl_name = mod_empl_name.get()
    search_empl_sal = mod_empl_sal.get()

    result_message = modify_employee(username1, search_empl_id, search_empl_name, search_empl_sal)

    empl_error_label['text'] = result_message
    if "Updated" in result_message:
        empl_error_label['fg'] = "green"
    else:
        empl_error_label['fg'] = "red"
    empl_error_label['font'] = ("calibri", 11)

    modemplidval.delete(0, END)
    modemplnameval.delete(0, END)
    modemplsalval.delete(0, END)


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


def delete_empl_sql():
    search_delete_empl_id = delete_empl_id.get()
    search_delete_empl_name = delete_empl_name.get()

    cursorObj.execute("SELECT * from " + username1 + "_employees where id = ? AND name = ?",
                      (search_delete_empl_id, search_delete_empl_name,))

    rows = cursorObj.fetchall()

    if (len(rows) > 0):
        cursorObj.execute("DELETE FROM " + username1 + "_employees where id = ? AND name = ?",
                          (search_delete_empl_id, search_delete_empl_name,))
        cursorObj.execute("UPDATE restos SET emplcount = emplcount-1 where name=?", (username1,))
        con.commit()
        empl_error_label['text'] = "Item deleted successfully."
        empl_error_label['fg'] = "green"
        empl_error_label['font'] = ("calibri", 11)

    else:

        deleteemplidval.delete(0, END)
        deleteemplnameval.delete(0, END)
        empl_error_label['text'] = "No such employee."
        empl_error_label['fg'] = "red"
        empl_error_label['font'] = ("calibri", 11)

def empl_add_item_populate():
    employee_editor_screen.destroy()
    employee_editor_open()

    global add_empl_name
    global add_empl_sal
    add_empl_name = StringVar()
    add_empl_sal = StringVar()

    global addemplnameval
    global addemplsalval

    Label(employee_editor_screen, text="Employee Name").pack()
    Label(employee_editor_screen, text="").pack()
    addemplnameval = Entry(employee_editor_screen, textvariable=add_empl_name)
    addemplnameval.pack()
    Label(employee_editor_screen, text="").pack()
    Label(employee_editor_screen, text="Employee Salary").pack()
    Label(employee_editor_screen, text="").pack()
    addemplsalval = Entry(employee_editor_screen, textvariable=add_empl_sal)
    addemplsalval.pack()
    Label(employee_editor_screen, text="").pack()
    Button(employee_editor_screen, text="Add", command=add_empl_sql).pack()
    Label(employee_editor_screen, text="").pack()


def empl_mod_item_populate():
    employee_editor_screen.destroy()
    employee_editor_open()

    global mod_empl_id
    global mod_empl_name
    global mod_empl_sal
    mod_empl_id = StringVar()
    mod_empl_name = StringVar()
    mod_empl_sal = StringVar()

    global modemplnameval
    global modemplidval
    global modemplsalval

    Label(employee_editor_screen, text="Employee ID").pack()
    Label(employee_editor_screen, text="").pack()
    modemplidval = Entry(employee_editor_screen, textvariable=mod_empl_id)
    modemplidval.pack()
    Label(employee_editor_screen, text="Employee Name").pack()
    Label(employee_editor_screen, text="").pack()
    modemplnameval = Entry(employee_editor_screen, textvariable=mod_empl_name)
    modemplnameval.pack()
    Label(employee_editor_screen, text="").pack()
    Label(employee_editor_screen, text="Employee Salary").pack()
    Label(employee_editor_screen, text="").pack()
    modemplsalval = Entry(employee_editor_screen, textvariable=mod_empl_sal)
    modemplsalval.pack()
    Label(employee_editor_screen, text="").pack()
    Button(employee_editor_screen, text="Modify", command=mod_empl_sql).pack()
    Label(employee_editor_screen, text="").pack()


def empl_delete_item_populate():
    pass
    employee_editor_screen.destroy()
    employee_editor_open()
    #
    global delete_empl_name
    delete_empl_name = StringVar()
    global delete_empl_id
    delete_empl_id = StringVar()

    global deleteemplnameval
    global deleteemplidval

    Label(employee_editor_screen, text="Empl ID").pack()
    Label(employee_editor_screen, text="").pack()
    deleteemplidval = Entry(employee_editor_screen, textvariable=delete_empl_id)
    deleteemplidval.pack()
    Label(employee_editor_screen, text="").pack()
    Label(employee_editor_screen, text="Empl Name").pack()
    Label(employee_editor_screen, text="").pack()
    deleteemplnameval = Entry(employee_editor_screen, textvariable=delete_empl_name)
    deleteemplnameval.pack()
    Label(employee_editor_screen, text="").pack()
    Button(employee_editor_screen, text="Delete", command=delete_empl_sql).pack()
    Label(employee_editor_screen, text="").pack()


def empl_list_item_populate():
    employee_editor_screen.destroy()
    employee_editor_open()

    cursorObj.execute("SELECT * from " + username1 + "_employees")

    rows = cursorObj.fetchall()

    if (len(rows) > 0):
        tree = ttk.Treeview(employee_editor_screen, column=("Id", "Name", "Salary"), show='headings')
        tree.heading("#1", text="ID")
        tree.heading("#2", text="NAME")
        tree.heading("#3", text="SALARY")
        for row in rows:
            print(row)
            tree.insert("", tk.END, values=row)
        tree.pack()

    else:

        print("No employees added yet...")

frames_to_keep = []


def clearMenuEditScreen(menuEditScreen):
    for widget in menuEditScreen.winfo_children():
        if isinstance(widget, ttk.Frame) and widget.winfo_id() not in frames_to_keep:
            widget.destroy()


def employee_editor_open(homeScreen, username1):
    homeScreen.withdraw()
    emplEditScreen = Toplevel(homeScreen)
    emplEditScreen.title("Menu Editor")
    emplEditScreen.geometry("640x480")
    Label(emplEditScreen, text="Welcome " + username1).pack()
    Label(emplEditScreen, text="").pack()

    top = Frame(emplEditScreen)
    frames_to_keep.append(top.winfo_id())
    top.pack(side=TOP)
    Button(emplEditScreen, text="Add Employee Data", command=lambda:empl_add_item_populate(emplEditScreen)).pack(in_=top, side=LEFT)
    Label(emplEditScreen, text="").pack()
    Button(emplEditScreen, text="Modify Employee Data", command=lambda:empl_mod_item_populate(emplEditScreen)).pack(in_=top, side=LEFT)
    Label(emplEditScreen, text="").pack()
    Button(emplEditScreen, text="Remove Employee", command=lambda:empl_delete_item_populate(emplEditScreen)).pack(in_=top, side=LEFT)
    Label(emplEditScreen, text="").pack()
    Button(emplEditScreen, text="List Employees", command=lambda:empl_list_item_populate(emplEditScreen)).pack(in_=top, side=LEFT)
    empl_error_label = Label(emplEditScreen, text="")
    empl_error_label.pack()