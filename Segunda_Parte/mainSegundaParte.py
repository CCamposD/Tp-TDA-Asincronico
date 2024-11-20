def primer_moneda_mayor_valor(monedas):
    return monedas[0] > monedas[-1]

def mateo_elige(monedas):

    if primer_moneda_mayor_valor(monedas):

        return monedas[0], monedas[1:]
    
    else:

        return monedas[-1], monedas[:-1]

def Tomar_moneda_y_actualizar(monedas, valor_al_elegir_primera, valor_al_elegir_ultima, inicio, fin):

    if valor_al_elegir_primera >= valor_al_elegir_ultima:

        moneda_elegida = monedas[inicio]
        monedas_actualizadas = monedas[1:]
    else:

        moneda_elegida = monedas[fin]
        monedas_actualizadas = monedas[:-1]

    return monedas_actualizadas, moneda_elegida
    

def inicializar_tabla_dp(n):

    dp = []

    for i in range(n):

        fila = [0] * n
        dp.append(fila)

    return dp

def calcular_valores_al_elegir(monedas, dp, inicio, fin):

    if inicio + 1 <= fin:

        valor_al_elegir_primera = monedas[inicio] - dp[inicio + 1][fin]

    else:

        valor_al_elegir_primera = monedas[inicio]

    if inicio <= fin - 1:

        valor_al_elegir_ultima = monedas[fin] - dp[inicio][fin - 1]

    else:

        valor_al_elegir_ultima = monedas[fin]

    return valor_al_elegir_primera, valor_al_elegir_ultima

def calcular_optimos(monedas):

    n = len(monedas)
    dp = inicializar_tabla_dp(n)

    for i in range(n):

        dp[i][i] = monedas[i]

    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):

            j = i + longitud - 1
            
            valor_al_elegir_primera, valor_al_elegir_ultima = calcular_valores_al_elegir(monedas, dp, i, j)
            dp[i][j] = max(valor_al_elegir_primera, valor_al_elegir_ultima)

    return dp


def sophia_elige(monedas):
    n = len(monedas)

    if n == 0:
        return 0, monedas
    
    dp = calcular_optimos(monedas)

    izquierda = 0
    derecha = n - 1

    valor_al_elegir_primera, valor_al_elegir_ultima = calcular_valores_al_elegir(monedas, dp, izquierda, derecha)

    monedas_actualizadas, moneda_elegida = Tomar_moneda_y_actualizar(monedas, valor_al_elegir_primera, valor_al_elegir_ultima, izquierda, derecha)

    return moneda_elegida, monedas_actualizadas

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
        print(turno_sophia)
        print(f"Monedas: {monedas}")

        if turno_sophia:

            puntaje_sophia, monedas = jugar_turno(puntaje_sophia, monedas, turno_sophia)

        else:

            puntaje_mateo, monedas = jugar_turno(puntaje_mateo, monedas, turno_sophia)
            

        turno_sophia = not turno_sophia

    return puntaje_sophia, puntaje_mateo

