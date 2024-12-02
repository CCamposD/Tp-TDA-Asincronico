# Estrategia de Mateo

def mateo_elige(monedas):
    # Regla greedy: elegir la moneda que maximice la temprana ganancia de Mateo
    if monedas[0] > monedas[-1]:
        return monedas[0], monedas[1:]
    else:
        return monedas[-1], monedas[:-1]



#  Estrategia de Sofia
    
def calcular_mejor_eleccion_sophia(monedas, inicio, fin, suma_acumulada, dp):
    if inicio > fin:
        return 0

    if dp[inicio][fin] != -1:
        return dp[inicio][fin]

    suma_intervalo = suma_acumulada[fin + 1] - suma_acumulada[inicio]
    elegir_primera = monedas[inicio] + (suma_intervalo - calcular_mejor_eleccion_sophia(monedas, inicio + 1, fin, suma_acumulada, dp))
    elegir_ultima = monedas[fin] + (suma_intervalo - calcular_mejor_eleccion_sophia(monedas, inicio, fin - 1, suma_acumulada, dp))

    dp[inicio][fin] = max(elegir_primera, elegir_ultima)
    return dp[inicio][fin]

def decision_por_PD(monedas):
    n = len(monedas)
    if n == 0:
        return 0, monedas

    # Crear una tabla de sumas acumuladas para evitar recalcular sumas repetidas
    suma_acumulada = [0] * (n + 1)
    for i in range(1, n + 1):
        suma_acumulada[i] = suma_acumulada[i - 1] + monedas[i - 1]

    # Crear una tabla dp para almacenar los resultados de subproblemas
    dp = [[-1] * n for _ in range(n)]

    # Determinar la decisión de Sophia utilizando la función recursiva
    i, j = 0, n - 1
    while i <= j:
        suma_intervalo = suma_acumulada[j + 1] - suma_acumulada[i]  # Recalcular la suma solo una vez
        if i + 1 <= j and calcular_mejor_eleccion_sophia(monedas, i, j, suma_acumulada, dp) == monedas[i] + (suma_intervalo - calcular_mejor_eleccion_sophia(monedas, i + 1, j, suma_acumulada, dp)):
            moneda = monedas[i]
            i += 1
        else:
            moneda = monedas[j]
            j -= 1
        break  # Sophia elige una vez

    monedas_actualizadas = monedas[i:j + 1]
    return moneda, monedas_actualizadas


def sophia_elige(monedas):
    # return decision_por_PD(monedas)
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



# Juego de monedas


def actualizar_puntaje(puntaje, moneda):
    return puntaje + moneda

def elegir_moneda_y_actualizar(puntaje, monedas, turno_sophia):

    if turno_sophia:
        moneda, monedas_actualizadas = sophia_elige(monedas)
    else:
        moneda, monedas_actualizadas = mateo_elige(monedas)
        
    puntaje_actualizado = actualizar_puntaje(puntaje, moneda)

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