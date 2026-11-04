from herramientas import imprimir_titulo, imprimir_exito, imprimir_info

imprimir_titulo("EJERCICIO 4 · FUSIONAR LISTAS")

a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 10]

resultado = []

i = 0
j = 0

while i < len(a) and j < len(b):

    if a[i] <= b[j]:
        resultado.append(a[i])
        i += 1

    else:
        resultado.append(b[j])
        j += 1

resultado.extend(a[i:])
resultado.extend(b[j:])

imprimir_info(f"Lista A: {a}")
imprimir_info(f"Lista B: {b}")
imprimir_exito(f"Lista fusionada: {resultado}")