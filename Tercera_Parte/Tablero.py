def parametros_tablero():

    """
    Solicita las dimensiones del tablero al usuario.
    """

    ancho = int(input("Ingrese el ancho del tablero: "))
    alto = int(input("Ingrese el alto del tablero: "))

    return ancho, alto


def inicializar_tablero(ancho, alto):

    """
    Crea un tablero vacío con dimensiones dadas.
    """

    return [[0 for _ in range(ancho)] for _ in range(alto)]


def imprimir_tablero(tablero):

    """
    Imprime el tablero de forma legible.
    """

    print("\nTablero:")
    
    for fila in tablero:
        print(" ".join(str(celda) for celda in fila))
    print()