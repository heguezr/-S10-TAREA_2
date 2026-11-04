from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:
    """Las mismas operaciones usando los métodos del list de Python."""

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):                      # ✅ resuelto
        if self.buscar(pasajero.numero) != -1:
            print("  ⚠ Ya existe ese número de pasajero")
            return False
        self.pasajeros.append(pasajero)
        return True

    def listar(self):                                 # ✅ resuelto
        if not self.pasajeros:
            print("  (lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"  [{i}] {p}")

    # ---------------- ✍ IMPLEMENTA (tabla 3.2 de la guía) ----------------
    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            print("  ⚠ Posición no válida")
            return False
        if self.buscar(pasajero.numero) != -1:
            print("  ⚠ Ya existe ese número de pasajero")
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    def buscar(self, numero):
        posiciones = [i for i, p in enumerate(self.pasajeros) if p.numero == numero]
        if posiciones:
            return posiciones[0]
        return -1

    def buscar_binaria(self, numero):
        numeros = [p.numero for p in self.pasajeros]
        posicion = bisect_left(numeros, numero)
        if posicion < len(numeros) and numeros[posicion] == numero:
            return posicion
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.pasajeros[pos].destino = nuevo_destino
        self.pasajeros[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            print("  ⚠ Posición no válida")
            return None
        return self.pasajeros.pop(posicion)

    def eliminar_por_valor(self, numero):
        encontrados = [p for p in self.pasajeros if p.numero != numero]
        if len(encontrados) == len(self.pasajeros):
            return False
        self.pasajeros = encontrados
        return True

    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.numero)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
        nueva = ListaPython()
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    def longitud(self):
        return len(self.pasajeros)

    def filtrar_por_destino(self, destino):
        return [p for p in self.pasajeros if p.destino.lower() == destino.lower()]

    def mayores_de_edad(self):
        return [p for p in self.pasajeros if p.es_mayor_de_edad()]