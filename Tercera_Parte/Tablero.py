def parametros_tablero():

    '''
    Solicita las dimensiones del tablero al usuario.
    '''
    condicion = True
    while condicion:

        try:
            ancho = int(input("Ancho del tablero: "))
            alto = int(input("Alto del tablero: "))

            if ancho > 0 and alto > 0:
                condicion = False
            else:
                print("Por favor, ingrese un número mayor a 0.")

        except ValueError:
            print("Por favor, ingrese un número válido.")

    return ancho, alto


def inicializar_tablero(ancho, alto):

    '''
    Crea un tablero vacío con dimensiones dadas.
    '''

    return [[0 for i in range(ancho)] for i in range(alto)]


def imprimir_tablero(tablero):

    '''
    Imprime el tablero.
    '''
    print("\nTablero:")
    
    for fila in tablero:
        print(" ".join(str(celda) for celda in fila)," ".join(f"| {sum(fila)}"))
    

    print(" ".join("-" for _ in range(len(tablero[0]))))

    for i in range(len(tablero[0])):
        print(sum(tablero[j][i] for j in range(len(tablero))), end=" ")

    print("\n")
