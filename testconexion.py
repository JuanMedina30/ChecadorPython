#Estas librerias son meramente estéticas, el programa puede funcionar sin ellas
import os #os es el modulo que permite limpiar la pantalla
import msvcrt  
from datetime import datetime
import pyodbc 
import pandas as pd

#Conexion a SQL server

#server='JUANMEDINA\SQLEXPRESS'#El nombre del servidor
server='JUANMEDINA'#El nombre del servidor
bd='ChecadorPython'#El nombre de la base de datos
#Aqui se creo un usuario para acceder a SQL server, asi mismo el usuario se crea desde SQL
user='User'#Usuario creado
password='admin'#Contraseña creado
#La conexion puede llegar a fallar, por eso se le complementa con un try
try:
    #Codigo que funge como conector, en el mismo se llama a un "driver"
    #conector = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+bd+';UID='+user+';PWD='+ password)
    conector = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+bd+';UID='+user+';PWD='+password+';TrustServerCertificate=yes')
    print("Conexion exitosa")#Mensaje a desplegar si la conexion fue exitosa
except Exception as e:
    print(f"La conexion ha fallado. Error: {e}") 

