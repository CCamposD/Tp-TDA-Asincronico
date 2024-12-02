def primer_moneda_mayor_valor(monedas):
    return monedas[0] > monedas[-1]

def sophia_elige(monedas):

    if primer_moneda_mayor_valor(monedas):

        return monedas[0], monedas[1:]
    else:

        return monedas[-1], monedas[:-1]

def mateo_elige(monedas):

    if primer_moneda_mayor_valor(monedas):

        return monedas[-1], monedas[:-1]
    else:

        return monedas[0], monedas[1:]

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

    while monedas:

        if turno_sophia:

            puntaje_sophia, monedas = jugar_turno(puntaje_sophia, monedas, turno_sophia)

        else:

            puntaje_mateo, monedas = jugar_turno(puntaje_mateo, monedas, turno_sophia)

        turno_sophia = not turno_sophia

    return puntaje_sophia, puntaje_mateo