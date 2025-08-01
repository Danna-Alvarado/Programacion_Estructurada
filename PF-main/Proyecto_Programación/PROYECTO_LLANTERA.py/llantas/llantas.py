from conexionBD_llantas import *

def agregar_llanta(usuario_id):
    import funciones  # para usar borrar_pantalla y esperar_tecla
    funciones.borrar_pantalla()
    print("\n\t\t\t ✩ ✩ ✩ AGREGAR LLANTA ✩ ✩ ✩ \n")

    # Marca
    marcas = {
        "1": "Michelin",
        "2": "Goodyear",
        "3": "Bridgestone",
        "4": "Continental",
        "5": "Pirelli",
        "6": "Yokohama",
        "7": "Dunlop",
        "8": "BFGoodrich"
    }
    while True:
        for k, v in marcas.items():
            print(f"\t{k}.- {v}")
        marca = input("\n\tSeleccione la marca de la llanta: ").strip()
        if marca in marcas:
            marca = marcas[marca]
            break
        else:
            print("\n\tOpción inválida, intente otra vez.")

    # Tipo
    tipos = {
        "1": "M/T (Mud Terrain)",
        "2": "A/T (All Terrain)",
        "3": "H/T (Highway Terrain)"
    }
    while True:
        for k, v in tipos.items():
            print(f"\t{k}.- {v}")
        tipo = input("\n\tIngrese el tipo de llanta (1-3): ").strip()
        if tipo in tipos:
            tipo = tipos[tipo]
            break
        else:
            print("\n\tOpción inválida, intente otra vez.")

    # Medida según tipo
    medidas_por_tipo = {
        "M/T (Mud Terrain)": {
            "1": "285/75/R16",
            "2": "315/70/R17",
            "3": "33x12.50/R15",
            "4": "35x12.50/R17"
        },
        "A/T (All Terrain)": {
            "1": "245/70/R16",
            "2": "265/70/R17",
            "3": "275/65/R18",
            "4": "285/70/R17"
        },
        "H/T (Highway Terrain)": {
            "1": "185/65/R15",
            "2": "195/60/R15",
            "3": "205/55/R16",
            "4": "215/50/R17",
            "5": "215/75/R15",
            "6": "225/70/R16",
            "7": "235/70/R16",
            "8": "255/50/R20"
        }
    }
    while True:
        print("\n\tSeleccione la medida de la llanta:")
        opciones_medidas = medidas_por_tipo[tipo]
        for k, v in opciones_medidas.items():
            print(f"\t{k}.- {v}")
        medida = input("\n\tIngrese la opción de medida: ").strip()
        if medida in opciones_medidas:
            medida = opciones_medidas[medida]
            break
        else:
            print("\n\tOpción inválida, intente otra vez.")

    # Desgaste
    desgastes = {
        "1": "Nueva",
        "2": "Seminueva",
        "3": "Usada",
        "4": "Dañada (Para desecho)"
    }
    while True:
        for k, v in desgastes.items():
            print(f"\t{k}.- {v}")
        desgaste = input("\n\tSeleccione el estado de la llanta (1-4): ").strip()
        if desgaste in desgastes:
            desgaste = desgastes[desgaste]
            break
        else:
            print("\n\tOpción inválida, intente otra vez.")

    # Cantidad
    while True:
        try:
            cantidad = int(input("\n\tTeclee la cantidad de llantas que desea agregar: "))
            if cantidad > 0:
                break
            else:
                print("\n\tLa cantidad debe ser mayor a 0.")
        except ValueError:
            print("\n\tIngrese un número entero válido.")

    # Precio
    while True:
        try:
            precio = float(input("\n\tIngrese el precio de la llanta: "))
            if precio > 0:
                break
            else:
                print("\n\tEl precio debe ser mayor a 0.")
        except ValueError:
            print("\n\tIngrese un valor numérico válido.")

    # Guardar en BD
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO llantas (usuario_id, marca, categoria, medida, estado, precio, cantidad)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (usuario_id, marca, tipo, medida, desgaste, precio, cantidad))
        conexion.commit()
        print("\n\tLlanta agregada correctamente.")
    except Exception as e:
        print("\n\tError al agregar la llanta:", e)
    finally:
        cursor.close()
        funciones.esperar_tecla()


def mostrar_llantas(usuario_id):
    import funciones
    funciones.borrar_pantalla()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id, marca, categoria, medida, estado, precio, cantidad
            FROM llantas WHERE usuario_id = %s
        """, (usuario_id,))
        filas = cursor.fetchall()
        if filas:
            print("\n\t✩✩✩ LISTA DE LLANTAS ✩✩✩\n")
            for fila in filas:
                print(f"\tID: {fila[0]}, Marca: {fila[1]}, Tipo: {fila[2]}, Medida: {fila[3]}, Estado: {fila[4]}, Precio: ${fila[5]}, Cantidad: {fila[6]}")
        else:
            print("\n\tNo hay llantas registradas para este usuario.")
    except Exception as e:
        print("\n\tError al obtener llantas:", e)
    finally:
        cursor.close()
        funciones.esperar_tecla()


def buscar_llanta(usuario_id):
    import funciones
    funciones.borrar_pantalla()
    medida_buscar = input("\n\tIngrese la medida de la llanta a buscar: ").strip()

    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id, marca, categoria, medida, estado, precio, cantidad
            FROM llantas
            WHERE usuario_id = %s AND medida = %s
        """, (usuario_id, medida_buscar))
        filas = cursor.fetchall()

        if filas:
            print("\n\t✩✩✩ RESULTADOS DE LA BÚSQUEDA ✩✩✩\n")
            for fila in filas:
                print(f"\tID: {fila[0]}, Marca: {fila[1]}, Tipo: {fila[2]}, Medida: {fila[3]}, Estado: {fila[4]}, Precio: ${fila[5]}, Cantidad: {fila[6]}")
        else:
            print("\n\tNo se encontraron llantas con esa medida.")
    except Exception as e:
        print("\n\tError al buscar llantas:", e)
    finally:
        cursor.close()
        funciones.esperar_tecla()


def eliminar_llanta(usuario_id):
    import funciones
    funciones.borrar_pantalla()

    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id, marca, categoria, medida, estado, precio, cantidad
            FROM llantas WHERE usuario_id = %s
        """, (usuario_id,))
        filas = cursor.fetchall()

        if not filas:
            print("\n\tNo hay llantas para eliminar.")
            funciones.esperar_tecla()
            return

        print("\n\t✩✩✩ INVENTARIO DE LLANTAS ✩✩✩\n")
        for fila in filas:
            print(f"\tID: {fila[0]}, Marca: {fila[1]}, Tipo: {fila[2]}, Medida: {fila[3]}, Estado: {fila[4]}, Precio: ${fila[5]}, Cantidad: {fila[6]}")

        while True:
            try:
                id_eliminar = int(input("\n\tIngrese el ID de la llanta a eliminar: "))
                llanta = None
                for fila in filas:
                    if fila[0] == id_eliminar:
                        llanta = fila
                        break
                if llanta is None:
                    print("\n\tID no válido, intente de nuevo.")
                    continue
                break
            except ValueError:
                print("\n\tDebe ingresar un número válido.")

        while True:
            try:
                cantidad_eliminar = int(input(f"\n\tIngrese la cantidad a eliminar (máximo {llanta[6]}): "))
                if 0 < cantidad_eliminar <= llanta[6]:
                    break
                else:
                    print("\n\tCantidad inválida, intente de nuevo.")
            except ValueError:
                print("\n\tDebe ingresar un número válido.")

        if cantidad_eliminar == llanta[6]:
            # Eliminar la fila completa
            cursor.execute("DELETE FROM llantas WHERE id = %s", (id_eliminar,))
            print(f"\n\tSe eliminaron {cantidad_eliminar} llanta(s).")
        else:
            # Actualizar la cantidad
            nueva_cantidad = llanta[6] - cantidad_eliminar
            cursor.execute("UPDATE llantas SET cantidad = %s WHERE id = %s", (nueva_cantidad, id_eliminar))
            print(f"\n\tSe eliminaron {cantidad_eliminar} llanta(s). Quedan {nueva_cantidad}.")

        conexion.commit()
    except Exception as e:
        print("\n\tError al eliminar llantas:", e)
    finally:
        cursor.close()
        funciones.esperar_tecla()
