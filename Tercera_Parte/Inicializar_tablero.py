import os


'''
BATALLA NAVAL
'''

def parametros_tablero():

    os.system("cls")

    ancho = int(input("\n <---> Ingrese el ancho del tablero: "))
    print("\n^")
    print("|")
    alto = int(input("v Ingrese el alto del tablero: "))

    os.system("cls")

    return ancho, alto


def inicializar_tablero(ancho, alto):

    tablero = []

    for i in range(alto):
        tablero.append([])
        for j in range(ancho):
            tablero[i].append("X")

    return tablero

def imprimir_tablero(tablero):

    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" ")
        print()


def main():

    ancho, alto = parametros_tablero()
    tablero = inicializar_tablero(ancho, alto)

    imprimir_tablero(tablero)

    print("\n\n")

    return tablero

main()