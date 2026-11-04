from herramientas import imprimir_titulo, imprimir_exito, imprimir_info

imprimir_titulo("EJERCICIO 2 · NÚMEROS ÚNICOS")

numeros = [1, 3, 2, 3, 4, 1]
unicos = []

for numero in numeros:
    if numero not in unicos:
        unicos.append(numero)

imprimir_info(f"Lista original: {numeros}")
imprimir_exito(f"Números únicos: {unicos}")