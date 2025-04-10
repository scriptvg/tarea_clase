def redondear_diccionario(diccionario):
    
    """
    Recibe un diccionario con valores decimales y devuelve un nuevo diccionario
    con los valores redondeados.
    """
    
    return {clave: round(valor) for clave, valor in diccionario.items()}

# Diccionario
diccionario = {
    "a": 1.2,
    "b": 2.5,
    "c": 3.7,
    "d": 4.4,
    "e": -1.8,
    "f": 0.0
}

print("Diccionario original:")
print(diccionario)

diccionario_redondeado = redondear_diccionario(diccionario)

print("\nDiccionario redondeado:")
print(diccionario_redondeado)