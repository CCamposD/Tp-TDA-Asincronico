import Barcos
import Tablero

#PRE: Recibe un tablero, una fila, una columna, un largo y una dirección
#POST: Devuelve True si la posición es válida, False si no cumple con la restricción
def es_valida(tablero, fila, columna, largo, direccion):

    ancho = len(tablero[0])
    alto = len(tablero)



    if direccion == "H" and columna + largo > ancho:
        return False
    
    if direccion == "V" and fila + largo > alto:
        return False



    for i in range(largo):

        if direccion == "H":

            if not esta_espacio_libre(tablero, fila, columna + i):

                return False
            
        elif direccion == "V":
            if not esta_espacio_libre(tablero, fila + i, columna):

                return False

    return True

#PRE: Recibe un tablero, una fila y una columna
#POST: Devuelve True si la celda y su entorno están vacías, False si no lo están
def esta_espacio_libre(tablero, fila, columna):

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

#PRE: Recibe un tablero, unas coordenadas, un largo y una dirección
#POST: Coloca un barco en el tablero
def colocar_barco(tablero, fila, columna, largo, direccion):

    for i in range(largo):

        if direccion == "H":
            tablero[fila][columna + i] = 1

        elif direccion == "V":
            tablero[fila + i][columna] = 1

#PRE: Recibe un tablero, unas coordenadas, un largo y una dirección
#POST: Retira un barco del tablero
def retirar_barco(tablero, fila, columna, largo, direccion):

    for i in range(largo):

        if direccion == "H":
            tablero[fila][columna + i] = 0

        elif direccion == "V":
            tablero[fila + i][columna] = 0

#PRE: Recibe un tablero, un largo
#POST: Devuelve True si encuentra una posición válida para colocar un barco, False si no la encuentra
def intentar_colocar_barco(tablero, largo):

    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            for direccion in ["H", "V"]:

                if es_valida(tablero, fila, columna, largo, direccion):
                    colocar_barco(tablero, fila, columna, largo, direccion)
                    return True
    return False

#PRE: Recibe un tablero, una lista de barcos y un índice
#POST: Devuelve True si logra colocar todos los barcos, False si no lo logra
def colocar_barcos_backtracking(tablero, barcos, indice=0):

    if indice == len(barcos):
        return True

    tipo, largo = barcos[indice]

    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            for direccion in ["H", "V"]:

                if es_valida(tablero, fila, columna, largo, direccion):

                    colocar_barco(tablero, fila, columna, largo, direccion)

                    if colocar_barcos_backtracking(tablero, barcos, indice + 1):
                        return True

                    retirar_barco(tablero, fila, columna, largo, direccion)


    return False

#PRE: Recibe un tablero, una lista de barcos y una opción de estrategia
#POST: Devuelve el tablero actualizado, un diccionario de barcos no colocados y una de los barcos colocados
def colocar_barcos_como_sea_posible(tablero, barcos, opcion):

    barcos_no_colocados = {}
    barcos_colocados = []

    if opcion == 1:  # Greedy
        barcos = sorted(barcos, key=lambda x: x[1], reverse=True)
        
        for tipo, largo in barcos:
            
            if not intentar_colocar_barco(tablero, largo):
                
                if tipo in barcos_no_colocados:
                    barcos_no_colocados[tipo] += 1
                
                else:
                    barcos_no_colocados[tipo] = 1

            else:
                barcos_colocados.append((tipo, largo))


    elif opcion == 2:  # Backtracking
        
        for tipo, largo in barcos:

            if not colocar_barcos_backtracking(tablero, [(tipo, largo)]):
                
                if tipo in barcos_no_colocados:
                    barcos_no_colocados[tipo] += 1

                else:
                    barcos_no_colocados[tipo] = 1

            else:
                barcos_colocados.append((tipo, largo))


    return tablero, barcos_no_colocados, barcos_colocados

#PRE: Recibe un tablero, unas coordenadas, una dirección
#POST: Devuelve la cantidad de celdas vacías en una fila o columna
def verificar_demanda(tablero, fila, columna, direccion):
    
    demanda = 0

    if direccion == "H": 

        actual_demanda = 0

        for i in range(len(tablero[0])):

            if tablero[fila][i] == 0:
                actual_demanda += 1 

            else:
                demanda = max(demanda, actual_demanda) 
                actual_demanda = 0
        demanda = max(demanda, actual_demanda)  
    
    elif direccion == "V": 
        
        actual_demanda = 0

        for i in range(len(tablero)):

            if tablero[i][columna] == 0:
                actual_demanda += 1  

            else:
                demanda = max(demanda, actual_demanda)  
                actual_demanda = 0
        demanda = max(demanda, actual_demanda)
    
    return demanda

#PRE: Recibe un tablero
#POST: Devuelve una lista de demandas ordenadas de mayor a menor
def obtener_demandas_ordenadas(tablero):
    demandas = []
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            for direccion in ["H", "V"]:

                actual_demandada = verificar_demanda(tablero, fila, columna, direccion)

                if actual_demandada > 0:

                    demandas.append([actual_demandada, fila, columna, direccion])
    
    demandas.sort(reverse=True, key=lambda x: x[0])

    return demandas

#PRE: Recibe un tablero, una lista de barcos en el tablero
#POST: Devuelve el barco de mayor longitud en el tablero
def identificar_barco_mayor_longitud(tablero, barcos_en_el_tablero):
    
    mayor_longitud = max(barcos_en_el_tablero, key=lambda x: x[1])
    
    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            for direccion in ["H", "V"]:
                if direccion == "H":

                    if columna + mayor_longitud[1] <= len(tablero[0]):  
                        if all(tablero[fila][columna + i] == 1 for i in range(mayor_longitud[1])):
                            
                            print(f"Barco de mayor longitud encontrado: {mayor_longitud}, en fila {fila}, columna {columna}, dirección H")
                            
                            return mayor_longitud, fila, columna, direccion
                
                elif direccion == "V":
                   
                    if fila + mayor_longitud[1] <= len(tablero): 
                        
                        if all(tablero[fila + i][columna] == 1 for i in range(mayor_longitud[1])):
                            
                            print(f"Barco de mayor longitud encontrado: {mayor_longitud}, en fila {fila}, columna {columna}, dirección V")
                            
                            return mayor_longitud, fila, columna, direccion

    print("No se encontró el barco de mayor longitud")

    return mayor_longitud

#PRE: Recibe un tablero, un barco, sus coordenadas y direccion, y las coordenadas y dirección de la demanda, ademas de los barcos en el tablero
#POST: Devuelve True si logra colocar el barco en la demanda, False si no lo logra
def intentar_colocar_barco(tablero, barco, fila, columna, direccion, fila_demandada, columna_demandada, direccion_demandada, barcos_en_el_tablero):

    if direccion_demandada == "V":

        for i in range(len(tablero)):

            if es_valida(tablero, i, columna_demandada, barco[1], "V"):

                retirar_barco(tablero, fila, columna, barco[1], direccion)
                barcos_en_el_tablero.remove(barco)

                colocar_barco(tablero, i, columna_demandada, barco[1], "V")

                return True
            
    elif direccion_demandada == "H":

        for i in range(len(tablero[0])):

            if es_valida(tablero, fila_demandada, i, barco[1], "H"):

                retirar_barco(tablero, fila, columna, barco[1], direccion)
                barcos_en_el_tablero.remove(barco)

                colocar_barco(tablero, fila_demandada, i, barco[1], "H")

                return True
            
    return False

#PRE: Recibe un tablero y una lista de barcos en el tablero
#POST: Devuelve el tablero con los barcos reubicados
def aproximacion(tablero, barcos_en_el_tablero):
    
    intentos_sin_colocacion = 0
    max_intentos = len(barcos_en_el_tablero)

    while barcos_en_el_tablero and intentos_sin_colocacion < max_intentos:

        barco_mayor_longitud, fila, columna, direccion = identificar_barco_mayor_longitud(tablero, barcos_en_el_tablero)
        demandas = obtener_demandas_ordenadas(tablero)

        colocado = False

        for demanda in demandas:
            mayor_demandada, fila_demandada, columna_demandada, direccion_demandada = demanda
            
            if mayor_demandada >= barco_mayor_longitud[1]:

                if intentar_colocar_barco(tablero, barco_mayor_longitud, fila, columna, direccion, fila_demandada, columna_demandada, direccion_demandada, barcos_en_el_tablero):

                    colocado = True
                    break
        
        if not colocado:

            print(f"No se encontró una posición válida para colocar el barco: {barco_mayor_longitud}")

            intentos_sin_colocacion += 1

        else:
            intentos_sin_colocacion = 0

    if intentos_sin_colocacion >= max_intentos:

        print("No se pudieron colocar todos los barcos después de varios intentos. Fin del juego.")

    return tablero

#PRE: Recibe un tablero y una lista de barcos
#POST: Muestra un menú con las opciones de estrategia para colocar los barcos
def menu(tablero, lista_barcos):

    print("Que estraegia desea utilizar para colocar los barcos?")
    print("1. Greedy")
    print("2. Backtracking")
    print("3. Salir")

    desicion = True
    ciclo = 0

    while desicion:
        try:

            
            if ciclo == 0:
                opcion = int(input("Ingrese su opcion: "))
                    
                if opcion == 1 or opcion == 2:
                    
                    tablero, barcos_no_colocados, barcos_en_el_tablero = colocar_barcos_como_sea_posible(tablero, lista_barcos, opcion)

                    Tablero.imprimir_tablero(tablero)
                    Barcos.imprimir_barcos_no_colocados(barcos_no_colocados)

                    ciclo = 1

                elif opcion == 3:
                    
                    print("Adios.")
                    desicion = False

                else:
                    print("Por favor, ingrese una opcion valida.")

            else:

                print("Desea reubicar los barcos que ya estan en el tablero?")
                print("1. Si")
                print("2. No")

                opcion = int(input("Ingrese su opcion: "))

                if opcion == 1:

                    nuevo_tablero = aproximacion(tablero, barcos_en_el_tablero)

                    print("Tablero con barcos reubicados:")
                    
                    Tablero.imprimir_tablero(nuevo_tablero)

                    desicion = False

                elif opcion == 2:

                    print("Adios.")
                    desicion = False

                else:
                    print("Por favor, ingrese una opcion valida.")

        except ValueError:
            print("Por favor, ingrese un numero valido.")


#PRE: -
#POST: Main
def main():
    
    ancho, alto = Tablero.parametros_tablero()
    tablero = Tablero.inicializar_tablero(ancho, alto)

    lista_barcos = Barcos.pedir_barcos()

    menu(tablero, lista_barcos)

    print("FIN DEL JUEGO")

if __name__ == "__main__":
    main()
