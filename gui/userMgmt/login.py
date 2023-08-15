from tkinter import Toplevel, StringVar, Label, Entry, Button, Frame, END

from database.login_sql_operations import login_user_sql


def login_sucess():
    global main_home_screen
    main_home_screen = Toplevel(screen)
    main_home_screen.title("Home")
    main_home_screen.geometry("640x480")
    Label(main_home_screen, text="Welcome " + username1).pack()
    Label(main_home_screen, text="").pack()
    Button(main_home_screen, text="Menu Editor", command=menu_editor_open).pack()
    Label(main_home_screen, text="").pack()
    Button(main_home_screen, text="Employee Editor", command=employee_editor_open).pack()


def password_not_recognised():
    global password_error_screen
    password_error_screen = Toplevel(screen)
    password_error_screen.title("Failure!")
    password_error_screen.geometry("150x100")
    Label(password_error_screen, text="Password Error").pack()
    Button(password_error_screen, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def loginUser(username_verify, password_verify, userentry, passentry):
    username1 = username_verify.get()
    password1 = password_verify.get()
    userentry.delete(0, END)
    passentry.delete(0, END)

    return login_user_sql(username1, password1)

