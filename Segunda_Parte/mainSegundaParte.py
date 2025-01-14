import sys

def leer_monedas_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            
            contenido = archivo.readline().strip()

            # Separar por punto y coma
            valores_lista = contenido.split(";")

            # Convertir a lista de enteros
            monedas = [int(valor) for valor in valores_lista]

            return monedas

    except FileNotFoundError:
        print('No se encontró el archivo.')
        sys.exit(1)


# Estrategia de Mateo

def mateo_elige(monedas):
    # Regla greedy: elegir la moneda que maximice la temprana ganancia de Mateo
    if monedas[0] > monedas[-1]:
        return monedas[0], monedas[1:]
    else:
        return monedas[-1], monedas[:-1]



#  Estrategia de Sofia
    
"""
def sophia_elige(monedas):
    n = len(monedas)
    if n == 0:
        return 0, monedas

    # Crear una tabla
    dp = [[0] * n for _ in range(n)]

    # Crear una tabla de sumas acumuladas para evitar recalcular sumas repetidas
    suma_acumulada = [0] * (n + 1)
    for i in range(1, n + 1):
        suma_acumulada[i] = suma_acumulada[i - 1] + monedas[i - 1]

    # Llenar la tabla dp de manera iterativa
    for longitud in range(1, n + 1):  # Desde intervalos de tamaño 1 hasta n
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            suma_intervalo = suma_acumulada[j + 1] - suma_acumulada[i]
            elegir_primera = monedas[i] + (suma_intervalo - dp[i + 1][j] if i + 1 <= j else 0)
            elegir_ultima = monedas[j] + (suma_intervalo - dp[i][j - 1] if i <= j - 1 else 0)
            dp[i][j] = max(elegir_primera, elegir_ultima)

    # Determinar la decisión de Sophia
    i, j = 0, n - 1
    while i <= j:
        suma_intervalo = suma_acumulada[j + 1] - suma_acumulada[i]  # Recalcular la suma solo una vez
        if i + 1 <= j and dp[i][j] == monedas[i] + (suma_intervalo - dp[i + 1][j]):
            moneda = monedas[i]
            i += 1
        else:
            moneda = monedas[j]
            j -= 1
        break  # Sophia elige una vez

    monedas_actualizadas = monedas[i:j + 1]
    return moneda, monedas_actualizadas

"""

def sophia_elige(monedas):
    """Función principal que representa la decisión de Sophia."""
    if not monedas:
        return 0, monedas

    n = len(monedas)
    suma_acumulada = calcular_suma_acumulada(monedas)
    dp = llenar_tabla_dp(monedas, suma_acumulada)

    return determinar_decision(monedas, suma_acumulada, dp)


def calcular_suma_acumulada(monedas):
    """Calcula la suma acumulada de las monedas para evitar recalcular sumas repetidas."""
    suma_acumulada = [0] * (len(monedas) + 1)
    for i in range(1, len(monedas) + 1):
        suma_acumulada[i] = suma_acumulada[i - 1] + monedas[i - 1]
    return suma_acumulada


def llenar_tabla_dp(monedas, suma_acumulada):
    """Llena la tabla DP iterativamente para calcular las mejores decisiones posibles."""
    n = len(monedas)
    dp = [[0] * n for _ in range(n)]

    for longitud in range(1, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            suma_intervalo = suma_acumulada[j + 1] - suma_acumulada[i]
            elegir_primera = monedas[i] + (suma_intervalo - dp[i + 1][j] if i + 1 <= j else 0)
            elegir_ultima = monedas[j] + (suma_intervalo - dp[i][j - 1] if i <= j - 1 else 0)
            dp[i][j] = max(elegir_primera, elegir_ultima)
    return dp


def determinar_decision(monedas, suma_acumulada, dp):
    """Determina la moneda que Sophia elige y actualiza la lista de monedas restantes."""
    i, j = 0, len(monedas) - 1
    while i <= j:
        suma_intervalo = suma_acumulada[j + 1] - suma_acumulada[i]
        if i + 1 <= j and dp[i][j] == monedas[i] + (suma_intervalo - dp[i + 1][j]):
            moneda = monedas[i]
            i += 1
        else:
            moneda = monedas[j]
            j -= 1
        break  # Sophia elige una vez
    monedas_actualizadas = monedas[i:j + 1]
    return moneda, monedas_actualizadas



# Juego de monedas


def actualizar_puntaje(puntaje, moneda):
    return puntaje + moneda

def elegir_moneda_y_actualizar(puntaje, monedas, turno_sophia):

    if turno_sophia:
        moneda, monedas_actualizadas = sophia_elige(monedas)
    else:
        moneda, monedas_actualizadas = mateo_elige(monedas)
        
    puntaje_actualizado = actualizar_puntaje(puntaje, moneda)

    if turno_sophia:
        print(f'Sophia elige la moneda: {moneda}')
    else:
        print(f'Mateo elige la moneda: {moneda}')
    
    return puntaje_actualizado, monedas_actualizadas

def jugar_turno(puntaje, monedas, turno_sophia):
    return elegir_moneda_y_actualizar(puntaje, monedas, turno_sophia)

def juego_monedas(monedas):

    puntaje_sophia = 0
    puntaje_mateo = 0
    turno_sophia = True

    if not monedas:
      
        return puntaje_sophia, puntaje_mateo


    while monedas:

        if turno_sophia:

            puntaje_sophia, monedas = jugar_turno(puntaje_sophia, monedas, turno_sophia)

        else:

            puntaje_mateo, monedas = jugar_turno(puntaje_mateo, monedas, turno_sophia)
            

        turno_sophia = not turno_sophia

    return puntaje_sophia, puntaje_mateo


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Uso: python mainPrimeraParte.py nombre_archivo')
        sys.exit(1)

    nombre_archivo = sys.argv[1]
    monedas = leer_monedas_desde_archivo(nombre_archivo)

    puntaje_sophia, puntaje_mateo = juego_monedas(monedas)

    if puntaje_mateo < puntaje_sophia:
        print('Gana Sophia')
    elif puntaje_mateo > puntaje_sophia:
        print('Gana Mateo')
    else:
        print('Empate')