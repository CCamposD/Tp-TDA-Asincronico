from Segunda_Parte.mainSegundaParte import juego_monedas

def test01_monedasDE1A10ConsecutivasEnJuegoGanaSofia():
	#Arrange
    monedas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	#Act
    puntaje_sofia, puntaje_mateo = juego_monedas(monedas)

	#Assert
    assert puntaje_sofia > puntaje_mateo

def test02_con4MonedasYUnaDeValorMuyAltoSiSofiaElige7Pierde():
	#Arrange
	monedas = [1, 5, 233, 7]
	
	#Act
	puntaje_sofia, puntaje_mateo = juego_monedas(monedas)

	
	#Assert
	assert puntaje_sofia > puntaje_mateo

def test03_seJuegaCon3MonedasSiendoLaDeAlMedioDeValorMasAltoSofiaPierde():
	#Arrange
	monedas = [1, 10, 5]

	#Act
	# Sophia siempre pierde
	puntaje_sofia, puntaje_mateo = juego_monedas(monedas)
	
	#Assert
	assert puntaje_mateo > puntaje_sofia

def test04_seJuegaCon0MonedasAmbosTendranMismoPuntaje0():
	#Arrange
    monedas = []
    
    #Act
    puntaje_sofia, puntaje_mateo = juego_monedas(monedas)

    #Assert
    assert puntaje_sofia == puntaje_mateo

def test05_sofiIdentificaBienQueNumeroElegirParaGanar():
	#Arrange
    monedas = [3, 17, 6, 1]
	
    #Act
    # sofia debe elegir el 1 al principio 
    puntaje_sofia, puntaje_mateo = juego_monedas(monedas)
	
    #Assert
    assert puntaje_sofia > puntaje_mateo

def test06_monedasConValoresAltosYBajosSofiaGana():
    #Arrange
    monedas = [1, 4, 7, 4, 2, 1, 7, 90, 100, 10]
    
    #Act
    puntaje_sofia, puntaje_mateo = juego_monedas(monedas)
    
    #Assert
    assert puntaje_sofia > puntaje_mateo

def testCatedra01_seJuegaConUnTotalDe5Monedas():
	# Arrange
	nombre_archivo = "Segunda_Parte/TestsCatedra/5.txt"
	with open(nombre_archivo, 'r') as archivo:
		primera_linea = archivo.readline()
	valores_lista = primera_linea.split(";")
	array_5_monedas = [int(valor) for valor in valores_lista]

	# Act
	puntaje_sofia, puntaje_mateo = juego_monedas(array_5_monedas)

	# Assert
	assert puntaje_sofia > puntaje_mateo

def testCatedra02_seJuegaConUnTotalDe10Monedas():
    # Arrange
    nombre_archivo = "Segunda_Parte/TestsCatedra/10.txt"
    with open(nombre_archivo, 'r') as archivo:
        primera_linea = archivo.readline()
    valores_lista = primera_linea.split(";")
    array_10_monedas = [int(valor) for valor in valores_lista]

    # Act
    puntaje_sofia, puntaje_mateo = juego_monedas(array_10_monedas)

    # Assert
    assert puntaje_sofia > puntaje_mateo

def testCatedra03_seJuegaConUnTotalDe20Monedas():
    # Arrange
    nombre_archivo = "Segunda_Parte/TestsCatedra/20.txt"
    with open(nombre_archivo, 'r') as archivo:
        primera_linea = archivo.readline()
    valores_lista = primera_linea.split(";")
    array_20_monedas = [int(valor) for valor in valores_lista]

    # Act
    puntaje_sofia, puntaje_mateo = juego_monedas(array_20_monedas)

    # Assert
    assert puntaje_sofia > puntaje_mateo

def testCatedra04_seJuegaConUnTotalDe50Monedas():
    # Arrange
    nombre_archivo = "Segunda_Parte/TestsCatedra/50.txt"
    with open(nombre_archivo, 'r') as archivo:
        primera_linea = archivo.readline()
    valores_lista = primera_linea.split(";")
    array_50_monedas = [int(valor) for valor in valores_lista]

    # Act
    puntaje_sofia, puntaje_mateo = juego_monedas(array_50_monedas)

    # Assert
    assert puntaje_sofia > puntaje_mateo

def testCatedra05_seJuegaConUnTotalDe100Monedas():
    # Arrange
    nombre_archivo = "Segunda_Parte/TestsCatedra/100.txt"
    with open(nombre_archivo, 'r') as archivo:
        primera_linea = archivo.readline()
    valores_lista = primera_linea.split(";")
    array_100_monedas = [int(valor) for valor in valores_lista]

    # Act
    puntaje_sofia, puntaje_mateo = juego_monedas(array_100_monedas)

    # Assert
    assert puntaje_sofia > puntaje_mateo

def testCatedra06_seJuegaConUnTotalDe1000Monedas():
    # Arrange
    nombre_archivo = "Segunda_Parte/TestsCatedra/1000.txt"
    with open(nombre_archivo, 'r') as archivo:
        primera_linea = archivo.readline()
    valores_lista = primera_linea.split(";")
    array_1000_monedas = [int(valor) for valor in valores_lista]

    # Act
    puntaje_sofia, puntaje_mateo = juego_monedas(array_1000_monedas)

    # Assert
    assert puntaje_sofia > puntaje_mateo

def testCatedra07_seJuegaConUnTotalDe10000Monedas():
    # Arrange
    nombre_archivo = "Segunda_Parte/TestsCatedra/10000.txt"
    with open(nombre_archivo, 'r') as archivo:
        primera_linea = archivo.readline()
    valores_lista = primera_linea.split(";")
    array_10000_monedas = [int(valor) for valor in valores_lista]

    # Act
    puntaje_sofia, puntaje_mateo = juego_monedas(array_10000_monedas)

    # Assert
    assert puntaje_sofia > puntaje_mateo