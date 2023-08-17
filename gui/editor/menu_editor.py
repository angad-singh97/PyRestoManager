from tkinter import Toplevel, Label, Button, TOP, LEFT, ttk, END, Entry, StringVar
from tkinter.ttk import Frame

from database.sql_operations.menu_sql_operations import listMenuItemSQL, addMenuItemSQL, deleteMenuItemSQL

defaultWidgets = []
deleteWidgets = []
addWidgets = []
# editWidgets = []
def resetToDefaultElements(screen, list):
    for widget in screen.winfo_children():
        if widget.winfo_id() not in list:
            widget.destroy()

def saveDefaultElements(screen, list):
    list.clear()
    for widget in screen.winfo_children():
        list.append(widget.winfo_id())



def addMenuItem(itemName, itemPrice, itemNameField, itemPriceField, panel, username):
    search_item = itemName.get()
    search_price = itemPrice.get()

    result_message = addMenuItemSQL(username, search_item, search_price)

    if "already exists" not in result_message:
        resetToDefaultElements(panel,addWidgets)
        Label(panel, text=result_message, fg="green", font=("calibri,12")).pack()
    else:
        resetToDefaultElements(panel,addWidgets)
        itemNameField.delete(0, END)
        itemPriceField.delete(0, END)
        Label(panel, text=result_message, fg="red", font=("calibri,12")).pack()


def deleteMenuItem(username1, deleteitemnameval, delete_item_name, panel):
    resObj = deleteMenuItemSQL(username1, delete_item_name.get())

    if resObj == True:
        resetToDefaultElements(panel,deleteWidgets)
        Label(panel, text="Item deleted successfully.", fg="green", font=("calibri,12")).pack()
    else:
        resetToDefaultElements(panel,deleteWidgets)
        deleteitemnameval.delete(0, END)
        Label(panel, text="No such item.", fg="red", font=("calibri,12")).pack()


def showMenuAddUI(menuEditScreen, username):
    resetToDefaultElements(menuEditScreen, defaultWidgets)
    addMenuItemFrame = Frame(menuEditScreen)
    addMenuItemFrame.pack(padx=10, pady=10, expand=True, fill="both")
    itemName = StringVar()
    itemPrice = StringVar()
    Label(addMenuItemFrame, text="Item Name").pack()
    Label(addMenuItemFrame, text="").pack()
    itemNameField = Entry(addMenuItemFrame, textvariable=itemName)
    itemNameField.pack()
    Label(addMenuItemFrame, text="").pack()
    Label(addMenuItemFrame, text="Item Price").pack()
    Label(addMenuItemFrame, text="").pack()
    itemPriceField = Entry(addMenuItemFrame, textvariable=itemPrice)
    itemPriceField.pack()
    Label(addMenuItemFrame, text="").pack()
    Button(addMenuItemFrame, text="Add", command=lambda:addMenuItem(itemName, itemPrice, itemNameField, itemPriceField, addMenuItemFrame, username)).pack()
    Label(addMenuItemFrame, text="").pack()
    saveDefaultElements(addMenuItemFrame, addWidgets)

def showMenuDeleteUI(menuEditScreen, username):
    resetToDefaultElements(menuEditScreen, defaultWidgets)
    deleteMenuItemFrame = Frame(menuEditScreen)
    deleteMenuItemFrame.pack(padx=10, pady=10, expand=True, fill="both")
    itemName = StringVar()
    Label(deleteMenuItemFrame, text="Item Name", fg="white", bg="black", font=("Arial", 14)).pack()
    Label(deleteMenuItemFrame, text="").pack()
    itemNameField = Entry(deleteMenuItemFrame, textvariable=itemName)
    itemNameField.pack()
    Label(deleteMenuItemFrame, text="").pack()
    Label(deleteMenuItemFrame, text="").pack()
    Button(deleteMenuItemFrame, text="Delete", command=lambda: deleteMenuItem(username, itemNameField, itemName, deleteMenuItemFrame),
           fg="white", bg="black", font=("Arial", 14)).pack()
    Label(deleteMenuItemFrame, text="").pack()
    saveDefaultElements(deleteMenuItemFrame,deleteWidgets)

def showMenuListUI(menuEditScreen, username):
    resetToDefaultElements(menuEditScreen, defaultWidgets)
    menuListObj = listMenuItemSQL(username)
    if menuListObj is not None:
        panel = Frame(menuEditScreen)
        panel.pack(padx=10, pady=10, expand=True, fill="both")
        tree = ttk.Treeview(panel, column=("Id", "Name", "Price"), show='headings', style="Custom.Treeview")
        tree.heading("#1", text="ID")
        tree.heading("#2", text="NAME")
        tree.heading("#3", text="PRICE")
        tree.pack(side="top", fill="both", expand=True)
        tree.tag_configure("Custom.Treeview", font=("Arial", 14), background="black", foreground="white")
        for row in menuListObj:
            tree.insert("", END, values=row)


def showMenuEditorUI(homeScreen, username):
    homeScreen.withdraw()
    menuEditScreen = Toplevel(homeScreen)
    menuEditScreen.title("Menu Editor")
    menuEditScreen.geometry("640x480+200+200")
    Label(menuEditScreen, text="Welcome " + username).pack()
    Label(menuEditScreen, text="").pack()
    top = Frame(menuEditScreen)
    top.pack(side=TOP)
    Button(menuEditScreen, text="Add/Modify Items", command=lambda: showMenuAddUI(menuEditScreen,username)).pack(
        in_=top, side=LEFT)
    Label(menuEditScreen, text="\n\n\n").pack()
    Button(menuEditScreen, text="Remove Items",
           command=lambda: showMenuDeleteUI(menuEditScreen, username)).pack(in_=top,
                                                                            side=LEFT)
    Label(menuEditScreen, text="\n\n\n").pack()
    Button(menuEditScreen, text="List Items", command=lambda: showMenuListUI(menuEditScreen, username)).pack(
        in_=top, side=LEFT)
    menu_error_label = Label(menuEditScreen, text="")
    menu_error_label.pack()
    saveDefaultElements(menuEditScreen, defaultWidgets)
