"""
Este script ordena listas de números en orden descendente.
"""

# Lista predefinida
numeros = [5, 2, 9, 1, 7, 3]
print(f"Lista original: {numeros}")
print(f"Lista ordenada (descendente): {sorted(numeros, reverse=True)}")

# Solicitar lista al usuario
entrada = input("Ingresa números separados por comas: ")
numeros_usuario = [int(x.strip()) for x in entrada.split(",")]
print(f"Tu lista: {numeros_usuario}")
print(f"Tu lista ordenada (descendente): {sorted(numeros_usuario, reverse=True)}")
