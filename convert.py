# Lista de temperaturas en grados Celsius
temperaturas_celsius = [0, 20, 30, 40, 100]

# Conversión de Celsius a Fahrenheit usando map
temperaturas_fahrenheit = list(map(lambda c: c * 9/5 + 32, temperaturas_celsius))

# Imprimir resultados
print("Temperaturas en Celsius:", temperaturas_celsius)
print("Temperaturas en Fahrenheit:", temperaturas_fahrenheit)