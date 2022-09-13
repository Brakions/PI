import mysql.connector
from configg import PASSWORD

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=PASSWORD,
  database="pi-1"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT driverId,driverRef FROM drivers WHERE driverId=30 LIMIT 1")

myresult3 = mycursor.fetchall()
for x in myresult3:
  print(x)