# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:06:48 2019

@author: Angad
"""

import tkinter as tk
from tkinter import *
from tkintertable import TableCanvas, TableModel
from tkinter import ttk
import os
import sqlite3

con = sqlite3.connect('mydatabase.db')

cursorObj = con.cursor()
global username_info

def delete2():
  main_home_screen.destroy()

def delete3():
  password_error_screen.destroy()

def delete4():
  screen5.destroy()
################################################## ADD SQL FUNCTIONS #######################################################
def add_menu_sql():
    search_item = add_item_name.get()
    search_price = add_item_price.get()
    

    cursorObj.execute("SELECT name,price from "+username1+" where name = ?",(search_item,))
  
    rows = cursorObj.fetchall()
    
 
    if(len(rows)>0):
       cursorObj.execute("UPDATE "+username1+" SET name=?,price=? where name=?",(search_item,search_price,search_item,))
       con.commit()
       menu_error_label['text'] = "Item already exists. Updated values successfully."
       menu_error_label['fg'] = "red"
       menu_error_label['font'] = ("calibri", 11)
       
    else:
      
      cursorObj.execute("INSERT INTO "+username1+"(name,price) values(?,?)",(search_item,search_price,))
      cursorObj.execute("UPDATE restos SET menucount = menucount+1 where name=?",(username1,))
      print("Item added successfully.")
      con.commit()
  
      additemnameval.delete(0, END)
      additempriceval.delete(0, END)
    
#      Label(menu_editor_screen, text = , fg = "green" ,font = ("calibri", 11))
      menu_error_label['text'] = "Item Added Successfully."
      menu_error_label['fg'] = "green"
      menu_error_label['font'] = ("calibri", 11)

def add_empl_sql():
    search_empl_name = add_empl_name.get()
    search_empl_sal = add_empl_sal.get()
    

  
    cursorObj.execute("INSERT INTO "+username1+"_employees(name,salary) values(?,?)",(search_empl_name,search_empl_sal,))
    cursorObj.execute("UPDATE restos SET emplcount = emplcount+1 where name=?",(username1,))
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
    

    cursorObj.execute("SELECT id,name from "+username1+"_employees where id = ? AND name = ?",(search_empl_id,search_empl_name,))
  
    rows = cursorObj.fetchall()
    
 
    if(len(rows)>0):
       cursorObj.execute("UPDATE "+username1+"_employees SET name=?,salary=? where id=?",(search_empl_name,search_empl_sal,search_empl_id,))
       con.commit()
       empl_error_label['text'] = "Updated employee data successfully."
       empl_error_label['fg'] = "green"
       empl_error_label['font'] = ("calibri", 11)
       
    else:
  
      modemplidval.delete(0, END)
      modemplnameval.delete(0, END)
      modemplsalval.delete(0, END)
    
#      Label(menu_editor_screen, text = , fg = "green" ,font = ("calibri", 11))
      empl_error_label['text'] = "No such employee exists. Please try again."
      empl_error_label['fg'] = "red"
      empl_error_label['font'] = ("calibri", 11)


################################################## ----ADD SQL FUNCTIONS #######################################################

################################################## DELETE SQL FUNCTIONS #######################################################
def delete_menu_sql():
    search_delete_item = delete_item_name.get()
    

    cursorObj.execute("SELECT * from "+username1+" where name = ?",(search_delete_item,))
  
    rows = cursorObj.fetchall()
    
 
    if(len(rows)>0):
       cursorObj.execute("DELETE FROM "+username1+" where name=?",(search_delete_item,))
       cursorObj.execute("UPDATE restos SET menucount = menucount-1 where name=?",(username1,))
       con.commit() 
       menu_error_label['text'] = "Item deleted successfully."
       menu_error_label['fg'] = "green"
       menu_error_label['font'] = ("calibri", 11)
       
    else:
      
      deleteitemnameval.delete(0, END)
      menu_error_label['text'] = "No such item."
      menu_error_label['fg'] = "red"
      menu_error_label['font'] = ("calibri", 11)      

def delete_empl_sql():
    search_delete_empl_id = delete_empl_id.get()
    search_delete_empl_name = delete_empl_name.get()
    

    cursorObj.execute("SELECT * from "+username1+"_employees where id = ? AND name = ?",(search_delete_empl_id,search_delete_empl_name,))
  
    rows = cursorObj.fetchall()
    
 
    if(len(rows)>0):
       cursorObj.execute("DELETE FROM "+username1+"_employees where id = ? AND name = ?",(search_delete_empl_id,search_delete_empl_name,))
       cursorObj.execute("UPDATE restos SET emplcount = emplcount-1 where name=?",(username1,))
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

   
##################################################----- DELETE SQL FUNCTIONS #######################################################      

 ########################## ADD/MODIFY POPULATE FUNCTIONS############################################ 


def empl_add_item_populate():

    employee_editor_screen.destroy()
    employee_editor_open()
    
    global add_empl_name
    global add_empl_sal
    add_empl_name = StringVar()
    add_empl_sal =StringVar()

    global addemplnameval
    global addemplsalval
    
    Label(employee_editor_screen, text="Employee Name").pack()
    Label(employee_editor_screen, text = "").pack()
    addemplnameval = Entry(employee_editor_screen,textvariable=add_empl_name)
    addemplnameval.pack()
    Label(employee_editor_screen, text = "").pack()
    Label(employee_editor_screen, text="Employee Salary").pack()
    Label(employee_editor_screen, text = "").pack()
    addemplsalval = Entry(employee_editor_screen,textvariable=add_empl_sal)
    addemplsalval.pack()
    Label(employee_editor_screen, text = "").pack()
    Button(employee_editor_screen,text="Add",command=add_empl_sql).pack()
    Label(employee_editor_screen, text = "").pack()
    
    
def empl_mod_item_populate():

    employee_editor_screen.destroy()
    employee_editor_open()
    
    global mod_empl_id
    global mod_empl_name
    global mod_empl_sal
    mod_empl_id = StringVar()
    mod_empl_name = StringVar()
    mod_empl_sal =StringVar()

    global modemplnameval
    global modemplidval
    global modemplsalval
    
    
    Label(employee_editor_screen, text="Employee ID").pack()
    Label(employee_editor_screen, text = "").pack()
    modemplidval = Entry(employee_editor_screen,textvariable=mod_empl_id)
    modemplidval.pack()   
    Label(employee_editor_screen, text="Employee Name").pack()
    Label(employee_editor_screen, text = "").pack()
    modemplnameval = Entry(employee_editor_screen,textvariable=mod_empl_name)
    modemplnameval.pack()
    Label(employee_editor_screen, text = "").pack()
    Label(employee_editor_screen, text="Employee Salary").pack()
    Label(employee_editor_screen, text = "").pack()
    modemplsalval = Entry(employee_editor_screen,textvariable=mod_empl_sal)
    modemplsalval.pack()
    Label(employee_editor_screen, text = "").pack()
    Button(employee_editor_screen,text="Modify",command=mod_empl_sql).pack()
    Label(employee_editor_screen, text = "").pack()
    
def menu_add_item_populate():

    menu_editor_screen.destroy()
    menu_editor_open()
    
    global add_item_name
    global add_item_price
    add_item_name = StringVar()
    add_item_price =StringVar()

    global additemnameval
    global additempriceval
    
    Label(menu_editor_screen, text="Item Name").pack()
    Label(menu_editor_screen, text = "").pack()
    additemnameval = Entry(menu_editor_screen,textvariable=add_item_name)
    additemnameval.pack()
    Label(menu_editor_screen, text = "").pack()
    Label(menu_editor_screen, text="Item Price").pack()
    Label(menu_editor_screen, text = "").pack()
    additempriceval = Entry(menu_editor_screen,textvariable=add_item_price)
    additempriceval.pack()
    Label(menu_editor_screen, text = "").pack()
    Button(menu_editor_screen,text="Add",command=add_menu_sql).pack()
    Label(menu_editor_screen, text = "").pack()    

   ########################## -----ADD/MODIFY POPULATE FUNCTIONS############################################ 

########################## DELETE POPULATE FUNCTIONS############################################ 
def menu_delete_item_populate():

    menu_editor_screen.destroy()
    menu_editor_open()
    
    global delete_item_name
    delete_item_name = StringVar()


    global deleteitemnameval

    
    Label(menu_editor_screen, text="Item Name").pack()
    Label(menu_editor_screen, text = "").pack()
    deleteitemnameval = Entry(menu_editor_screen,textvariable=delete_item_name)
    deleteitemnameval.pack()   
    Label(menu_editor_screen, text = "").pack()
    Label(menu_editor_screen, text = "").pack()
    Button(menu_editor_screen,text="Delete",command=delete_menu_sql).pack()
    Label(menu_editor_screen, text = "").pack()
    
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
    Label(employee_editor_screen, text = "").pack()
    deleteemplidval = Entry(employee_editor_screen,textvariable=delete_empl_id)
    deleteemplidval.pack()   
    Label(employee_editor_screen, text = "").pack()
    Label(employee_editor_screen, text="Empl Name").pack()
    Label(employee_editor_screen, text = "").pack()
    deleteemplnameval = Entry(employee_editor_screen,textvariable=delete_empl_name)
    deleteemplnameval.pack() 
    Label(employee_editor_screen, text = "").pack()
    Button(employee_editor_screen,text="Delete",command=delete_empl_sql).pack()
    Label(employee_editor_screen, text = "").pack()

########################## ------DELETE POPULATE FUNCTIONS############################################ 

########################## LIST POPULATE FUNCTIONS############################################ 
def menu_list_item_populate():

    menu_editor_screen.destroy()
    menu_editor_open()
    
    cursorObj.execute("SELECT * from "+username1)
  
    rows = cursorObj.fetchall()
    
 
    if(len(rows)>0):
        tree = ttk.Treeview(menu_editor_screen, column=("Id","Name","Price"),show='headings')
        tree.heading("#1", text="ID")
        tree.heading("#2", text="NAME")
        tree.heading("#3", text="PRICE")
        for row in rows:
            print(row)
            tree.insert("",tk.END,values=row)                     
        tree.pack()
       
    else:
      
      print("No items added yet...")
    
def empl_list_item_populate():

    employee_editor_screen.destroy()
    employee_editor_open()
    
    cursorObj.execute("SELECT * from "+username1+"_employees")
  
    rows = cursorObj.fetchall()
    
 
    if(len(rows)>0):
        tree = ttk.Treeview(employee_editor_screen, column=("Id","Name","Salary"),show='headings')
        tree.heading("#1", text="ID")
        tree.heading("#2", text="NAME")
        tree.heading("#3", text="SALARY")
        for row in rows:
            print(row)
            tree.insert("",tk.END,values=row)                     
        tree.pack()
       
    else:
      
      print("No employees added yet...")

  ########################## -----LIST POPULATE FUNCTIONS############################################   
  
  
    ########################## EDITOR MENU FUNCTIONS############################################  
  
def menu_editor_open():
    global menu_editor_screen
    menu_editor_screen = Toplevel(main_home_screen)
    menu_editor_screen.title("Menu Editor")
    menu_editor_screen.geometry("640x480")
    Label(menu_editor_screen, text = "Welcome "+username1).pack()
    Label(menu_editor_screen, text = "").pack()
    
    top = Frame(menu_editor_screen)
    top.pack(side=TOP)
    Button(menu_editor_screen, text = "Add/Modify Items", command =menu_add_item_populate).pack(in_=top,side=LEFT)
    Label(menu_editor_screen, text = "").pack()
    Button(menu_editor_screen, text = "Remove Items", command =menu_delete_item_populate).pack(in_=top,side=LEFT)
    Label(menu_editor_screen, text = "").pack()
    Button(menu_editor_screen, text = "List Items", command =menu_list_item_populate).pack(in_=top,side=LEFT)
    global menu_error_label
    menu_error_label = Label(menu_editor_screen, text = "")
    menu_error_label.pack()



def employee_editor_open():
    global employee_editor_screen
    employee_editor_screen = Toplevel(main_home_screen)
    employee_editor_screen.title("Menu Editor")
    employee_editor_screen.geometry("640x480")
    Label(employee_editor_screen, text = "Welcome "+username1).pack()
    Label(employee_editor_screen, text = "").pack()
    
    top = Frame(employee_editor_screen)
    top.pack(side=TOP)
    Button(employee_editor_screen, text = "Add Employee Data", command =empl_add_item_populate).pack(in_=top,side=LEFT)
    Label(employee_editor_screen, text = "").pack()
    Button(employee_editor_screen, text = "Modify Employee Data", command =empl_mod_item_populate).pack(in_=top,side=LEFT)
    Label(employee_editor_screen, text = "").pack()
    Button(employee_editor_screen, text = "Remove Employee", command =empl_delete_item_populate).pack(in_=top,side=LEFT)
    Label(employee_editor_screen, text = "").pack()
    Button(employee_editor_screen, text = "List Employees", command =empl_list_item_populate).pack(in_=top,side=LEFT)
    global empl_error_label
    empl_error_label = Label(employee_editor_screen, text = "")
    empl_error_label.pack()

  ########################## -----EDITOR MENU FUNCTIONS############################################  

def login_sucess():
  global main_home_screen
  main_home_screen = Toplevel(screen)
  main_home_screen.title("Home")
  main_home_screen.geometry("640x480")
  Label(main_home_screen, text = "Welcome "+username1).pack()
  Label(main_home_screen, text = "").pack()
  Button(main_home_screen, text = "Menu Editor", command =menu_editor_open).pack()
  Label(main_home_screen, text = "").pack()
  Button(main_home_screen, text = "Employee Editor", command =employee_editor_open).pack()


def password_not_recognised():
  global password_error_screen
  password_error_screen = Toplevel(screen)
  password_error_screen.title("Failure!")
  password_error_screen.geometry("150x100")
  Label(password_error_screen, text = "Password Error").pack()
  Button(password_error_screen, text = "OK", command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()


def close_login():
    registration_screen.destroy()
def register_user():
  print("working")
  

  username_info = username.get()
  password_info = password.get()
  
  cursorObj.execute("SELECT username,password from user_logins where username=?",(username_info,))
  
  rows = cursorObj.fetchall()
 
  if(len(rows)>0):
       print("User already exists.")
  else:
      
      cursorObj.execute("INSERT INTO user_logins(username,password) values(?,?)",(username_info,password_info,))
      cursorObj.execute("INSERT INTO restos(name,menucount,emplcount) values(?,0,0)",(username_info,))      
      cursorObj.execute("CREATE TABLE "+username_info+"(id integer primary key autoincrement, name text NOT NULL,price int)")
      cursorObj.execute("CREATE TABLE "+username_info+"_employees(id integer primary key autoincrement, name text NOT NULL,salary int)")
      con.commit()
  
      username_entry.delete(0, END)
      password_entry.delete(0, END)
    
      Label(registration_screen, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()
      Button(registration_screen, text="Go back to Home Screen",command=close_login).pack()

def login_verify():
  
  global username1
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  cursorObj.execute("SELECT username,password from user_logins where username=?",(username1,))
  
  rows = cursorObj.fetchall()
  print(rows)
  print(type(rows))
  
  if(len(rows)>0):
      if str(rows[0][1]) == password1:
          login_sucess()
      else:
          password_not_recognised()
  else:
        user_not_found()
  


def register():
  global registration_screen
  registration_screen = Toplevel(screen)
  registration_screen.title("Register")
  registration_screen.geometry("640x480")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(registration_screen, text = "Please enter details below").pack()
  Label(registration_screen, text = "").pack()
  Label(registration_screen, text = "Username * ").pack()
 
  username_entry = Entry(registration_screen, textvariable = username)
  username_entry.pack()
  Label(registration_screen, text = "Password * ").pack()
  password_entry =  Entry(registration_screen,show = "*", textvariable = password)
  password_entry.pack()
  Label(registration_screen, text = "").pack()
  Button(registration_screen, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
  global login_screen
  login_screen = Toplevel(screen)
  login_screen.title("Login")
  login_screen.geometry("640x480")
  Label(login_screen, text = "Please enter details below to login").pack()
  Label(login_screen, text = "").pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(login_screen, text = "Username * ").pack()
  username_entry1 = Entry(login_screen, textvariable = username_verify)
  username_entry1.pack()
  Label(login_screen, text = "").pack()
  Label(login_screen, text = "Password * ").pack()
  password_entry1 = Entry(login_screen, show = "*", textvariable = password_verify)
  password_entry1.pack()
  Label(login_screen, text = "").pack()
  Button(login_screen, text = "Login", width = 10, height = 1, command = login_verify).pack()
  
  
def main_screen():
  global screen
  screen = Tk()
  screen.configure(background='black')
  screen.geometry("640x480")
  screen.title("RIMS - Restaurant Inventory Management System")

  Label(text = "RIMS - Restaurant Inventory Management System",fg="white", bg = "grey", width = "640", height = "2", font = ("Calibri", 18)).pack()
  Label(text = "",background="black",).pack()
  Label(text = "",background="black").pack()
  Label(text = "",background="black").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "",background="black").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()

  screen.mainloop()

main_screen()
  
