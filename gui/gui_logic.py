import tkinter as tk

from gui.editor.employee_editor import employee_editor_open
from gui.editor.menu_editor import showMenuEditorUI
from gui.userMgmt.login import loginUser
from gui.userMgmt.register import registerUser


def show_register_screen(main_screen):
    main_screen.withdraw()  # Hide the main screen
    register_screen = tk.Toplevel(main_screen)
    register_screen.title("Register User")
    register_screen.geometry("640x480+200+200")
    register_screen.configure(background='lightgray')  # Light gray background

    username = tk.StringVar()
    password = tk.StringVar()

    tk.Label(register_screen, text="Create an Account", fg="black", bg="lightgray",
             font=("Calibri", 18, "bold")).pack(pady=10)

    frame = tk.Frame(register_screen, background='lightgray')
    frame.pack(pady=20, padx=20, fill='both', expand=True)

    tk.Label(frame, text="Username:", fg="black",bg="lightgray", font=("Calibri", 14)).pack(anchor='w')
    username_entry = tk.Entry(frame, textvariable=username, font=("Calibri", 14))
    username_entry.pack(fill='x', pady=5)

    tk.Label(frame, text="Password:", fg="black",bg="lightgray", font=("Calibri", 14)).pack(anchor='w')
    password_entry = tk.Entry(frame, show="*", textvariable=password, font=("Calibri", 14))
    password_entry.pack(fill='x', pady=5)

    register_button = tk.Button(frame, text="Register", width=15, height=1,
                                command=lambda: register_run_logic(username, password, register_screen, main_screen),
                                font=("Calibri", 14), bg="green", fg="white")
    register_button.pack(pady=10)

    tk.Label(register_screen, text="Already have an account?", bg="lightgray",font=("Calibri", 12)).pack(pady=10)
    login_link = tk.Label(register_screen, text="Login here", bg="lightgray",fg="blue", cursor="hand2", font=("Calibri", 12))
    login_link.pack()
    login_link.bind("<Button-1>", lambda event: show_login_screen(register_screen))

    tk.Label(register_screen, text="Explore PyRestoManager and elevate your restaurant business!",bg="lightgray", fg="black",
             font=("Calibri", 15, "italic")).pack(pady=20)



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

    # Calculate screen dimensions
    screen_width = login_screen.winfo_screenwidth()
    screen_height = login_screen.winfo_screenheight()
    x = (screen_width - 640) // 2
    y = (screen_height - 480) // 2
    login_screen.geometry(f"640x480+{x}+{y}")

    login_screen.configure(background='gray')

    tk.Label(login_screen, text="Please enter details below to login", fg="white", bg="gray",
             font=("Calibri", 18)).pack(pady=20)

    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    tk.Label(login_screen, text="Username:", fg="white", bg="gray", font=("Calibri", 14)).pack()
    username_entry1 = tk.Entry(login_screen, textvariable=username_verify, font=("Calibri", 14))
    username_entry1.pack(pady=10)

    tk.Label(login_screen, text="Password:", fg="white", bg="gray", font=("Calibri", 14)).pack()
    password_entry1 = tk.Entry(login_screen, show="*", textvariable=password_verify, font=("Calibri", 14))
    password_entry1.pack(pady=10)

    login_button = tk.Button(login_screen, text="Login", command=lambda: login_run_logic(username_verify, password_verify, username_entry1, password_entry1, login_screen, main_screen), font=("Calibri", 14), bg="green", fg="white")
    login_button.pack(pady=20)



def login_run_logic(username, password, userentry, passentry, login_screen, main_screen):
    result_enum = loginUser(username, password, userentry, passentry)
    if (result_enum == 0):
        # tk.Button(register_screen, text="Go Home",
        #           command=lambda: register_success(register_screen, main_screen)).pack()
        show_home_screen(username.get(),login_screen, main_screen)
        print("logging in now.")
    elif (result_enum == 1):
        print("wrong password")
    else:
        print("no such user.")


def login_success(register_screen, main_screen):
    register_screen.destroy()
    main_screen.deiconify()  # Show the main screen again

def show_home_screen(username1, login_screen2, main_screen):
    login_screen2.destroy()
    homeScreen = tk.Toplevel(main_screen)
    homeScreen.title("Home Screen Open Now")

    # Calculate screen dimensions
    screen_width = homeScreen.winfo_screenwidth()
    screen_height = homeScreen.winfo_screenheight()
    x = (screen_width - 640) // 2
    y = (screen_height - 480) // 2
    homeScreen.geometry(f"640x480+{x}+{y}")

    homeScreen.configure(background='lightgray')  # Light gray background

    welcome_label = tk.Label(homeScreen, text="Welcome, " + username1 + "!", fg="black",
                             font=("Calibri", 18, "italic"))
    welcome_label.pack(pady=20)

    options_frame = tk.Frame(homeScreen, background='lightgray', padx=20, pady=20, bd=2, relief="groove")
    options_frame.pack()

    menu_editor_button = tk.Button(options_frame, text="Menu Editor", command=lambda: showMenuEditorUI(homeScreen, username1),
                                   font=("Calibri", 14), bg="green", fg="white")
    menu_editor_button.grid(row=0, column=0, padx=20, pady=10)
    tk.Label(options_frame, text="Create Delicious Dishes", font=("Calibri", 12, "italic"), fg="black",
             background='lightgray').grid(row=1, column=0)
    tk.Label(options_frame, text="🍔", font=("Arial", 24), bg='lightgray').grid(row=2, column=0)

    # Divider Label
    divider_label = tk.Label(options_frame, text="", background="gray", height=1, relief="sunken")
    divider_label.grid(row=0, column=1, rowspan=3, padx=10, sticky='ns')

    employee_editor_button = tk.Button(options_frame, text="Employee Editor", command=lambda: employee_editor_open(homeScreen, username1),
                                       font=("Calibri", 14), bg="blue", fg="white")
    employee_editor_button.grid(row=0, column=2, padx=20, pady=10)
    tk.Label(options_frame, text="Manage Your Superstar Staff", font=("Calibri", 12, "italic"), fg="black",
             background='lightgray').grid(row=1, column=2)
    tk.Label(options_frame, text="👨‍🍳", font=("Arial", 24), bg='lightgray').grid(row=2, column=2)
