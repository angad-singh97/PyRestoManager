from database.sql_operations.register_sql_operations import register_user_sql


def registerUser(username, password):
    username_info = username.get()
    password_info = password.get()
    success = register_user_sql(username_info, password_info)
    if success:
        return True
    else:
        return False



