import mysql.connector
from configg import PASSWORD

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=PASSWORD,
  database="pi-1"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT year,circuitId,count(circuitId) as veces FROM races GROUP BY circuitId ORDER BY veces DESC LIMIT 1")

myresult4 = mycursor.fetchall()
for x in myresult4:
  print(x)