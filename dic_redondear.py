def redondear_diccionario(diccionario):
    """Redondea los valores de un diccionario."""
    return {clave: round(valor) for clave, valor in diccionario.items()}

if __name__ == "__main__":
    diccionario = {
        "a": 1.2,
        "b": 2.5,
        "c": 3.7,
        "d": 4.4,
        "e": -1.8,
        "f": 0.0
    }
    print("Diccionario original:", diccionario)
    print("Diccionario redondeado:", redondear_diccionario(diccionario))