import tkinter as tk

from gui import gui_logic


class MainScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Screen")
        self.geometry("640x480+200+200")
        self.configure(background='grey')
        self.title("PyRestoManager")

        tk.Label(text="PyRestoManager", fg="white", bg="grey", width="900", height="2",
              font=("Calibri", 14)).pack()

        tk.Button(self, text="Login", command=self.show_login).pack()
        tk.Button(self, text="Register", command=self.show_register).pack()

    def show_register(self):
        gui_logic.show_register_screen(self)


    def show_login(self):
        gui_logic.show_login_screen(self)

if __name__ == "__main__":
    app = MainScreen()
    app.mainloop()
