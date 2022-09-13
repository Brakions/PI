import mysql.connector
from configg import PASSWORD

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=PASSWORD,
  database="pi-1"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM circuits WHERE circuitId = 14")

myresult5 = mycursor.fetchall()
for x in myresult5:
  print(x)