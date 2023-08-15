import tkinter as tk

from gui.userMgmt.login import loginUser
from gui.userMgmt.register import registerUser


def show_register_screen(main_screen):
    main_screen.withdraw()  # Hide the main screen
    register_screen = tk.Toplevel(main_screen)
    register_screen.title("Register User")
    register_screen.geometry("640x480+100+100")

    username = tk.StringVar()
    password = tk.StringVar()

    tk.Label(register_screen, text="Please enter details below").pack()
    tk.Label(register_screen, text="").pack()
    tk.Label(register_screen, text="Username * ").pack()

    username_entry = tk.Entry(register_screen, textvariable=username)
    username_entry.pack()
    tk.Label(register_screen, text="Password * ").pack()
    password_entry = tk.Entry(register_screen, show="*", textvariable=password)
    password_entry.pack()
    tk.Label(register_screen, text="").pack()
    tk.Label(register_screen, text="Register User").pack()
    tk.Button(register_screen, text="Register", width=10, height=1,
              command=lambda: register_run_logic(username, password, register_screen, main_screen)).pack()


def register_run_logic(username, password, register_screen, main_screen):
    result_bool = registerUser(username, password)
    if (result_bool):
        tk.Button(register_screen, text="Go Home",
                  command=lambda: register_success(register_screen, main_screen)).pack()
        # Label(registration_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        # Label(registration_screen, text="User already exists.", fg="red", font=("calibri", 11)).pack()

    # register_success(register_screen, main_screen)


def register_success(register_screen, main_screen):
    register_screen.destroy()
    main_screen.deiconify()  # Show the main screen again


def show_login_screen(main_screen):
    main_screen.withdraw()  # Hide the main screen
    login_screen = tk.Toplevel(main_screen)
    login_screen.title("Login Screen Open Now")
    login_screen.geometry("640x480+100+100")

    tk.Label(login_screen, text="Please enter details below to login").pack()
    tk.Label(login_screen, text="").pack()

    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    username_entry1 = tk.Entry(login_screen, textvariable=username_verify)
    username_entry1.pack()
    tk.Label(login_screen, text="").pack()
    password_entry1 = tk.Entry(login_screen, show="*", textvariable=password_verify)
    password_entry1.pack()
    tk.Label(login_screen, text="").pack()

    tk.Label(login_screen, text="Login Screen Label").pack()
    tk.Button(login_screen, text="Login Button", command=lambda: login_run_logic(username_verify, password_verify, username_entry1, password_entry1, login_screen, main_screen)).pack()


def login_run_logic(username, password, userentry, passentry, login_screen, main_screen):
    result_enum = loginUser(username, password, userentry, passentry)
    if (result_enum == 0):
        # tk.Button(register_screen, text="Go Home",
        #           command=lambda: register_success(register_screen, main_screen)).pack()
        print("logging in now.")
    elif (result_enum == 1):
        print("wrong password")
    else:
        print("no such user.")


def login_success(register_screen, main_screen):
    register_screen.destroy()
    main_screen.deiconify()  # Show the main screen again


# def show_home_screen
