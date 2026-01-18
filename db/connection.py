import mysql.connector

def get_connecction():
  return mysql.connector.connect(
    host = "localhost",
    user = "fuku", #mysqlのルートユーザー
    password = "6954", #mysqlのルートユーザーのpw
    database = "todo_db"
    )
