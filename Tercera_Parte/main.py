import Barcos
import Tablero

def es_valida(tablero, fila, columna, largo, direccion):
    ancho = len(tablero[0])
    alto = len(tablero)

    # Verificar que el barco no exceda los límites del tablero
    if direccion == "H" and columna + largo > ancho:
        return False
    if direccion == "V" and fila + largo > alto:
        return False

    # Verificar que las celdas y su entorno estén vacías
    for i in range(largo):
        if direccion == "H":
            if not esta_espacio_libre(tablero, fila, columna + i):
                return False
        elif direccion == "V":
            if not esta_espacio_libre(tablero, fila + i, columna):
                return False

    return True


def esta_espacio_libre(tablero, fila, columna):
    """
    Verifica que una celda y su entorno (adyacentes y diagonales) estén vacías.
    """
    alto = len(tablero)
    ancho = len(tablero[0])

    for i in range(-1, 2):
        for j in range(-1, 2):
            nueva_fila = fila + i
            nueva_columna = columna + j

            if 0 <= nueva_fila < alto and 0 <= nueva_columna < ancho:
                if tablero[nueva_fila][nueva_columna] == 1:
                    return False

    return True


def colocar_barco(tablero, fila, columna, largo, direccion):
    """
    Coloca un barco en el tablero.
    """
    for i in range(largo):
        if direccion == "H":
            tablero[fila][columna + i] = 1
        elif direccion == "V":
            tablero[fila + i][columna] = 1


def retirar_barco(tablero, fila, columna, largo, direccion):
    """
    Retira un barco del tablero.
    """
    for i in range(largo):
        if direccion == "H":
            tablero[fila][columna + i] = 0
        elif direccion == "V":
            tablero[fila + i][columna] = 0


def resolver_batalla_naval(tablero, barcos, indice=0):
    """
    Algoritmo de backtracking para resolver el problema de la Batalla Naval.
    """
    if indice == len(barcos):
        return True

    largo = barcos[indice]

    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            for direccion in ["H", "V"]:
                if es_valida(tablero, fila, columna, largo, direccion):
                    colocar_barco(tablero, fila, columna, largo, direccion)

                    if resolver_batalla_naval(tablero, barcos, indice + 1):
                        return True

                    retirar_barco(tablero, fila, columna, largo, direccion)

    return False


def main():
    # Inicializar tablero
    ancho, alto = Tablero.parametros_tablero()
    tablero = Tablero.inicializar_tablero(ancho, alto)

    # Obtener barcos
    lista_barcos = Barcos.pedir_barcos()

    # Resolver el problema
    if resolver_batalla_naval(tablero, lista_barcos):
        print("¡Solución encontrada!")
        Tablero.imprimir_tablero(tablero)
    else:
        print("No hay solución posible.")


if __name__ == "__main__":
    main()
