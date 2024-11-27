import os

def pedir_barcos():
    
    """
    Solicita al usuario la cantidad de barcos de cada tipo y devuelve una lista de sus longitudes.
    """
    os.system("cls")

    tipos_barcos = {"Portaaviones": 4, "Submarino": 3, "Destructor": 2, "Lancha": 1}
    barcos = []

    print("Ingrese la cantidad de barcos de cada tipo:")

    for tipo, longitud in tipos_barcos.items():

        try:

            longitud = int(input(f"Largo de {tipo}: "))
            cantidad = int(input(f"{tipo} (longitud {longitud}): "))
            barcos.extend([longitud] * cantidad)

        except ValueError:

            print("Por favor, ingrese un número válido.")

            return pedir_barcos()

    os.system("cls")
    return barcos
