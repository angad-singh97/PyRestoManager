from tkinter import Toplevel, Label, Button, TOP, ttk, LEFT, END, StringVar, Entry
from tkinter.ttk import Frame

from database.sql_operations.empl_sql_operations import listEmplSQL, deleteEmplSQL, modifyEmplSQL, addEmplSQL
from database.sql_operations.sql_operations import connect_to_database


defaultWidgets = []
deleteWidgets = []
addWidgets = []
modWidgets = []

def resetToDefaultElements(screen, list):
    for widget in screen.winfo_children():
        if widget.winfo_id() not in list:
            widget.destroy()

def saveDefaultElements(screen, list):
    list.clear()
    for widget in screen.winfo_children():
        list.append(widget.winfo_id())



def addEmpl(addFrame, uname, empNm, empSal, nmFld, salFld):
    search_empl_name = empNm.get()
    search_empl_sal = empSal.get()
    addEmplSQL(uname,search_empl_name, search_empl_sal)
    nmFld.delete(0, END)
    salFld.delete(0, END)
    resetToDefaultElements(addFrame,addWidgets)
    Label(addFrame, text="Added employee data successfully.", fg="green", font=("calibri,12")).pack()


def modEmpl(empId, empName, empSal, idFld, nmFld, slyFld, modFrame, uname):
    search_empl_id = empId.get()
    search_empl_name = empName.get()
    search_empl_sal = empSal.get()
    resObj = modifyEmplSQL(uname, search_empl_id, search_empl_name, search_empl_sal)
    if resObj == True:
        resetToDefaultElements(modFrame,deleteWidgets)
        Label(modFrame, text="Updated employee data successfully.", fg="green", font=("calibri,12")).pack()
    else:
        resetToDefaultElements(modFrame,deleteWidgets)
        Label(modFrame, text="No such employee exists. Please try again.", fg="green", font=("calibri,12")).pack()
    idFld.delete(0, END)
    nmFld.delete(0, END)
    slyFld.delete(0, END)

def deleteEmpl(uname, nm, id, nmFld, idFld, panel):
    search_delete_empl_id = id.get()
    search_delete_empl_name = nm.get()
    resObj = deleteEmplSQL(uname,search_delete_empl_id,search_delete_empl_name)
    if resObj == True:
        resetToDefaultElements(panel,deleteWidgets)
        Label(panel, text="Employee record deleted successfully.", fg="green", font=("calibri,12")).pack()
    else:
        resetToDefaultElements(panel,deleteWidgets)
        idFld.delete(0, END)
        nmFld.delete(0, END)
        Label(panel, text="No such employee.", fg="red", font=("calibri,12")).pack()

def empl_add_item_populate(emplEditScreen, uname):
    resetToDefaultElements(emplEditScreen, defaultWidgets)
    addFrame = Frame(emplEditScreen)
    addFrame.pack(padx=10, pady=10, expand=True, fill="both")
    empNm = StringVar()
    empSal = StringVar()
    Label(addFrame, text="Employee Name").pack()
    Label(addFrame, text="").pack()
    nmFld = Entry(addFrame, textvariable=empNm)
    nmFld.pack()
    Label(addFrame, text="").pack()
    Label(addFrame, text="Employee Salary").pack()
    Label(addFrame, text="").pack()
    salFld = Entry(addFrame, textvariable=empSal)
    salFld.pack()
    Label(addFrame, text="").pack()
    Button(addFrame, text="Add", command=lambda:addEmpl(addFrame, uname, empNm, empSal, nmFld, salFld)).pack()
    Label(addFrame, text="").pack()
    saveDefaultElements(addFrame,addWidgets)


def empl_mod_item_populate(emplEditScreen, uname):
    resetToDefaultElements(emplEditScreen, defaultWidgets)
    modFrame = Frame(emplEditScreen)
    modFrame.pack(padx=10, pady=10, expand=True, fill="both")
    empId = StringVar()
    empName = StringVar()
    empSal = StringVar()
    Label(modFrame, text="Employee ID").pack()
    Label(modFrame, text="").pack()
    idFld = Entry(modFrame, textvariable=empId)
    idFld.pack()
    Label(modFrame, text="Employee Name").pack()
    Label(modFrame, text="").pack()
    nmFld = Entry(modFrame, textvariable=empName)
    nmFld.pack()
    Label(modFrame, text="").pack()
    Label(modFrame, text="Employee Salary").pack()
    Label(modFrame, text="").pack()
    slyFld = Entry(modFrame, textvariable=empSal)
    slyFld.pack()
    Label(modFrame, text="").pack()
    Button(modFrame, text="Modify", command=lambda:modEmpl(empId, empName, empSal, idFld, nmFld, slyFld, modFrame, uname)).pack()
    Label(modFrame, text="").pack()
    saveDefaultElements(modFrame,modWidgets)


def empl_delete_item_populate(emplEditScreen, uname):
    resetToDefaultElements(emplEditScreen, defaultWidgets)
    deleteFrame = Frame(emplEditScreen)
    deleteFrame.pack(padx=10, pady=10, expand=True, fill="both")
    emplName = StringVar()
    emplId = StringVar()
    Label(deleteFrame, text="Empl ID").pack()
    Label(deleteFrame, text="").pack()
    idField = Entry(deleteFrame, textvariable=emplId)
    idField.pack()
    Label(deleteFrame, text="").pack()
    Label(deleteFrame, text="Empl Name").pack()
    Label(deleteFrame, text="").pack()
    nameField = Entry(deleteFrame, textvariable=emplName)
    nameField.pack()
    Label(deleteFrame, text="").pack()
    Button(deleteFrame, text="Delete", command=lambda:deleteEmpl(uname, emplName, emplId, nameField, idField, deleteFrame)).pack()
    Label(deleteFrame, text="").pack()
    saveDefaultElements(deleteFrame,deleteWidgets)


def empl_list_item_populate(emplEditScreen, username1):
    resetToDefaultElements(emplEditScreen, defaultWidgets)
    resObj = listEmplSQL(username1)
    tree = ttk.Treeview(emplEditScreen, column=("Id", "Name", "Salary"), show='headings')
    tree.heading("#1", text="ID")
    tree.heading("#2", text="NAME")
    tree.heading("#3", text="SALARY")
    if resObj is not None:
        for row in resObj:
            print(row)
            tree.insert("", END, values=row)
    tree.pack()

def employee_editor_open(homeScreen, username1):
    homeScreen.withdraw()
    emplEditScreen = Toplevel(homeScreen)
    emplEditScreen.title("Menu Editor")
    emplEditScreen.geometry("640x480+200+200")
    Label(emplEditScreen, text="Welcome " + username1).pack()
    Label(emplEditScreen, text="").pack()
    top = Frame(emplEditScreen)
    top.pack(side=TOP)
    Button(emplEditScreen, text="Add Employee Data", command=lambda:empl_add_item_populate(emplEditScreen,username1)).pack(in_=top, side=LEFT)
    Label(emplEditScreen, text="").pack()
    Button(emplEditScreen, text="Modify Employee Data", command=lambda:empl_mod_item_populate(emplEditScreen,username1)).pack(in_=top, side=LEFT)
    Label(emplEditScreen, text="").pack()
    Button(emplEditScreen, text="Remove Employee", command=lambda:empl_delete_item_populate(emplEditScreen,username1)).pack(in_=top, side=LEFT)
    Label(emplEditScreen, text="").pack()
    Button(emplEditScreen, text="List Employees", command=lambda:empl_list_item_populate(emplEditScreen,username1)).pack(in_=top, side=LEFT)
    empl_error_label = Label(emplEditScreen, text="")
    empl_error_label.pack()
    saveDefaultElements(emplEditScreen, defaultWidgets)