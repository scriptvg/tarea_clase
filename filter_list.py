# filter_list.py

def filtrar_pares(numeros):
    """Filtra números pares de una lista."""
    return [x for x in numeros if x % 2 == 0]

if __name__ == "__main__":
    # Lista predefinida
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Lista original:", numeros)
    print("Lista de números pares:", filtrar_pares(numeros))

    # Lista ingresada por el usuario
    entrada = input("Ingresa una lista de números separados por comas: ")
    numeros_usuario = list(map(int, entrada.split(',')))
    print("Lista original ingresada:", numeros_usuario)
    print("Lista de números pares:", filtrar_pares(numeros_usuario))
