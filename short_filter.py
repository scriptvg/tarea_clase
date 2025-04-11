# Lista de palabras
palabras = ["casa", "elefante", "sol", "montaña", "luz", "programación"]

# Filtrar palabras con 5 o más letras
palabras_largas = list(filter(lambda palabra: len(palabra) >= 5, palabras))

# Imprimir el resultado
print(palabras_largas)