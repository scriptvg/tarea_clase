# Función para convertir una lista de palabras a mayúsculas
def convertir_a_mayusculas(palabras):
    """Convierte una lista de palabras a mayúsculas."""
    return [palabra.upper() for palabra in palabras]

# Ejemplo con una lista predeterminada
def ejemplo_lista_predeterminada():
    palabras = ["hola", "mundo", "python"]
    print("Lista predeterminada:", palabras)
    print("Conversión a mayúsculas:", convertir_a_mayusculas(palabras))

# Solicitar lista al usuario y procesarla
def procesar_lista_usuario():
    entrada = input("\nIntroduce palabras en minúsculas separadas por comas: ")
    palabras = [palabra.strip() for palabra in entrada.split(",")]

    if all(palabra.islower() for palabra in palabras):
        print("Lista ingresada:", palabras)
        print("Conversión a mayúsculas:", convertir_a_mayusculas(palabras))
    else:
        print("Error: Todas las palabras deben estar en minúsculas.")

# Ejecución del programa
if __name__ == "__main__":
    palabras = ["hola", "mundo", "python"]
    print("Lista predeterminada:", palabras)
    print("Conversión a mayúsculas:", convertir_a_mayusculas(palabras))

    entrada = input("\nIntroduce palabras en minúsculas separadas por comas: ")
    palabras_usuario = [palabra.strip() for palabra in entrada.split(",")]
    print("Conversión a mayúsculas:", convertir_a_mayusculas(palabras_usuario))
