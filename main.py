from db.connection import get_connecction

def add_todo(title):
  conn = get_connecction()
  cursor = conn.cursor()

  sql = "INSERT INTO todos (title) VALUES (%s)"
  cursor.execute(sql, (title,))

  conn.commit()

  cursor.close()
  conn.close()

def show_todos():
  conn = get_connecction()
  cursor = conn.cursor()

  sql ="SELECT id, title, is_completed, created_at FROM todos"
  cursor.execute(sql)

  todos = cursor.fetchall()

  print("==== TODO LIST ====")
  for todo in todos:
    status = "✓" if todo[2] else ""
    print(f"[{status}] {todo[0]}: {todo[1]}")

  cursor.close()
  conn.close()

def main():
  add_todo("関数の変化")
  show_todos()

if __name__ == "__main__":
  main()