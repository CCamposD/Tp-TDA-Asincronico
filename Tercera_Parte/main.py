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

    '''
    Verifica que una celda y su entorno (adyacentes y diagonales) estén vacías.
    '''

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

    '''
    Coloca un barco en el tablero.
    '''

    for i in range(largo):

        if direccion == "H":
            tablero[fila][columna + i] = 1
        elif direccion == "V":
            tablero[fila + i][columna] = 1


def retirar_barco(tablero, fila, columna, largo, direccion):

    '''
    Retira un barco del tablero.
    '''

    for i in range(largo):

        if direccion == "H":
            tablero[fila][columna + i] = 0
        elif direccion == "V":
            tablero[fila + i][columna] = 0

def intentar_colocar_barco(tablero, largo):
    '''
    Busca una posición válida para colocar un barco.
    Si encuentra una posición válida, coloca el barco y devuelve True.
    Si no encuentra posición, devuelve False.
    '''
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            for direccion in ["H", "V"]:
                if es_valida(tablero, fila, columna, largo, direccion):
                    colocar_barco(tablero, fila, columna, largo, direccion)
                    return True
    return False

def colocar_barcos_backtracking(tablero, barcos, indice=0):
    """
    Función de backtracking que intenta colocar los barcos uno a uno en el tablero,
    pero solo los que quepan en el tablero.
    """
    # Caso base: Si hemos intentado colocar todos los barcos, terminamos
    if indice == len(barcos):
        return True

    tipo, largo = barcos[indice]

    # Intentar colocar el barco en todas las posiciones posibles y direcciones
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            for direccion in ["H", "V"]:
                

                if es_valida(tablero, fila, columna, largo, direccion):

                    colocar_barco(tablero, fila, columna, largo, direccion)

                    if colocar_barcos_backtracking(tablero, barcos, indice + 1):
                        return True

                    retirar_barco(tablero, fila, columna, largo, direccion)


    return False

def colocar_barcos_como_sea_posible(tablero, barcos, opcion):
    '''
    Utiliza backtracking para colocar tantos barcos como sea posible en el tablero.
    Devuelve el tablero actualizado y un diccionario de barcos no colocados.
    '''

    print(barcos)

    barcos_no_colocados = {}

    if opcion == 1:  # Greedy
        barcos = sorted(barcos, key=lambda x: x[1], reverse=True)  # Ordenar barcos de mayor a menor
        
        for tipo, largo in barcos:
            if not intentar_colocar_barco(tablero, largo):  # Intentar colocar este barco
                # Si no se puede colocar, agregarlo a barcos_no_colocados
                if tipo in barcos_no_colocados:
                    barcos_no_colocados[tipo] += 1
                else:
                    barcos_no_colocados[tipo] = 1


    elif opcion == 2:  # Backtracking
        
        for tipo, largo in barcos:
            if not colocar_barcos_backtracking(tablero, [(tipo, largo)]):  # Intentar colocar este barco
                if tipo in barcos_no_colocados:
                    barcos_no_colocados[tipo] += 1
                else:
                    barcos_no_colocados[tipo] = 1


    return tablero, barcos_no_colocados

##############################


##########################

def menu(tablero, lista_barcos):

    print("Que estraegia desea utilizar para colocar los barcos?")
    print("1. Greedy")
    print("2. Backtracking")
    print("3. Aproximacion")
    print("4. Salir")

    desicion = True
    ciclo = 0
    while desicion:
        try:

            
            if ciclo == 0:
                opcion = int(input("Ingrese su opcion: "))
                    
                if opcion == 1 or opcion == 2:
                    
                    tablero, barcos_no_colocados = colocar_barcos_como_sea_posible(tablero, lista_barcos, opcion)

                    Tablero.imprimir_tablero(tablero)

                    Barcos.imprimir_barcos_no_colocados(barcos_no_colocados)

                    ciclo = 1

                elif opcion == 3:

                    print("Aproximacion no implementada.")
                    input("Presione enter para volver al menu.")

                elif opcion == 4:
                    
                    print("Adios.")
                    desicion = False
                else:
                    print("Por favor, ingrese una opcion valida.")

            else:
                print("Desea volver a colocar los barcos que ya estan en el tablero?")
                print("1. Si")
                print("2. No")

                opcion = int(input("Ingrese su opcion: "))




                desicion = False

        except ValueError:
            print("Por favor, ingrese un numero valido.")



def main():
    # Inicializar tablero
    ancho, alto = Tablero.parametros_tablero()
    tablero = Tablero.inicializar_tablero(ancho, alto)

    # Obtener barcos
    lista_barcos = Barcos.pedir_barcos()

    menu(tablero, lista_barcos)



if __name__ == "__main__":
    main()
