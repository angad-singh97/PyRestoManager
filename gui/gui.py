import tkinter as tk
from tkinter.ttk import Style, Button

from gui import gui_logic


class MainScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.title("PyRestoManager")
        self.configure(background='gray')

        # Calculate screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 640) // 2
        y = (screen_height - 480) // 2
        self.geometry(f"640x480+{x}+{y}")

        # Create title label
        title_label = tk.Label(self, text="Welcome to PyRestoManager", fg="white", bg="gray",
                               font=("Calibri", 18))
        title_label.pack(pady=20)

        # Create buttons with styling
        button_style = Style()
        button_style.configure("MainButton.TButton", font=("Calibri", 12))

        burger_label = tk.Label(self, text="🍔", font=("Arial", 72), bg="gray")
        burger_label.pack(pady=20)

        login_button = Button(self, text="Login",style="MainButton.TButton", command=self.show_login)
        login_button.pack(pady=10)

        register_button = Button(self, text="Register",style="MainButton.TButton",   command=self.show_register)
        register_button.pack(pady=10)

        # Create display message label
        display_message = tk.Label(self, text="Elevate Your Restaurant Business!", fg="white", bg="grey",
                                   font=("Calibri", 15))
        display_message.pack(pady=20)

    def show_login(self):
        print("Login button clicked")

    def show_register(self):
        print("Register button clicked")

    def show_register(self):
        gui_logic.show_register_screen(self)


    def show_login(self):
        gui_logic.show_login_screen(self)

if __name__ == "__main__":
    app = MainScreen()
    app.mainloop()
