import agenda
def main():
    agenda_contactos={}
    opcion=True
    while opcion:
        agenda.borrarpantalla()
        opcion=agenda.menuprincipal()
        if opcion=="1":
            agenda.agregar_contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion=="2":
            agenda.mostrar_contactos(agenda_contactos)
            agenda.esperarTecla()
        elif opcion=="3":
            agenda.buscar_contacto(agenda_contactos)
            agenda.esperarTecla()
        elif opcion=="4":
            agenda.borrarpantalla()
            print("🖐️ Programa Finalizado")
            opcion=False
        elif opcion=="6":
            agenda.borrarpantalla()
            agenda.eliminarContacto()
        elif opcion=="7":
            agenda.modificaratributos()

        else:
            print("Ingrese una opcion valida")

