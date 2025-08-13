agregar_contactos{}
def borrarpantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("Presione enter para continuar")

def menuprincipal():
    borrarpantalla()
    opcion=input("Ingrese la opcion")

def agregar_contacto(agenda):
    borrarpantalla()
    print("Agregar Contactos")
    if nombre in agenda:
        print("Este contacto ya existe")
    else:
        nombre=input("Nombre: ").upper() .strip()
        tel=input("Telefono: ").upper() .strip()
        email=input("Email: ") .upper() .strip()
        print("Accion realizada con exito")

def buscar_contacto():
    borrarpantalla()
    print("Buscar contactos")
    if not agenda_contactos:
        print("No hay contactos")
    else:
        nombre=input("Nombre del contacto a buscar") .upper() .strip()
        if nombre in agenda_contactos:
            print (f"{'Nombre':<15} {'# Telefono':<15} {"E-mail":<10}")
            print (f"-"*60)
            print(f"{"Nombre":>15} {agenda_contactos[nombre][0]} {agenda_contactos[nombre][1]:>10}")
            print (f"-"*60)
        else:
            print("El contacto no existe")

def modificaratributos():
    borrarpantalla()
    print("Modificar contactos")
    if not agenda_contactos:
        print("No hay contactos")
    else:
        nombre=input("Nombre del contacto a modificar") .upper() .strip()
        if nombre in agenda_contactos:
            print(f"Nombre: {nombre}\n\t Telefono:{agenda_contactos[nombre][0]}\n\t{agenda_contactos[nombre][1]}")
            print (f"-"*60)
            resp=input("Desea modificar?").lower() .strip()
            if resp=="si":
                tel=input("Telefono:").upper() .strip()
                email=input("E-mail:").upper() .strip()
                agenda_contactos[nombre]=tel,email
        else:
            print("El contacto no existe")

def eliminarContacto(agenda_contactos):
    borrarpantalla()
    print("Eliminar contactos")
    if not agenda_contactos:
        print("No hay contactos")
    else:
        nombre=input("Nombre del contacto a modificar") .upper() .strip()
        if nombre in agenda_contactos:
            print(f"Nombre: {nombre}\n\t Telefono:{agenda_contactos[nombre][0]}\n\t{agenda_contactos[nombre][1]}")
            resp=input("desea eliminar el contacto?")
            if resp=="si":
                agenda_contactos.pop(nombre)
        else:
            print("Este contacto no existe")





