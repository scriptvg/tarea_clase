# ===========================  =========================== #

from colorama import Fore, Style, init
from tamano_palabra import palabras, longitudes
from dic_redondear import redondear_diccionario
from convert_mayus import convertir_a_mayusculas
from filter_list import filtrar_pares

# Inicializar colorama
init(autoreset=True)

# ===========================
# Funciones auxiliares
# ===========================
def mostrar_menu(titulo, opciones):
    """Muestra un menú con un título y opciones numeradas."""
    print(f"\n{Style.BRIGHT}{Fore.MAGENTA}╔════════════════════════════════════════╗")
    print(f"{Fore.MAGENTA}║ {Fore.YELLOW}{titulo.center(40)} {Fore.MAGENTA}║")
    print(f"{Fore.MAGENTA}╚════════════════════════════════════════╝")
    for i, opcion in enumerate(opciones, 1):
        print(f"{Fore.CYAN}║ {Fore.YELLOW}{i}. {Fore.WHITE}{opcion.ljust(30)} {Fore.CYAN}║")
    print(f"{Fore.CYAN}╚════════════════════════════════╝")
    return input(f"{Fore.GREEN}Elige una opción: {Fore.WHITE}")

def mostrar_lista(lista, titulo="Lista"):
    """Muestra una lista con formato."""
    print(f"\n{Fore.CYAN}{titulo}:")
    for i, item in enumerate(lista, 1):
        print(f"  {Fore.YELLOW}{i}. {Fore.WHITE}{item}")

def mostrar_diccionario(diccionario, titulo="Diccionario"):
    """Muestra un diccionario con formato."""
    print(f"\n{Fore.CYAN}{titulo}:")
    for clave, valor in diccionario.items():
        print(f"  {Fore.YELLOW}{clave}: {Fore.WHITE}{valor}")

# ===========================
# Submenús
# ===========================
def submenu_palabras():
    while True:
        choice = mostrar_menu("Operaciones con palabras", [
            "Convertir palabras a mayúsculas",
            "Ver ejemplo con lista predefinida",
            "Volver al menú principal"
        ])
        if choice == "1":
            entrada = input(f"\n{Fore.GREEN}Introduce palabras en minúsculas separadas por comas: {Fore.WHITE}")
            palabras_lista = [palabra.strip() for palabra in entrada.split(",")]
            palabras_mayus = convertir_a_mayusculas(palabras_lista)
            mostrar_lista([f"{original} → {mayus}" for original, mayus in zip(palabras_lista, palabras_mayus)], "Palabras en mayúsculas")
        elif choice == "2":
            mostrar_lista(palabras, "Lista de palabras")
            mostrar_lista([f"{palabra}: {longitud} caracteres" for palabra, longitud in zip(palabras, longitudes)], "Longitudes de las palabras")
        elif choice == "3":
            break
        else:
            print(f"{Fore.RED}Opción no válida. Intenta de nuevo.")

def submenu_diccionarios():
    while True:
        choice = mostrar_menu("Operaciones con diccionarios", [
            "Redondear valores de un diccionario",
            "Ver ejemplo con diccionario predefinido",
            "Volver al menú principal"
        ])
        if choice == "1":
            diccionario = {}
            print(f"{Fore.CYAN}Ingrese valores para las claves (Enter para usar valores por defecto):")
            for clave in ['a', 'b', 'c', 'd', 'e', 'f']:
                valor = input(f"{Fore.GREEN}Valor para {Fore.YELLOW}{clave} {Fore.GREEN}[0.0]: {Fore.WHITE}")
                diccionario[clave] = float(valor) if valor else 0.0
            mostrar_diccionario(diccionario, "Diccionario original")
            mostrar_diccionario(redondear_diccionario(diccionario), "Diccionario redondeado")
        elif choice == "2":
            diccionario = {"a": 1.2, "b": 2.5, "c": 3.7, "d": 4.4, "e": -1.8, "f": 0.0}
            mostrar_diccionario(diccionario, "Diccionario original")
            mostrar_diccionario(redondear_diccionario(diccionario), "Diccionario redondeado")
        elif choice == "3":
            break
        else:
            print(f"{Fore.RED}Opción no válida. Intenta de nuevo.")

def submenu_listas():
    while True:
        choice = mostrar_menu("Operaciones con listas", [
            "Filtrar números pares de una lista",
            "Ver ejemplo con lista predefinida",
            "Volver al menú principal"
        ])
        if choice == "1":
            entrada = input(f"\n{Fore.GREEN}Ingresa una lista de números separados por comas: {Fore.WHITE}")
            numeros = list(map(int, entrada.split(',')))
            mostrar_lista(numeros, "Lista original")
            mostrar_lista(filtrar_pares(numeros), "Números pares")
        elif choice == "2":
            lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            mostrar_lista(lista, "Lista original")
            mostrar_lista(filtrar_pares(lista), "Números pares")
        elif choice == "3":
            break
        else:
            print(f"{Fore.RED}Opción no válida. Intenta de nuevo.")

# ===========================
# Menú principal
# ===========================
def main():
    while True:
        choice = mostrar_menu("Menú Principal", [
            "Operaciones con palabras",
            "Operaciones con diccionarios",
            "Operaciones con listas",
            "Salir"
        ])
        if choice == "1":
            submenu_palabras()
        elif choice == "2":
            submenu_diccionarios()
        elif choice == "3":
            submenu_listas()
        elif choice == "4":
            print(f"{Fore.RED}Saliendo del programa...")
            break
        else:
            print(f"{Fore.RED}Opción no válida. Intenta de nuevo.")

# ===========================
# Punto de entrada
# ===========================
if __name__ == "__main__":
    main()
