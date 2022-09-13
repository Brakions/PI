from ensurepip import version
from http.client import HTTPException
from turtle import title
from fastapi import FastAPI
from fastapi import HTTPException

import mysql.connector

from testy import myresult
from testy2 import myresult2
from testy3 import myresult3
from testy4 import myresult4
from testy5 import myresult5
from testy6 import myresult6
from testy7 import myresult7

from configg  import PASSWORD



from database import database as connection
from database import User

from schemas import UsersRequestModel
from schemas import UsersResponseModel

app =FastAPI(title= "P.I",
                description=" Proyecto Individual",
                version=" 1.0.0")

@app.on_event("startup")
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([User])
    
@app.on_event("shutdown")
def shutdown():
    if not connection.is_closed():
        connection.close()


@app.get("/")
async def index ():
    return "Hello World"

@app.post("/users")
async def create_user(user_request: UsersRequestModel):
    user = User.create(
            username=user_request.username,
            email=user_request.email
    )
    return user_request

@app.get("/users({user_id})")
async def get_user(user_id):
    user =User.select().where(User.id==user_id).first()

    if user:
        return UsersResponseModel(id=user.id,
                                 username=user.username,
                                 email=user.email)
    else:
        return HTTPException(404,"User not found")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=PASSWORD,
  database="pi-1"
)
@app.get("/p1")
async def Año_con_más_carreras():

        return  ("Año con más carreras, veces"), myresult

@app.get("/p1.5")
async def Veces_driverid_Position():
        
        return "Veces driverid posicion",myresult2

@app.get("/p2")
async def Piloto_con_mayor_cantidad_de_primeros_puestos():
        
        return "driverid , Nombre",myresult3

@app.get("/p2.5")
async def Año_circuitoid_veces():
        
        return "Año, CircuitoID , Veces",myresult4

@app.get("/p3")
async def Nombre_del_circuito_más_corrido():
        
        return " CircuitoID , Nombre",myresult5

@app.get("/p3.5")
async def Driverid_Puntos_Total():
        
        return " Driverid ,Total de puntos,Nacionalidad ",myresult6

@app.get("/p4")
async def Piloto_con_mayor_cantidad_de_puntos_en_total_cuyo_constructor_sea_de_nacionalidad_sea_American_o_British():
        
        return " Piloto con mayor cantidad de puntos  ",myresult7





