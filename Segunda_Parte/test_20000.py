from mainSegundaParte import juego_monedas

def test_20000():
    nombre_archivo = "Primera_Parte/TestsCatedra/10000.txt"
    with open(nombre_archivo, 'r') as archivo:
        primera_linea = archivo.readline() 
    valores_lista = primera_linea.split(";")
    array_20000_monedas = [int(valor) for valor in valores_lista if valor.isdigit()]


    " Act " # Act
    puntaje_sofia, puntaje_mateo = juego_monedas(array_20000_monedas)

    " Assert " # Assert
    assert puntaje_sofia > puntaje_mateo