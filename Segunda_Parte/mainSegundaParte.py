# Estrategia de Mateo

def mateo_elige(monedas):
    # Regla greedy: elegir la moneda que maximice la temprana ganancia de Mateo
    if monedas[0] > monedas[-1]:
        return monedas[0], monedas[1:]
    else:
        return monedas[-1], monedas[:-1]



#  Estrategia de Sofia

# Nueva implementación, sacada de RPL lunatico 
def lunatico(ganancias):
    n = len(ganancias)
    
    if n == 0:
        return []
    elif n == 1:
        return [0] if ganancias[0] > 0 else []
    elif n == 2:
        return [0] if ganancias[0] >= ganancias[1] and ganancias[0] > 0 else ([1] if ganancias[1] > 0 else [])

    # Caso 1: Ignorar la última casa
    dp1 = [0] * (n - 1)  # Almacenamos solo hasta n-2
    track1 = [0] * (n - 1)

    dp1[0] = ganancias[0]
    track1[0] = 0
    if n > 2:
        dp1[1] = max(ganancias[0], ganancias[1])
        track1[1] = 0 if dp1[1] == ganancias[0] else 1

        for i in range(2, n - 1):
            if dp1[i - 1] > dp1[i - 2] + ganancias[i]:
                dp1[i] = dp1[i - 1]
                track1[i] = track1[i - 1]
            else:
                dp1[i] = dp1[i - 2] + ganancias[i]
                track1[i] = i

    # Recuperar las casas robadas para el caso 1
    casas_robadas1 = []
    i = len(dp1) - 1
    while i >= 0:
        if track1[i] == i:  # Se robó la casa i
            casas_robadas1.append(i)
            i -= 2  # Saltamos la casa adyacente
        else:
            i -= 1

    # Caso 2: Ignorar la primera casa
    dp2 = [0] * (n - 1)  # Almacenamos solo hasta n-2
    track2 = [0] * (n - 1)

    dp2[0] = ganancias[1]
    track2[0] = 1
    if n > 2:
        dp2[1] = max(ganancias[1], ganancias[2])
        track2[1] = 1 if dp2[1] == ganancias[1] else 2

        for i in range(2, n - 1):
            if dp2[i - 1] > dp2[i - 2] + ganancias[i + 1]:
                dp2[i] = dp2[i - 1]
                track2[i] = track2[i - 1]
            else:
                dp2[i] = dp2[i - 2] + ganancias[i + 1]
                track2[i] = i + 1

    # Recuperar las casas robadas para el caso 2
    casas_robadas2 = []
    i = len(dp2) - 1
    while i >= 0:
        if track2[i] == i + 1:  # Se robó la casa i+1
            casas_robadas2.append(i + 1)
            i -= 2  # Saltamos la casa adyacente
        else:
            i -= 1 

    # Elegir el mejor caso
    suma_caso1 = sum(ganancias[i] for i in casas_robadas1)
    suma_caso2 = sum(ganancias[i] for i in casas_robadas2)

    if suma_caso1 > suma_caso2:
        return sorted(casas_robadas1)
    else:
        return sorted(casas_robadas2)

def sophia_elige(monedas):
    n = len(monedas)

    if n == 0:
        return 0, monedas
    
    ''' Forma lunatico
    # Utilizar el algoritmo lunatico para elegir las monedas
    indices_robados = lunatico(monedas)
    if not indices_robados:
        return 0, monedas

    # Elegir la primera moneda de los índices robados
    indice_elegido = indices_robados[0]
    moneda_elegida = monedas[indice_elegido]
    monedas_actualizadas = monedas[:indice_elegido] + monedas[indice_elegido + 1:]
    '''
   
   
    # Evaluar las dos opciones: elegir la primera o la última moneda
    primera_moneda = monedas[0]
    ultima_moneda = monedas[-1]

    # Simular la elección de la primera moneda
    monedas_si_elige_primera = monedas[1:]
    if len(monedas_si_elige_primera) > 1:
        mateo_elige_primera = max(monedas_si_elige_primera[0], monedas_si_elige_primera[-1])
    else:
        if monedas_si_elige_primera:
            mateo_elige_primera = monedas_si_elige_primera[0]
        else:
            mateo_elige_primera = 0
    ganancia_si_elige_primera = primera_moneda + (sum(monedas_si_elige_primera) - mateo_elige_primera)

    # Simular la elección de la última moneda
    monedas_si_elige_ultima = monedas[:-1]
    if len(monedas_si_elige_ultima) > 1:
        mateo_elige_ultima = max(monedas_si_elige_ultima[0], monedas_si_elige_ultima[-1])
    else:
        if monedas_si_elige_ultima:
            mateo_elige_ultima = monedas_si_elige_ultima[0]
        else:
            mateo_elige_ultima = 0
    ganancia_si_elige_ultima = ultima_moneda + (sum(monedas_si_elige_ultima) - mateo_elige_ultima)

    # Elegir la opción que maximice la ganancia futura de Sofía
    if ganancia_si_elige_primera > ganancia_si_elige_ultima:
        moneda_elegida = primera_moneda
        monedas_actualizadas = monedas[1:]
    else:
        moneda_elegida = ultima_moneda
        monedas_actualizadas = monedas[:-1]


    return moneda_elegida, monedas_actualizadas




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


        if(turno_sophia):
            print("Turno de Sophia")
        else:
            print("Turno de Mateo")

        print(f"Monedas antes de elegir: {monedas}")

        if turno_sophia:

            puntaje_sophia, monedas = jugar_turno(puntaje_sophia, monedas, turno_sophia)

        else:

            puntaje_mateo, monedas = jugar_turno(puntaje_mateo, monedas, turno_sophia)
            

        turno_sophia = not turno_sophia

    return puntaje_sophia, puntaje_mateo

