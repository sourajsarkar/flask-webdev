import mysql.connector as c

conn = c.connect(
  host="localhost",
  user="root",
  passwd="toor"
)

if conn.is_connected():
  print("hello")
else:
  print("fucck")
mycursor = conn.cursor()
