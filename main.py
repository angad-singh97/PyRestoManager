from database.db_init import initialize_database
from database.db_init import sql_connection
from gui.main_app import start_app

# Initialize the database
initialize_database(sql_connection())

# Start the main screen
start_app()
