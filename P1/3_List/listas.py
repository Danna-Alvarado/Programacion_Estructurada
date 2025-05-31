#crear una lista de numeros e imprmir el contenido
numeros=[1,2,3,4,5,6,7,8,9,]
print(numeros)

lista=""
for i in numeros:
    lista+=f"{i}"
print(f"{lista}]")

lista="["
for i in range (0,len(numeros)):
    lista+=f"{numeros[i]}"
print(f"{lista}]")

lista="["
while i<len(numeros):
     lista+=f"{numeros[i]}"
print(f"{lista}]")

#crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
palabras=["casa","gato","Cubo","computadora"]

palabra_buacar=input("Dame la palabra buscar: ")
if palabra_buacar in palabras:
    print("Si se encontro la palabra en la lista")
else:
    print("No se encontro la palabra en la lista")



econtro=False
posicion=[]
for i in range(0,len(palabras)):
    if palabras[i]==palabra_buacar:
        encontro=True
        posicion.append(i)
if encontro:
    print("Si se encontro la palabra en la lista")
else:
    print("No se encontro la palabra en la lista")

#Añadir elementos a la lista
palabras.append("Animal","Microfono")
while opc=="si":
    palabras.append(float(input("Dame un numero entero o decimal")))
    opc=input("¿Desear agregar otro numero a la list?(si/no)").lower
    

#Crear una lista multidimencional que permita almacenar el nombre y telefono de una agenda

agenda=[
        ["Carlos","6181234567"],
        ["Alberto","6671234567"],
        ["Martin","6785678923"]
       ]

print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])    

cadena=""
for r in range(0,3):
    for c in range(0,2):
      cadena+=f"{agenda[r][c]}, "
    cadena+="\n"     
print(cadena) 