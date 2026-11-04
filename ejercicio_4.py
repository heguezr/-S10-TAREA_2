from herramientas import imprimir_titulo, imprimir_exito, imprimir_info

imprimir_titulo("EJERCICIO 3 · SEGUNDO MAYOR")

numeros = [5, 2, 9, 7, 9, 3]

mayor = float("-inf")
segundo = float("-inf")

for numero in numeros:
    if numero > mayor:
        segundo = mayor
        mayor = numero

    elif numero > segundo and numero < mayor:
        segundo = numero

imprimir_info(f"Lista original: {numeros}")
imprimir_exito(f"Mayor: {mayor}")
imprimir_exito(f"Segundo mayor: {segundo}")