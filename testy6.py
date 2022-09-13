import mysql.connector
from configg import PASSWORD

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=PASSWORD,
  database="pi-1"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT r.driverId,SUM(points) as Total,nationality FROM drivers d INNER JOIN results r  ON d.driverId=r.driverId WHERE  nationality ='British' or nationality = 'American' GROUP BY r.driverId ORDER BY Total DESC LIMIT 1")

myresult6 = mycursor.fetchall()
for x in myresult6:
  print(x)