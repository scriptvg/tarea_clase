# filter_list.py

# Filtrar números pares de una lista
def filtrar_pares(numeros):
    return [x for x in numeros if x % 2 == 0]

# Usar una lista predefinida y mostrar la vista de la lista original y la filtrada
def procesar_lista_predefinida():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista predefinida
    print("Lista original:", numeros)
    print("Lista de números pares:", filtrar_pares(numeros))

# Usar una lista ingresada por el usuario y mostrar la vista de la lista original y la filtrada
def procesar_lista_usuario():
    entrada = input("Ingresa una lista de números separados por comas: ")
    numeros = list(map(int, entrada.split(',')))  # Convertir la entrada en una lista de enteros
    print("Lista original ingresada:", numeros)
    print("Lista de números pares:", filtrar_pares(numeros))

# Ejecutar las funciones principales
if __name__ == "__main__":
    procesar_lista_predefinida()
    procesar_lista_usuario()
