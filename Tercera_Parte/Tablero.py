#PRE:
#POST: Se le pide al usuario los valores de ancho y alto del tablero
def parametros_tablero():

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

#PRE: Recibe un ancho y un alto del tablero
#POST: Devuelve una lista de listas con el tablero inicializado
def inicializar_tablero(ancho, alto):

    return [[0 for i in range(ancho)] for i in range(alto)]

#PRE: Recibe un tablero
#POST: Imprime el tablero
def imprimir_tablero(tablero):

    print("\nTablero:")
    
    for fila in tablero:
        print(" ".join(str(celda) for celda in fila)," ".join(f"| {sum(fila)}"))
    

    print(" ".join("-" for _ in range(len(tablero[0]))))

    for i in range(len(tablero[0])):
        print(sum(tablero[j][i] for j in range(len(tablero))), end=" ")

    print("\n")
