from Primera_Parte.mainPrimeraParte import juego_monedas

def test_01_10_monedas_gana_sofia():
	a = [0,1,2,3,4,5,6,7,8,9]
	puntaje_sofia, puntaje_mateo = juego_monedas(a)
	assert puntaje_sofia > puntaje_mateo

def test_02_10_monedas_gana_sofia():
	a = [9,8,7,6,5,4,3,2,1,0]
	puntaje_sofia, puntaje_mateo = juego_monedas(a)
	assert puntaje_sofia > puntaje_mateo

def test_03_11_monedas_gana_sofia():
	a = [1,4,7,4,2,1,7,90, 100, 10]
	puntaje_sofia, puntaje_mateo = juego_monedas(a)
	assert puntaje_sofia > puntaje_mateo

def testCatedra01SeJuegaConUnTotalDe20Monedas():
	" Arrange " # Arrange
	nombre_archivo = "Primera_Parte/TestsCatedra/20.txt"
	with open(nombre_archivo, 'r') as archivo:
		primera_linea = archivo.readline()  
	valores_lista = primera_linea.split(";")
	array_20_monedas = [int(valor) for valor in valores_lista]	
	
	" Act " # Act
	puntaje_sofia, puntaje_mateo = juego_monedas(array_20_monedas)
	
	" Assert " # Assert
	assert puntaje_sofia > puntaje_mateo

def testCatedra01BPuntajeDeSofiaCorrespondeConElResultadoEsperadoJugandoCon20Monedas():
	" Arrange " # Arrange
	nombre_archivo = "Primera_Parte/TestsCatedra/20.txt"
	with open(nombre_archivo, 'r') as archivo:
		primera_linea = archivo.readline()
	valores_lista = primera_linea.split(";")
	array_20_monedas = [int(valor) for valor in valores_lista]
	
	" Act " # Act
	puntaje_sofia, puntaje_mateo = juego_monedas(array_20_monedas)
	
	" Assert " # Assert
	assert (puntaje_sofia == 7165)

def testCatedra02SeJuegaConUnTotalDe25Monedas():
	" Arrange " # Arrange
	nombre_archivo = "Primera_Parte/TestsCatedra/25.txt"
	with open(nombre_archivo, 'r') as archivo:
		primera_linea = archivo.readline()  
	valores_lista = primera_linea.split(";")
	array_25_monedas = [int(valor) for valor in valores_lista]
	
	" Act " # Act
	puntaje_sofia, puntaje_mateo = juego_monedas(array_25_monedas)
	
	" Assert " # Assert
	assert puntaje_sofia > puntaje_mateo

def testCatedra03SeJuegaConUnTotalDe50Monedas():
	" Arrange " # Arrange
	nombre_archivo = "Primera_Parte/TestsCatedra/50.txt"
	with open(nombre_archivo, 'r') as archivo:
		primera_linea = archivo.readline()
	valores_lista = primera_linea.split(";")
	array_50_monedas = [int(valor) for valor in valores_lista]
	
	" Act " # Act
	puntaje_sofia, puntaje_mateo = juego_monedas(array_50_monedas)

	" Assert " # Assert
	assert puntaje_sofia > puntaje_mateo

def testCatedra04SeJuegaConUnTotalDe100Monedas():
	" Arrange " # Arrange
	nombre_archivo = "Primera_Parte/TestsCatedra/100.txt"
	with open(nombre_archivo, 'r') as archivo:
		primera_linea = archivo.readline() 
	valores_lista = primera_linea.split(";")
	array_100_monedas = [int(valor) for valor in valores_lista]
	
	" Act " # Act
	puntaje_sofia, puntaje_mateo = juego_monedas(array_100_monedas)
	
	" Assert " # Assert
	assert puntaje_sofia > puntaje_mateo

def testCatedra05SeJuegaConUnTotalDe1000Monedas():
	" Arrange " # Arrange
	nombre_archivo = "Primera_Parte/TestsCatedra/1000.txt"
	with open(nombre_archivo, 'r') as archivo:
		primera_linea = archivo.readline()  
	valores_lista = primera_linea.split(";")
	array_1000_monedas = [int(valor) for valor in valores_lista]	
	
	" Act " # Act
	puntaje_sofia, puntaje_mateo = juego_monedas(array_1000_monedas)
	
	" Assert " # Assert
	assert puntaje_sofia > puntaje_mateo

def testCatedra06SeJuegaConUnTotalDe10000Monedas():
	" Arrange " # Arrange
	nombre_archivo = "Primera_Parte/TestsCatedra/10000.txt"
	
	with open(nombre_archivo, 'r') as archivo:
		primera_linea = archivo.readline() 
	valores_lista = primera_linea.split(";")
	array_10000_monedas = [int(valor) for valor in valores_lista]

	" Act " # Act
	puntaje_sofia, puntaje_mateo = juego_monedas(array_10000_monedas)

	" Assert " # Assert
	assert puntaje_sofia > puntaje_mateo

def testCatedra07SeJuegaConUnTotalDe20000Monedas():
	" Arrange " # Arrange
	nombre_archivo = "Primera_Parte/TestsCatedra/20000.txt"
	with open(nombre_archivo, 'r') as archivo:
		primera_linea = archivo.readline() 
	valores_lista = primera_linea.split(";")
	array_20000_monedas = [int(valor) for valor in valores_lista]

	" Act " # Act
	puntaje_sofia, puntaje_mateo = juego_monedas(array_20000_monedas)

	" Assert " # Assert
	assert puntaje_sofia > puntaje_mateo
