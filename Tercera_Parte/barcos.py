import os

def pedir_barcos():
    '''
    Solicita al usuario la cantidad de barcos de cada tipo y devuelve una lista de sus longitudes junto con los tipos.
    '''
    os.system("cls")

    tipos_barcos = {"Porta avion": 0, "Submarino": 0, "Destructor": 0, "Lancha": 0}
    barcos = []

    print("Ingrese la cantidad de barcos de cada tipo:")

    for tipo, longitud in tipos_barcos.items():
        try:
            longitud = int(input(f"Largo de {tipo}: "))
            cantidad = int(input(f"{tipo} (longitud {longitud}): "))
            for _ in range(cantidad):
                barcos.append((tipo, longitud))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            return pedir_barcos()

    os.system("cls")
    return barcos

def imprimir_barcos_no_colocados(barcos_no_colocados):
    
    if barcos_no_colocados:
        print("No se pudieron colocar los siguientes barcos: \n")
        for tipo, cantidad in barcos_no_colocados.items():
            if (tipo in ["Porta avion", "Destructor"]) and cantidad > 1:
                print(f"{cantidad} {tipo}es")
            elif (tipo in ["Submarino", "Lancha"]) and cantidad > 1:
                print(f"{cantidad} {tipo}s")
            else:
                print(f"{cantidad} {tipo}")
    else:
        print("¡Todos los barcos fueron colocados exitosamente!")
        print("\n")

