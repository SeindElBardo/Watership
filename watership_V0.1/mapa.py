import random

class Territorio():
	def __init__(self, limit, agua, madriguera, vecinos):
		self.zorros = []
		self.conejos = []
		self.plantas = []
		self.limit = limit
		self.agua = agua # true o false
		self.madriguera = madriguera # valor que pondera la fuerza defensiva o evasiva de los conejos
		self.vecinos = []
		self.linkarVecinos(vecinos)

	def linkarVecinos(self, vecinos):
		for i in vecinos:
			self.vecinos.append(i)
			i.vecinos.append(self)

	def viajar(self, individuo, vecino):
		if not individuo.isAlive():
			return None
		if individuo in self.conejos:
			self.conejos.remove(individuo)
			vecino.conejos.append(individuo)
		else:
			self.zorros.remove(individuo)
			vecino.zorros.append(individuo)

	def morirPlanta(self, individuo):
		self.plantas.remove(individuo)

	def morirConejo(self, individuo):
		self.conejos.remove(individuo)

	def morirZorro(self, individuo):
		self.zorros.remove(individuo)



# Funciones de añadir individuos, reciben listas
	def newZorro(self,individuos):
		self.zorros += individuos

	def newConejo(self,individuos):
		self.conejos += individuos

	def newPlanta(self,individuos):
		self.plantas += individuos[:(self.limit-len(self.plantas))]

	def elMundoSeMueve(self):
		"""Retiramos del mapa los seres que hayan muerto, en futuras versiones debería haber una lista de seres y esto debería recorrer cada lista"""
		nuevasPlantas = []
		for planta in self.plantas:
			if planta.isAlive():
				nuevasPlantas.append(planta)
		self.plantas = nuevasPlantas
		for planta in self.plantas:
			self.newPlanta(planta.vivir())
		nuevosConejos = []
		for conejo in self.conejos:
			if conejo.isAlive():
				nuevosConejos.append(conejo)
				nuevosConejos += conejo.vivir()
		self.conejos = nuevosConejos

		nuevosZorros = []
		for zorro in self.zorros:
			if zorro.isAlive():
				nuevosZorros.append(zorro)
				nuevosZorros += zorro.vivir()
		self.zorros = nuevosZorros

# Funciones de flujo
	def getDeclaraciones(self):
		"""Inspirado en el sistema de algunos juegos de rol, cada individuo declara intenciones según su percepción, y después las hace según su velocidad"""
		declaracion = self.zorros[:]	+ self.conejos[:]
		#accion = self.lobos[:]	+ self.conejos[:]
		declaracion.sort(key=lambda individuo: individuo.habilidades["iniciativa"])
		for i in declaracion:
			print (str(i) + " " + str(i.nodo.indice))
			print(i.habilidades["iniciativa"])
		print ("\n")
		#accion.sort(key=lambda individuo: individuo.cromosoma["velocidad"], reverse=True)
		return declaracion

	def getIniciativas(self, acciones):
		acciones.sort(key=lambda acciones: acciones[0].cromosoma["velocidad"], reverse=True)



	def getAcciones(self, individuo, orgia, llorones, victimas):
		"""En el flujo debería ir obtener acciones y depués elegir cual hacer
		Devolvera una tupla con una lista de accciones posibles
		"""

		reproducirse = self.canReproducirse(individuo, orgia)
		buscarComida = self.canSearchFood(individuo)
		comer = self.canEat(individuo)
		llorar = self.canAlarmarHambre(individuo)
		darComida = self.canGiveFood(individuo, llorones)
		esconder = self.canHide(individuo, victimas)
		proteger = self.canProtec(individuo,victimas)
		descansar = self.canSleep(individuo)
		migrar = self.canMove(individuo)

		return (reproducirse, buscarComida, comer, llorar, darComida, descansar, migrar, esconder, proteger)

	def canHide(self,individuo,victimas):
		if (individuo.edad >= individuo.cromosoma["madurezSexual"]) and (individuo in victimas):
			return ("Esconder",)
		return (None,)

	def canProtec(self,individuo, victimas):
		if individuo.edad < individuo.cromosoma["madurezSexual"]:
			return (None,)
		if victimas and individuo in self.conejos:
			return ("Defender", victimas)
		return (None,)


	def canMove(self,individuo):
		if individuo.edad >= individuo.cromosoma["madurezSexual"] and self.vecinos:
			return ("Migrar", (self, individuo, random.choice(self.vecinos)))
		return (None,) 

	def canEat(self,individuo):
		if individuo.inventario:
			return ("Comer",)
		return (None,)

	def canGiveFood(self,individuo, llorones):
		if individuo.edad < individuo.cromosoma["madurezSexual"]:
			return (None,)
		if individuo.inventario and llorones:
			return ("DarComida", llorones)
		return (None,)

	def canSearchFood(self,individuo): #Para los lobos será distinto. Hay que añadir edad
		if individuo.edad < individuo.cromosoma["madurezSexual"]:
			return (None,)
		if individuo in self.conejos:
			if self.plantas and individuo.inventario < individuo.getCapacidadCarga():
				return ("Silflar", random.choice(self.plantas)) #Entenderemos Silflar como conseguir comida
		if individuo in self.zorros:
			if self.conejos and individuo.inventario < individuo.getCapacidadCarga():
				return ("Silflar", random.choice(self.conejos)) #Entenderemos Silflar como conseguir comida
		return (None,)

	def canReproducirse(self,individuo, orgia):
		if individuo.isFertil():
			"""
			gestionar UNICAMENTE la reproducción por turnos
    Primera version:
        las hembras se ofrecen y los machos escogen aleatoriamente cual montan, el primero en llegar gana
    Segunda version:
        Los conejos dicen me ofrezco o escogo según su genoma, el cual tambien tiene en cuenta el sexo. Hasta mejor opción se siguen escogiendo aleatoriamente.
			"""
			random.shuffle(orgia)
			for vicioso in orgia:
				if vicioso.sexo != individuo.sexo:
					return ("Reproducirse", vicioso)

			return ('DanzaDelVientre',)
		return (None,)

	def canAlarmarHambre(self,individuo):
		if individuo.edad < individuo.cromosoma["madurezSexual"]:
			return ("AlarmaHambre",)
		return (None,)

	def canSleep(self,individuo):
		return ("Descansar",)


"""
Van a existir 2 listas, orgia y llorones, en la primera van entrando y saliendo los que quieran reproducirse, y en la segunda los que pidan ayuda

Los lobos buscan conejos, y habrá otra nueva lista de conejos en peligro que permitirá a los otros conejos ayudar.

Se plantea un par de valores que permitan a los lobos reconocer los mejores conejos y quizá otro par para las plantas
De esta forma se podrían evaluar que presas son mejores que otras. Para las plantas podría ser un número que ponderará la cantidad de alimento recibido
o lo way que es este.
"""
