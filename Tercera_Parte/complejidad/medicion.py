import matplotlib.pyplot as plt
from Tercera_Parte.mainTerceraParte import colocar_barcos_backtracking  # Implementación exacta
from Tercera_Parte.mainTerceraParte import aproximacion        # Algoritmo aproximado
from Tablero import inicializar_tablero
from Tercera_Parte.mainTerceraParte import colocar_barcos_como_sea_posible
import numpy as np

def generar_tablero(n):
    return inicializar_tablero(n+5, n)



def generar_barcos(size):
    import random
    tipos_barcos = [("Porta avion", 4), ("Submarino", 3), ("Destructor", 2), ("Lancha", 1)]
    barcos = []
    
    # Generar una cantidad fija de barcos
    cantidad_barcos = size

    # Índice para recorrer la lista de tipos de barcos
    i = 0  

    while cantidad_barcos > 0:
        # Obtener el barco actual
        barco = tipos_barcos[i]
        
        # Crear una nueva tupla con la longitud modificada
        nuevo_barco = (barco[0], size)
        barcos.append(nuevo_barco)
        cantidad_barcos -= 1
        
        # Avanzar al siguiente tipo de barco de manera cíclica
        i = (i + 1) % len(tipos_barcos)
    
    return barcos

def preparar_argumentos(size):
    tablero = generar_tablero(size)
    barcos = generar_barcos(size)

    tablero_listo = colocar_barcos_como_sea_posible(tablero, barcos, 1)
    return tablero_listo, barcos

def calcular_rendimiento(instancias):
    """
    Calcula el rendimiento de las soluciones exacta y aproximada.
    """
    resultados = {"exacto": [], "aproximado": [], "relacion": []}

    for tablero, barcos in instancias:
        # Solución exacta
        z_i = colocar_barcos_backtracking(tablero, barcos)
        
        # Solución aproximada
        tablero_aprox = [fila[:] for fila in tablero]  # Copia del tablero
        a_i = aproximacion(tablero_aprox, barcos)
        
        # Relación entre aproximación y óptimo
        relacion = a_i / z_i if z_i > 0 else float('inf')

        # Almacenar resultados
        resultados["exacto"].append(z_i)
        resultados["aproximado"].append(a_i)
        resultados["relacion"].append(relacion)

    return resultados

def medir_rendimiento():
    """
    Mide el rendimiento para diferentes tamaños de tablero y muestra los resultados.
    """
    # Generar instancias pequeñas para comparar exacto vs aproximado
    tamaños_pequeños = [5, 10, 15]  # Ejemplo de tamaños
    instancias_pequeñas = [
        preparar_argumentos(n) for n in tamaños_pequeños
    ]

    resultados_pequeños = calcular_rendimiento(instancias_pequeñas)

    # Graficar resultados pequeños
    plt.figure(figsize=(10, 5))
    plt.plot(tamaños_pequeños, resultados_pequeños["exacto"], label="Exacto (z(I))", marker='o')
    plt.plot(tamaños_pequeños, resultados_pequeños["aproximado"], label="Aproximado (A(I))", marker='x')
    plt.title("Comparación entre soluciones exactas y aproximadas")
    plt.xlabel("Tamaño del tablero")
    plt.ylabel("Valor de solución")
    plt.legend()
    plt.grid()
    plt.savefig("comparacion_pequenos.png")
    print("Gráfico de instancias pequeñas guardado: comparacion_pequenos.png")

    # Evaluar r(A) (la relación máxima)
    r_a = max(resultados_pequeños["relacion"])
    print(f"Máximo r(A) para instancias pequeñas: {r_a:.2f}")

    # Generar instancias grandes para evaluar la escalabilidad
    tamaños_grandes = [50, 100, 200, 500]
    instancias_grandes = [
        preparar_argumentos(n) for n in tamaños_grandes
    ]

    resultados_grandes = []
    for tablero, barcos in instancias_grandes:
        tablero_aprox = [fila[:] for fila in tablero]  # Copia del tablero
        a_i = aproximacion(tablero_aprox, barcos)
        resultados_grandes.append(a_i)

    # Graficar resultados grandes
    plt.figure(figsize=(10, 5))
    plt.plot(tamaños_grandes, resultados_grandes, label="Aproximado (A(I))", marker='x')
    plt.title("Solución aproximada para instancias grandes")
    plt.xlabel("Tamaño del tablero")
    plt.ylabel("Valor de solución")
    plt.legend()
    plt.grid()
    plt.savefig("aproximacion_grandes.png")
    print("Gráfico de instancias grandes guardado: aproximacion_grandes.png")


if __name__ == "__main__":
    medir_rendimiento()