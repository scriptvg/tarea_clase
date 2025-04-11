"""
Este script ordena listas de números en orden descendente.
"""

def ordenar_descendente(lista):
    """Ordena una lista en orden descendente."""
    return sorted(lista, reverse=True)

if __name__ == "__main__":
    # Lista predefinida
    numeros = [5, 2, 9, 1, 7, 3]
    print(f"Lista original: {numeros}")
    print(f"Lista ordenada (descendente): {ordenar_descendente(numeros)}")

    # Solicitar lista al usuario
    entrada = input("Ingresa números separados por comas: ")
    numeros_usuario = [int(x.strip()) for x in entrada.split(",")]
    print(f"Tu lista: {numeros_usuario}")
    print(f"Tu lista ordenada (descendente): {ordenar_descendente(numeros_usuario)}")
