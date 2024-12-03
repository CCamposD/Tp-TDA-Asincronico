import os
import matplotlib.pyplot as plt
from Segunda_Parte.complejidad.util import time_algorithm
from mainSegundaParte import juego_monedas

# Define una función para generar argumentos para juego_monedas
def get_args(size):
    import random
    return [[random.randint(1, 100) for _ in range(size)]]

# Medir el rendimiento del algoritmo
def medir_rendimiento():
    sizes = [10, 50, 100, 500, 1000]
    tiempos = time_algorithm(juego_monedas, sizes, get_args)

    # Graficar los tiempos
    plt.figure(figsize=(10, 6))
    plt.plot(tiempos.keys(), tiempos.values(), marker='o', label='Tiempo de ejecución')
    plt.xlabel('Tamaño de entrada (número de monedas)')
    plt.ylabel('Tiempo promedio (s)')
    plt.title('Rendimiento de juego_monedas')
    plt.grid(True)
    plt.legend()

    # Ruta relativa a la carpeta dentro del repositorio
    output_folder = "complejidad"
    
    # Verifica si la carpeta existe, si no, créala
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Guardar el gráfico en la carpeta relativa
    output_path = os.path.join(output_folder, "rendimiento_juego_monedas.png")
    plt.savefig(output_path)
    print(f"Gráfico guardado en {output_path}")

if __name__ == "__main__":
    medir_rendimiento()
