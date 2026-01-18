from db.connection import get_connecction

def main():
  conn = get_connecction()
  cursor = conn.cursor()

  sql = "INSERT INTO todos (title) VALUES (%s)"
  cursor.execute(sql, ("PythonでTODO作成",))

  conn.commit()

  print("TODO inserted")

  cursor.close()
  conn.close()


if __name__ == "__main__":
  main()