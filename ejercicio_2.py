from herramientas import imprimir_titulo, imprimir_exito, imprimir_info

imprimir_titulo("EJERCICIO 1 · INVERTIR LISTA")

lista = [1, 2, 3, 4, 5]
invertida = []

for i in range(len(lista) - 1, -1, -1):
    invertida.append(lista[i])

imprimir_info(f"Lista original: {lista}")
imprimir_exito(f"Lista invertida: {invertida}")