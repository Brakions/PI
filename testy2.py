import mysql.connector
from configg import PASSWORD

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=PASSWORD,
  database="pi-1"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT COUNT(r.driverId) as Veces,r.driverId,position FROM results r INNER JOIN drivers d ON d.driverId=r.driverId WHERE position =1 GROUP BY r.driverId ORDER BY Veces DESC LIMIT 1;")

myresult2 = mycursor.fetchall()
for x in myresult2:
  print(x)