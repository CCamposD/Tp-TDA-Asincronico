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
    
    if turno_sophia:
        print(f'Sophia elige la moneda: {moneda}')
    else:
        print(f'Mateo elige la moneda: {moneda}')
    
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