# Lista de palabras
palabras = ["manzana", "banana", "cereza", "durazno", "kiwi"]

# Usar map() para obtener las longitudes de las palabras
longitudes = list(map(len, palabras))

# Código de ejemplo movido al bloque principal
if __name__ == "__main__":
    print("Lista de palabras:", palabras)
    print("Longitudes de las palabras en la lista:", longitudes)

    # Pedir al usuario que ingrese una palabra
    palabra_usuario = input("Ingresa una palabra para saber su tamaño: ")
    print(f"El tamaño de la palabra '{palabra_usuario}' es: {len(palabra_usuario)}")