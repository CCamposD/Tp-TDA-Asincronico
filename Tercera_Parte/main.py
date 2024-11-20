import os
import barcos
import Inicializar_tablero


def main():

    ancho, alto = Inicializar_tablero.parametros_tablero()
    tablero = Inicializar_tablero.inicializar_tablero(ancho, alto)

    barcos.pedir_barcos(ancho, alto)

    Inicializar_tablero.imprimir_tablero(tablero)

    print("\n\n")

    return tablero