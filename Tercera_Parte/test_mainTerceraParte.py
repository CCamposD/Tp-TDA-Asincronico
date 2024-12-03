#Test
import Tablero
import Tercera_Parte.mainTerceraParte as mainTerceraParte


def test_01_inicializar_tablero():
    tablero = Tablero.inicializar_tablero(5, 5)


    assert len(tablero) == 5
    assert all(len(fila) == 5 for fila in tablero)
    assert all(celda == 0 for fila in tablero for celda in fila)


def test_02_colocar_barcos_en_tablero_vacio():
    tablero = Tablero.inicializar_tablero(5, 5)
    barcos = [("Porta aviones", 4), ("Submarino", 3), ("Destructor", 2), ("Lancha", 1)]

    tablero, barcos_no_colocados, barcos_en_el_tablero = mainTerceraParte.colocar_barcos_como_sea_posible(tablero, barcos, 2)

    # El tablero debe tener barcos en él
    assert any(celda != 0 for fila in tablero for celda in fila)

    assert barcos_no_colocados == {}


def test_03_sobran_barcos():
    tablero = Tablero.inicializar_tablero(3, 3)
    barcos = [("Porta aviones", 4), ("Submarino", 3), ("Destructor", 2), ("Lancha", 1)]

    tablero, barcos_no_colocados, barcos_en_el_tablero = mainTerceraParte.colocar_barcos_como_sea_posible(tablero, barcos, 2)


    assert barcos_no_colocados == {"Porta aviones": 1, "Lancha": 1}

def test_04_colocar_todos_los_barcos():
    tablero = Tablero.inicializar_tablero(5, 5)
    barcos = [("Porta aviones", 4), ("Submarino", 3), ("Destructor", 2), ("Lancha", 1)]

    tablero, barcos_no_colocados, barcos_en_el_tablero = mainTerceraParte.colocar_barcos_como_sea_posible(tablero, barcos, 2)

    
    assert barcos_no_colocados == {}

def test_05_la_posicion_no_es_valida():
    tablero = Tablero.inicializar_tablero(5, 5)
    
    assert not mainTerceraParte.es_valida(tablero, 2, 2, 4, "H")

def test_06_la_posicion_es_valida():
    tablero = Tablero.inicializar_tablero(5, 5)
    
    assert mainTerceraParte.es_valida(tablero, 0, 0, 5, "H")

def test_07_esta_espacio_libre():
    tablero = Tablero.inicializar_tablero(5, 5)
    
    tablero[0][2] = 1
    tablero[2][0] = 1

    assert mainTerceraParte.esta_espacio_libre(tablero, 0, 0)

def test_08_no_esta_espacio_libre():
    tablero = Tablero.inicializar_tablero(5, 5)
    
    tablero[0][2] = 1
    tablero[2][0] = 1

    assert not mainTerceraParte.esta_espacio_libre(tablero, 1, 1)

def test_09_retirar_barco():

    tablero = Tablero.inicializar_tablero(5, 5)
    mainTerceraParte.colocar_barco(tablero, 0, 0, 4, "H")
    mainTerceraParte.retirar_barco(tablero, 0, 0, 4, "H")

    assert tablero == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

def test_10_resolver_batalla_naval_greedy():
    tablero = Tablero.inicializar_tablero(10, 10)
    
    #una lista con: 3 porta aviones(4 largo), 3 submarinos(3 largo), 2 destructores(5 largo) y 2 lancha(1 largo)

    barcos = [("Porta aviones", 4), ("Porta aviones", 4), ("Porta aviones", 4), ("Submarino", 3), ("Submarino", 3), ("Submarino", 3), ("Destructor", 2), ("Destructor", 2), ("Lancha", 1), ("Lancha", 1)]

    tablero, barcos_no_colocados, barcos_en_el_tablero = mainTerceraParte.colocar_barcos_como_sea_posible(tablero, barcos, 2)

    assert barcos_no_colocados == {}

def test_11_resolver_batalla_naval_greedy():
    tablero = Tablero.inicializar_tablero(10, 10)
    
    #una lista con: 3 porta aviones(4 largo), 3 submarinos(3 largo), 2 destructores(5 largo) y 2 lancha(1 largo)

    barcos = [("Porta aviones", 4), ("Porta aviones", 4), ("Porta aviones", 4), ("Submarino", 3), ("Submarino", 3), ("Submarino", 3), ("Destructor", 2), ("Destructor", 2), ("Lancha", 1), ("Lancha", 1)]

    tablero, barcos_no_colocados, barcos_en_el_tablero = mainTerceraParte.colocar_barcos_como_sea_posible(tablero, barcos, 2)

    assert barcos_no_colocados == {}

def test_12_tablero_1000_x_1000():
    tablero = Tablero.inicializar_tablero(1000, 1000)
    

    barcos = [("Porta aviones", 4), ("Porta aviones", 4), ("Porta aviones", 4), ("Submarino", 3), ("Submarino", 3), ("Submarino", 3), ("Destructor", 2), ("Destructor", 2), ("Lancha", 1), ("Lancha", 1)] * 100

    tablero, barcos_no_colocados, barcos_en_el_tablero = mainTerceraParte.colocar_barcos_como_sea_posible(tablero, barcos, 2)
    assert barcos_no_colocados == {}
