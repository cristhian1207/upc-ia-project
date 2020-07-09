import mysql.connector

def get_connection():
  return mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'mysql', 
    database = 'project_ia',
    auth_plugin = 'mysql_native_password'
  )