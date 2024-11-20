import os


#BATALLA NAVAL

def pedir_barcos(ancho, alto):
    os.system("cls")

    diccionario_barcos = {"Portaaviones": 4, "Submarino": 3, "Destructor": 2, "lancha": 1}

    # Pedir cantidad de barcos de cada tipo
    for barco in diccionario_barcos:

        cantidad_cada_barco = int(input("\n\nIngrese la cantidad de barcos de tipo " + barco + " que desea: "))

        diccionario_barcos[barco] = cantidad_cada_barco

    # Imprimir cantidad de barcos de cada tipo
    for barco in diccionario_barcos:
        print(f"\nBarcos de tipo {barco}: {diccionario_barcos[barco]}")

    

    input("\n\nPresione enter para continuar...")

    os.system("cls")
    return 

pedir_barcos(10, 10)