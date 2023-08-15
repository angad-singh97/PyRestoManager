from gui.gui import MainScreen


def start_app():  # Initialize database
    app = MainScreen()
    app.mainloop()

if __name__ == "__main__":
    start_app()
