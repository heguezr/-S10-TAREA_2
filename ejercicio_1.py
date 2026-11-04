
from herramientas import (
    imprimir_titulo,
    imprimir_info,
    imprimir_exito
)

imprimir_titulo("EJERCICIO · CONTAR APARICIONES")

lista = [1, 3, 2, 3, 4, 3, 5]
v = 3

# ---------------------- MANUAL ----------------------

count = 0

for x in lista:
    if x == v:
        count += 1

imprimir_info(f"Lista: {lista}")
imprimir_exito(f"{v} aparece {count} veces")


# ---------------------- PYTHONIC ----------------------

imprimir_titulo("SOLUCIÓN PYTHONIC")

imprimir_info(f"Lista: {lista}")
imprimir_exito(f"{v} aparece {lista.count(v)} veces")
