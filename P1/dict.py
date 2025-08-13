"""
dict.- 
Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las 
listas indices numericos tiene alfanumericos. Es decir es algo parecido como los Objetos 

Tambien se conoce como un arreglo asosiativo u Objeto JSON

El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
"""
import os
os.system("cls")

paises=["Mexico","Brasil","Canada","España",]

pais1={"nombre":"México",
        "Capital":"CDMX",
        "poblacion": 120000,
        "Idioma":"Español",
        "status": True
        }

pais2={"nombre":"Brasil",
        "Capital":"Brasilia",
        "poblacion": 1400000,
        "Idioma":"Portugues",
        "status": True
        }

pais3={"nombre":"Canada",
        "Capital":"Ottawa",
        "poblacion": 1000000,
        "Idioma":["Ingles","Frances"],
        "status": True
        }
print(pais1)
for valores in pais1:
    print(pais1[valores])
