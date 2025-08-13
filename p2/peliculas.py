import mysql
from  mysql.connector import Error
import mysql.connector
#dict u objeto para al,acenar los atrivutos( nombre, categoria, clasificacion, genero, idioma)

#pelicula=¨{
#      "nombre",
#      "categoria":"",
#     "clasificacion":"",
#        "genero":"",
#        "idioma":""
#}

pelicula={}


def borra_pantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t... Oprime  una tecla para continuar...")
    
def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas",
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es {e}")
        return None

def crearpeliculas():
    borra_pantalla()
    conexionbd=conectar()
    if conexionbd != None:
        print( "\n\t.:: Alta de Películas ::\n")
        pelicula.update({"nombre":input("Ingrese el nombre: ").upper ().strip ()})
        pelicula.update({"categoria":input("Ingrese la categoria: ").upper ().strip ()})
        pelicula.update({"clasificacion":input("Ingrese la clasificacion: ").upper ().strip ()})
        pelicula.update({"genero":input("Ingrese el genero: ").upper ().strip ()})
        pelicula.update({"idioma":input("Ingrese el idioma: ").upper ().strip ()})
        ##### SQL a BD
        cursor=conexionbd.cursor()
        sql="insert into peliculas (nombre, categoria, clasificacion, genero, idioma) values (%s, %s, %s, %s, %s)"
        val=(pelicula["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["categoria"])
        cursor.execute(sql,val)
        conexionbd.commit()
        print("\n\t.::¡LA OPERACION SE REALIZO CON EXITO!::.")


def mostrarPeliculas():
    borra_pantalla()
    print("\n\t.:: Consultar la  Película ::\n")
    if len(pelicula) > 0:
       for i in pelicula:
           print(f"\t{i}: {pelicula[i]}")
    else:
       print("\t.::No hay películas en el sistema.")

