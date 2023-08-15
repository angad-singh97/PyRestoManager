import sqlite3
 
from sqlite3 import Error
 

def sql_table(con):
 
    cursorObj = con.cursor()
    
    cursorObj.execute("CREATE TABLE IF NOT EXISTS  restos(id INTEGER PRIMARY KEY,name TEXT NOT NULL,menucount INTEGER NOT NULL,emplcount INTEGER NOT NULL)")
    
    cursorObj.execute("CREATE TABLE IF NOT EXISTS user_logins(username text PRIMARY KEY, password text)")
 
    con.commit()
    
  
 
con = sql_connection()
 
sql_table(con)