import os
import matplotlib.pyplot as plt
from util import time_algorithm
from main import aproximacion
from Tablero import inicializar_tablero

# Define una función para generar un tablero vacío
def generar_tablero(size):
    return inicializar_tablero(size+5, size)

# Define una función para generar barcos dinámicamente
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



# Función para preparar los argumentos de entrada
def preparar_argumentos(size):
    tablero = generar_tablero(size)
    barcos = generar_barcos(size)
    return tablero, barcos

# Medir el rendimiento del algoritmo
def medir_rendimiento():
    sizes = [1, 2, 3, 4, 5, 6]
    
    # Función generadora de argumentos ajustada
    def get_args(size):
        return preparar_argumentos(size)
    
    # Llamada correcta a time_algorithm
    print("Ejecutando time_algorithm")
    tiempos = time_algorithm(aproximacion, sizes, get_args)
    print("Sali:")
    
    # Graficar los tiempos
    plt.figure(figsize=(10, 6))
    plt.plot(tiempos.keys(), tiempos.values(), marker='o', label='Tiempo de ejecución')
    plt.xlabel('Aumento proporcional (n)')
    plt.ylabel('Tiempo promedio (s)')
    plt.title('Rendimiento de aproximacion')
    plt.grid(True)
    plt.legend()

    # Ruta relativa a la carpeta dentro del repositorio
    output_folder = "complejidad"
    
    # Verifica si la carpeta existe, si no, créala
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Guardar el gráfico en la carpeta relativa
    output_path = os.path.join(output_folder, "aumento_proporcional.png")
    plt.savefig(output_path)
    print(f"Gráfico guardado en {output_path}")


if __name__ == "__main__":
    medir_rendimiento()
