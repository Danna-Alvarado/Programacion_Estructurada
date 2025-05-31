'''list (Array)
son colecciones o conjunto de datos/ valores bajo un mismo nombre, 
para acceder a los valores se hace con un indice numerico

nota: sus valores si son modificables

La lista es una colecion ordenada y modificable. Permite miembros duplicados.'''

#Funciones mas comunes en las listas.
import os

paises=["Mexico, España, Brasil, Canada"]
numeros=[23,45,24]
varios=["Hola", 3.1416,33,True]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)

#Recorrer la lista
#1er forma

for i in paises:
    print(i)
#2da forma
lista=""
for i in range (0,len(paises)):
    lista=lista+f"[{paises}]."
print,(lista)

for i in range (0,len(paises)):
    print(paises[i])

#ordenar elementos
paises.sort()
print(paises)
numeros.sort()
print(numeros)

#dar la vuelta a una lista
paises.reverse()
print(paises)
varios.reverse()
print(varios)
#Agregar, insertar, añadir un elemento a una lista
#1er forma
paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,"Honduras")
print(paises)

paises.sort()
print(paises)

#Eliminar, borrar, suprimir; un elemento de una lista
#1er forma

paises.pop(4)
print(paises)

#2da forma
paises.remove("Honduras")

#Buscar un elemento dentro de la lista
print(paises)

print("brasil" in paises)

#Contar el numero de veces que aparece un elemento dentro de una lista
print(numeros)

cuantos=numeros.count(23)
print(cuantos)

numeros.append(23)
cuantos=numeros.count(23)
print(cuantos)

#Conocer la posicion o indice en  el que se encuentra un elemento de la lista
paises.reverse()
paises.append("Canada")
print(paises)

posicion=paises.index("Canada")
print(f"El valor de canada lo encontro en la posicion:{posicion}")
{posicion}

#Unir el contenido de una lista dentro de otra

print(numeros)
numeros2=[100,200]

print(numeros2)

#crear a partir de las listas de numeros 1 y 2 una resultante y mostrar el contenido ordenado descendentemente

numeros.extend (numeros2)
print(numeros)

numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)

