import mysql.connector
from configg import PASSWORD

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=PASSWORD,
  database="pi-1"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM drivers WHERE driverId = 18")

myresult7 = mycursor.fetchall()
for x in myresult7:
  print(x)