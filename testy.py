import mysql.connector
from configg import PASSWORD

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=PASSWORD,
  database="pi-1"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT year,count(date) as np FROM races GROUP BY year   ORDER BY np DESC LIMIT 1")

myresult = mycursor.fetchall()
for x in myresult:
  print(x)
