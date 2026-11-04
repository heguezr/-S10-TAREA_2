
from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython

from herramientas import (
    imprimir_titulo,
    imprimir_exito,
    imprimir_error,
    imprimir_info,
    imprimir_color
)

lista1 = MiLista(10)
lista2 = ListaPython()


# ------------------------- FUNCIONES DE APOYO -------------------------

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            imprimir_error("Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()

    return Pasajero(
        numero, nombre, cedula, edad,
        fecha, destino, asiento
    )


def cargar_datos_prueba(lista):
    lista.añadir(Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito", "12A"))
    lista.añadir(Pasajero(1002, "Ana", "0912345678", 28, "2026-11-15", "Lima", "03C"))
    lista.añadir(Pasajero(1009, "Luis", "0987654321", 35, "2026-11-20", "Bogotá", "18F"))
    lista.añadir(Pasajero(1004, "Beto", "0934567890", 16, "2026-11-20", "Quito", "07B"))
    lista.añadir(Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima", "01A"))

    imprimir_exito("Datos de prueba cargados")


def mostrar_opciones(titulo, extras=False):
    imprimir_titulo(titulo)

    imprimir_color(" 1. Añadir           2. Listar            3. Insertar en posición", "CYAN")
    imprimir_color(" 4. Buscar (lineal)  5. Buscar (binaria)  6. Modificar", "CYAN")
    imprimir_color(" 7. Eliminar por posición                 8. Eliminar por número", "CYAN")
    imprimir_color(" 9. Ordenar asc     10. Ordenar desc     11. Reversar", "CYAN")
    imprimir_color("12. Copiar          13. Longitud", "CYAN")

    if extras:
        imprimir_color("14. Filtrar por destino                  15. Mayores de edad", "CYAN")

    imprimir_color(" C. Cargar datos de prueba                0. Volver", "AMARILLO")


# ---------------------- MENÚ 1 · MiLista ----------------------

def menu_lista1():
    while True:
        mostrar_opciones("MENÚ 1 · MiLista")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()

            if lista1.añadir(pasajero):
                imprimir_exito("Pasajero añadido")

        elif op == "2":
            lista1.listar()

        elif op == "3":
            posicion = leer_entero("  Posición: ")
            pasajero = leer_pasajero()

            if lista1.insertar(posicion, pasajero):
                imprimir_exito("Pasajero insertado")

        elif op == "4":
            numero = leer_entero("  N.º a buscar: ")
            pos = lista1.buscar(numero)

            if pos == -1:
                imprimir_error("No existe")
            else:
                imprimir_info(
                    f"Encontrado en [{pos}]: {lista1.datos[pos].nombre}"
                )

        elif op == "5":
            numero = leer_entero("  N.º a buscar (lista ordenada): ")
            pos = lista1.buscar_binaria(numero)

            if pos == -1:
                imprimir_error("No existe (¿ordenaste la lista?)")
            else:
                imprimir_info(
                    f"Encontrado en [{pos}]: {lista1.datos[pos].nombre}"
                )

        elif op == "6":
            numero = leer_entero("  N.º a modificar: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()

            if lista1.modificar(numero, destino, asiento):
                imprimir_exito("Pasajero modificado")
            else:
                imprimir_error("No existe")

        elif op == "7":
            posicion = leer_entero("  Posición a eliminar: ")
            pasajero = lista1.eliminar_por_posicion(posicion)

            if pasajero is not None:
                imprimir_exito(f"Eliminado: {pasajero.nombre}")
            else:
                imprimir_error("No existe un pasajero en esa posición")

        elif op == "8":
            numero = leer_entero("  N.º a eliminar: ")

            if lista1.eliminar_por_valor(numero):
                imprimir_exito("Pasajero eliminado")
            else:
                imprimir_error("No existe")

        elif op == "9":
            lista1.ordenar_asc()
            imprimir_exito("Lista ordenada ascendentemente")

        elif op == "10":
            lista1.ordenar_desc()
            imprimir_exito("Lista ordenada descendentemente")

        elif op == "11":
            lista1.reversar()
            imprimir_exito("Lista reversada")

        elif op == "12":
            copia = lista1.copiar()
            imprimir_exito("Copia creada:")
            copia.listar()

        elif op == "13":
            imprimir_info(
                f"Cantidad de pasajeros: {lista1.longitud()}"
            )

        elif op == "C":
            cargar_datos_prueba(lista1)

        elif op == "0":
            break

        else:
            imprimir_error("Opción no válida")


# ---------------------- MENÚ 2 · LIST DE PYTHON ----------------------

def menu_lista2():
    while True:
        mostrar_opciones("MENÚ 2 · list de Python", extras=True)
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()

            if lista2.añadir(pasajero):
                imprimir_exito("Pasajero añadido")

        elif op == "2":
            lista2.listar()

        elif op == "3":
            posicion = leer_entero("  Posición: ")
            pasajero = leer_pasajero()

            if lista2.insertar(posicion, pasajero):
                imprimir_exito("Pasajero insertado")

        elif op == "4":
            numero = leer_entero("  N.º a buscar: ")
            pos = lista2.buscar(numero)

            if pos == -1:
                imprimir_error("No existe")
            else:
                imprimir_info(
                    f"Encontrado en [{pos}]: {lista2.pasajeros[pos].nombre}"
                )

        elif op == "5":
            numero = leer_entero("  N.º a buscar (lista ordenada): ")
            pos = lista2.buscar_binaria(numero)

            if pos == -1:
                imprimir_error("No existe (¿ordenaste la lista?)")
            else:
                imprimir_info(
                    f"Encontrado en [{pos}]: {lista2.pasajeros[pos].nombre}"
                )

        elif op == "6":
            numero = leer_entero("  N.º a modificar: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()

            if lista2.modificar(numero, destino, asiento):
                imprimir_exito("Pasajero modificado")
            else:
                imprimir_error("No existe")

        elif op == "7":
            posicion = leer_entero("  Posición a eliminar: ")
            pasajero = lista2.eliminar_por_posicion(posicion)

            if pasajero is not None:
                imprimir_exito(f"Eliminado: {pasajero.nombre}")
            else:
                imprimir_error("No existe un pasajero en esa posición")

        elif op == "8":
            numero = leer_entero("  N.º a eliminar: ")

            if lista2.eliminar_por_valor(numero):
                imprimir_exito("Pasajero eliminado")
            else:
                imprimir_error("No existe")

        elif op == "9":
            lista2.ordenar_asc()
            imprimir_exito("Lista ordenada ascendentemente")

        elif op == "10":
            lista2.ordenar_desc()
            imprimir_exito("Lista ordenada descendentemente")

        elif op == "11":
            lista2.reversar()
            imprimir_exito("Lista reversada")

        elif op == "12":
            copia = lista2.copiar()
            imprimir_exito("Copia creada:")
            copia.listar()

        elif op == "13":
            imprimir_info(
                f"Cantidad de pasajeros: {lista2.longitud()}"
            )

        elif op == "14":
            destino = input("  Destino a filtrar: ").strip()
            filtrados = lista2.filtrar_por_destino(destino)

            if not filtrados:
                imprimir_error("No hay pasajeros para ese destino")
            else:
                for pasajero in filtrados:
                    imprimir_color(str(pasajero), "CYAN")

        elif op == "15":
            mayores = lista2.mayores_de_edad()

            if not mayores:
                imprimir_error("No hay pasajeros mayores de edad")
            else:
                for pasajero in mayores:
                    imprimir_color(str(pasajero), "VERDE")

        elif op == "C":
            cargar_datos_prueba(lista2)

        elif op == "0":
            break

        else:
            imprimir_error("Opción no válida")


# ---------------------- MENÚ PRINCIPAL ----------------------

def main():
    while True:
        imprimir_titulo("TAREA LISTAS · PASAJEROS ✈")

        imprimir_color("1. Menú 1 · MiLista", "CYAN")
        imprimir_color("2. Menú 2 · list de Python", "CYAN")
        imprimir_color("3. Salir", "AMARILLO")

        op = input("\nOpción: ").strip()

        if op == "1":
            menu_lista1()

        elif op == "2":
            menu_lista2()

        elif op == "3":
            imprimir_exito("¡Hasta pronto!")
            break

        else:
            imprimir_error("Opción no válida")


if __name__ == "__main__":
    main()