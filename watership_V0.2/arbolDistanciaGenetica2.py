class ArbolEspecie():
	def __init__(self):
		self.matrizGenetica = []
		self.listaIndicesLibres = []
		self.listaNodos = []

	def getIndice(self):
		if self.listaIndicesLibres:
			return self.listaIndicesLibres.pop()
		self.matrizGenetica.append([]) # Añadimos la nueva fila
		self.listaNodos.append("x") # Es necesario crear la posicion
		return len(self.matrizGenetica)-1

	def getDistancia(self, indice1, indice2):
		return self.matrizGenetica[indice1][indice2]


class Nodo():
	def __init__(self, padre1, padre2, especie):
		self.indice = 1#especie.getIndice()
		self.padres = (padre1, padre2) # referencias a los nodos de los padres
		self.especie = especie
		#self.actualizarMatriz()	
		#self.especie.listaNodos[self.indice] = self

	def getParents(self):
		if None in self.padres:
			return []
		return list(self.padres)

	def actualizarMatriz(self):
		ascendencia = self.obtenerAscendencia()
		esNuevaColumna = self.indice == len(self.especie.matrizGenetica)-1 # Vemos si hay que añadir nuevas columnas o sobreescribir

		for i in range(0, len(self.especie.matrizGenetica)):
			if self.indice != i:
				distancia = self.calcularDistancia(self.especie.listaNodos[i],ascendencia) #VAMOS A CAMBIAR ESTO, CUIDAO
			else:
				distancia = 1
			if esNuevaColumna:
				if i == self.indice:
					self.especie.matrizGenetica[i].append(distancia)
				else:
					self.especie.matrizGenetica[i].append(distancia)
					self.especie.matrizGenetica[self.indice].append(distancia)
			else:
				self.especie.matrizGenetica[i][self.indice] = distancia
				self.especie.matrizGenetica[self.indice][i] = distancia

	def calcularDistancia(self, individuo, ascendenciaSelf):
		if not self.getParents:
			return 0
		#individuo = self.especie.listaNodos[indice] # obtenemos el individuo correspondiente al indice. YA NO
		ascendenciaIndice = individuo.obtenerAscendencia()
		distancias = [] # Pueden darse varias coincidencias, así que nos quedaremos con la mejor
		distanciaSelf = 1
		distanciaIndice = 1
		for i in range(0, len(ascendenciaSelf)): # Comprobamos si son descendientes directos
			if individuo in ascendenciaSelf[i]:
				return (1/(2**(i+1)))
		# Comprobamos relacion familiar indirecta
		for i in ascendenciaSelf:
			for j in ascendenciaIndice:
				auxDistancia = len([ x for x in i if x in j ]) # Contamos ascendentes comunes
				if  auxDistancia == 1:
					distancias.append(1/(2**(distanciaSelf+distanciaIndice)))
				elif auxDistancia > 1: # Si tiene más de una coincidencia pensaremos que tienen 2 familiares en común y por tanto la distancia se multiplica por 2.
					distancias.append(1/(2**(distanciaSelf+distanciaIndice-1)))
				distanciaIndice +=1
			distanciaIndice = 1
			distanciaSelf +=1
		if distancias: # Si no hay datos en distancias es que no tienen niguna relación
			return max(distancias)
		return 0




	"""
	Utilizando estos 2 metodos obtendremos una lista con listas de padres
	abuelos, bisabuelos y tatarabuelos.
	"""
	def obtenerAscendencia(self): # -1 = yo, 0 = papas, 1 = abuelos, 2 = bisabuelos, 3 = tatarabuelo
		if self.padres[0] == None:
			return []
		generacion = 0
		ascendencia = []
		ascendencia.append(self.getParents())
		while generacion < 3:
			auxlist = self.obtenerAscendenciaDirecta(ascendencia[generacion])
			if auxlist:
				ascendencia.append(auxlist)
				generacion+=1
			else:
				generacion = 8000 # Si no hay ascendentes salimos
		return ascendencia

	def obtenerAscendenciaDirecta(self, descendientes):
		ascendenciaDirecta = []
		for i in descendientes:
			ascendenciaDirecta += i.getParents()
		return ascendenciaDirecta

	def muerteFamiliar(self):
		for i in range(0, len(self.especie.matrizGenetica)):
			self.especie.matrizGenetica[i][self.indice] = 0
			self.especie.matrizGenetica[self.indice][i] = 0
		self.especie.listaNodos[self.indice] = None
		self.especie.listaIndicesLibres.append(self.indice)


#_## PRUEBAS
#_#m1= [[1, 0, 0, 0.5, 0, 0, 0.25, 0.125],
#_#	[0, 1, 0, 0.5, 0.5, 0.5, 0.25, 0.25],
#_#	[0, 0, 1, 0, 0.5, 0.5, 0.25, 0.25],
#_#	[0.5, 0.5, 0, 1, 0.25, 0.25, 0.5, 0.25],
#_#	[0, 0.5, 0.5, 0.25, 1, 0.5, 0.5, 0.25],
#_#	[0, 0.5, 0.5, 0.25, 0.5, 1, 0.25, 0.5],
#_#	[0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 1, 0.5],
#_#	[0.125, 0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 1]]
#_#m2= [[1, 0, 0, 0, 0, 0, 0.25, 0.125],
#_#[0, 1, 0, 0, 0.5, 0.5, 0.25, 0.25],
#_#	[0, 0, 1, 0, 0.5, 0.5, 0.25, 0.25],
#_#	[0, 0, 0, 0, 0, 0, 0, 0],
#_#	[0, 0.5, 0.5, 0, 1, 0.5, 0.5, 0.25],
#_#	[0, 0.5, 0.5, 0, 0.5, 1, 0.25, 0.5],
#_#	[0.25, 0.25, 0.25, 0, 0.5, 0.25, 1, 0.5],
#_#	[0.125, 0.25, 0.25, 0, 0.25, 0.5, 0.5, 1]]
#_#m3= [[1, 0, 0, 0.125, 0, 0, 0.25, 0.125],
#_#	[0, 1, 0, 0.25, 0.5, 0.5, 0.25, 0.25],
#_#	[0, 0, 1, 0.25, 0.5, 0.5, 0.25, 0.25],
#_#	[0.125, 0.25, 0.25, 1, 0.25, 0.5, 0.5, 0.5],
#_#	[0, 0.5, 0.5, 0.25, 1, 0.5, 0.5, 0.25],
#_#	[0, 0.5, 0.5, 0.5, 0.5, 1, 0.25, 0.5],
#_#	[0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 1, 0.5],
#_#	[0.125, 0.25, 0.25, 0.5, 0.25, 0.5, 0.5, 1]]
#_#especie = ArbolEspecie()
#_#pepe = Nodo(None,None,especie)
#_#pepa = Nodo(None,None,especie)
#_#pepo = Nodo(None,None,especie)
#_#pipi = Nodo(pepe,pepa,especie)
#_#popo = Nodo(pepo,pepa,especie)
#_#popo2 = Nodo(pepo,pepa,especie)
#_#pepin = Nodo(pipi,popo,especie)
#_#pepinio = Nodo(pepin,popo2,especie)
#_#print (especie.matrizGenetica)
#_#if especie.matrizGenetica == m1:
#_#	print("SUCCESSFUL")
#_#pipi.muerteFamiliar()
#_#print (especie.matrizGenetica)
#_#if especie.matrizGenetica == m2:
#_#	print("SUCCESSFUL")
#_#pepinio2 = Nodo(pepin,popo2,especie)
#_#print (especie.matrizGenetica)
#_#if especie.matrizGenetica == m3:
#_#	print("SUCCESSFUL")

# [0.125, 0.25, 0.25, 1, 0.25, 0.5, 0.5, 0.5, ]]
# [0.125, 0.25, 0.25, 1, 0.25, 0.5, 0.5, 0.5]
#pandoc planteamientoTFG.md --latex-engine=xelatex -o planteamientoTFG.pdf
