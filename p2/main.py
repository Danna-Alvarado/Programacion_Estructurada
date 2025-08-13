#Crear un proyecto  que permita  gestionar (administrar películas); colocar  un menu  de opciones para agregar, borrar,  modificar, consultar, buscar y vaciar películas 
#Notas: 
#1.-utiliza  funciones y mandar a llamar desde otro archivo 
#2.- Utilizar dict  para almacenar  los siguentes atrivutos (nombre, categoria, clasificacion, genero,idioama de la película, )
#In
import peliculas

opcion=True
while opcion:
    peliculas.borra_pantalla()
    print("\n\t..::: PELICULAS :::... \n..::: Sistema de Gestión de Peliculas :::...\n\n 1.- Crear \n 2.- Borrar \n 3.- Mostrar \n 4.- Buscar  \n 5.- Modificar \n 6.-Salir  ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearpeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarpeliculas()
            peliculas.esperarTecla() 
        case "3":
            peliculas.mostrarPeliculas()   
            peliculas.esperarTecla()
        case "4":
            peliculas.buscarPeliculas() 
            peliculas.esperarTecla() 
        case "5": 
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "6":
            opcion=False    
            print("Terminaste la ejecucion del SW")
            peliculas.borra_pantalla()
            print("/n\tTerminaste la ejecucion del SW")
        case _:
            opsion=True
            peliculas.esperarTecla()
            input("Opción invalida vuelva a intentarlo ... por favor")