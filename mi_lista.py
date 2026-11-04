from pasajero import Pasajero


class MiLista:
    """Lista construida a mano sobre un arreglo de tamaño fijo.
    datos     -> [p1, p2, p3, None, None, ...]
    capacidad -> total de cajones     cantidad -> cajones ocupados
    ⛔ Sin append, insert, pop, remove, sort, reverse, copy, len, in, slicing.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def añadir(self, pasajero):                      # ✅ resuelto
        if self.cantidad == self.capacidad:
            print("  ⚠ La lista está llena")
            return False
        if self.buscar(pasajero.numero) != -1:
            print("  ⚠ Ya existe ese número de pasajero")
            return False
        self.datos[self.cantidad] = pasajero          # primer cajón libre
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ resuelto
        if self.cantidad == 0:
            print("  (lista vacía)")
            return
        for i in range(self.cantidad):
            print(f"  [{i}] {self.datos[i]}")

    # ---------------- ✍ IMPLEMENTA (tabla 3.1 de la guía) ----------------
    def insertar(self, posicion, pasajero):
        if self.cantidad == self.capacidad:
            print("  ⚠ La lista está llena")
            return False
        if posicion < 0 or posicion > self.cantidad:
            print("  ⚠ Posición no válida")
            return False
        if self.buscar(pasajero.numero) != -1:
            print("  ⚠ Ya existe ese número de pasajero")
            return False

        i = self.cantidad
        while i > posicion:
            self.datos[i] = self.datos[i - 1]
            i = i - 1
        self.datos[posicion] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    def buscar(self, numero):
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i
        return -1

    def buscar_binaria(self, numero):
        izq = 0
        der = self.cantidad - 1
        while izq <= der:
            medio = (izq + der) // 2
            if self.datos[medio].numero == numero:
                return medio
            elif self.datos[medio].numero < numero:
                izq = medio + 1
            else:
                der = medio - 1
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            print("  ⚠ Posición no válida")
            return None
        pasajero = self.datos[posicion]
        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1
        return pasajero

    def eliminar_por_valor(self, numero):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.eliminar_por_posicion(pos)
        return True

    def ordenar_asc(self):
        n = self.cantidad
        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].numero > self.datos[i + 1].numero:
                    aux = self.datos[i]
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = aux

    def ordenar_desc(self):
        n = self.cantidad
        for vuelta in range(n - 1):
            for i in range(n - 1 - vuelta):
                if self.datos[i].numero < self.datos[i + 1].numero:
                    aux = self.datos[i]
                    self.datos[i] = self.datos[i + 1]
                    self.datos[i + 1] = aux

    def reversar(self):
        izq = 0
        der = self.cantidad - 1
        while izq < der:
            aux = self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der] = aux
            izq = izq + 1
            der = der - 1

    def copiar(self):
        nueva = MiLista(self.capacidad)
        for i in range(self.cantidad):
            nueva.añadir(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad