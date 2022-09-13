from enum import unique
from unittest.util import _MAX_LENGTH
from peewee import*
from configg import PASSWORD

database = MySQLDatabase(
    "pi-1",
    user="root",password=PASSWORD,
    host="localhost" , port=3306
)

#Crear un nuevo modelo

class User(Model): 
    username = CharField(max_length=50,unique=True)
    email = CharField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        database= database
        table_name = "users"