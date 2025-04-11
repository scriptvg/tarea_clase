# Lista de tuplas
personas = [("Juan", 25), ("Ana", 20), ("Luis", 30)]

# Ordenar por el segundo valor (edad)
personas_ordenadas = sorted(personas, key=lambda x: x[1])

# Imprimir el resultado
print(personas_ordenadas)