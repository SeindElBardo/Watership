import arbolDistanciaGenetica2 as ae
import random
import math

INCREMENTOVIDA = 0.05

class Individuo():
	def __init__(self, nodo, especie, edad, sexo, cromosoma):
		self.nodo = nodo
		self.cinta = None
		self.edad = edad
		self.sexo = sexo # 1 = Es macho
		self.felicidad = 0
		self.especie = especie
		self.energia = cromosoma["constitucion"]
		self.inventario = 0
		self.cromosoma = cromosoma
		#{
		#'fuerza' : cromosoma["fuerza"],
		#'destreza' : cromosoma["destreza"],
		#'constitucion' : cromosoma["constitucion"],
		#'velocidad' : cromosoma["velocidad"],
		#'inteligencia' : cromosoma["inteligencia"],
		#'percepcion' : cromosoma["percepcion"],
		#'esperanzaVida' : cromosoma["esperanzaVida"],
		#'fecundidad' : cromosoma["fecundidad"],
		#'madurezSexual' cromosoma["madurezSexual"]}
		self.habilidades = self.crearHabilidades()

	def calcularDistancias(self,individuo):
		if individuo.especie is self.especie:
			return self.especie.getDistancia(self.nodo.indice, individuo.nodo.indice)
		return 0

	def fMutar(self, atributo):
		aux = atributo+random.randint(-2, 2)
		return aux if aux >=0 else 0

#Habilidades
	def crearHabilidades(self):
		return {
		"Silflar": 0,
		"iniciativa": self.cromosoma["percepcion"] if self.edad >= self.cromosoma["madurezSexual"] else 0,
		"Defender": 0}

	def getBonus(self, habilidad):
		i = 10
		level = 0
		while i < habilidad:
			i += i
			level+= 1
		return level

	def getCapacidadCarga(self):
		return (self.cromosoma["fuerza"] + self.cromosoma["constitucion"]+min(self.edad,10))

	def getCapacidadEnergia(self):
		return (self.cromosoma["constitucion"]*2+min(self.edad,10))


#Reproducción
	#TODOS LOS METODOS DE ACCUION DEBEN RESTAR LA ENERGIA NECESARIA E INCREMENTAR LA felicidad
	def isFertil(self):
		return ((not self.cinta) and (self.edad >= self.cromosoma["madurezSexual"]))

	def danzaDelVientre(self):
		if not self.isAlive():
			print (self.nodo.indice)
			print ("Ha muerto")
			return None
		self.energia -= 4
		print (self.nodo.indice)
		print ("DdV")

	def procrear(self,individuo):
		if not self.isAlive():
			print (self.nodo.indice)
			print ("Ha muerto")
			return None
		if self.isFertil() and individuo.isFertil():
			self.energia -= 4
			self.felicidad += 10
			#individuo.energia -= 4 Esto se resta en la accion de danza vientre
			individuo.felicidad += 10
			if self.sexo: # Es macho
				individuo.cinta = (self, individuo.edad + 4) # el segundo numero es la edad de parir
				self.cinta = 1 # No queremos machos promiscuos
			else:
				self.cinta = (individuo, self.edad + 4)
				individuo.cinta = 1
		else:
			self.energia -= 4
		print (self.nodo.indice)
		print ("procrear")

	def cruce(self, cromosoma1, cromosoma2):
		""" Hay que añadir mutación y quiza deberíamos generalizar más porque en parir la cria se crea con todos los atributos"""
		genes = {}
		keys = list(cromosoma1.keys())
		for key in keys:
			if random.randrange(0,2):
				genes[key] = self.fMutar(cromosoma1[key])
			else:
				genes[key] = self.fMutar(cromosoma2[key])

		return genes
		
	def parir(self): # Habrá que cambiarlo para camadas
		""" 
		Se usa el padre que esta en cinta y se generan tantas crias como en la fecundidad
		Se devuelven listas ya que a este metodo se le llama desde nuevo lo que sea"""
		crias = []
		if self.cinta:
			print (self.nodo.indice)
			self.felicidad += 10
			if self.sexo:
				self.cinta = None
			elif self.cinta[1] == self.edad:
				for i in range(0, math.ceil((self.cromosoma["fecundidad"]+self.cinta[0].cromosoma["fecundidad"])/2)):
					nodo = ae.Nodo(self.nodo, self.cinta[0].nodo, self.especie)
					print ("PARIENDO")
					print(nodo.indice)
					genes = self.cruce(self.cromosoma, self.cinta[0].cromosoma)
					crias.append(Individuo(nodo, self.especie, 0, random.randrange(0,2), genes))
				self.cinta = None
		return crias

#Alimentación
	def comer(self):
		"""Plantear niveles de urgencia para ver cuanto gasta"""
		if not self.isAlive():
			print (self.nodo.indice)
			print ("Ha muerto")
			return None
		merienda = min(self.getCapacidadEnergia()-self.energia, self.inventario)
		self.energia += merienda if not self.cinta else merienda/2
		self.inventario -= merienda
		self.felicidad += 2
		print (self.nodo.indice)
		print ("comer")

	def darComida(self, receptor):
		"""Quiza se debería regular más la cantidad de comida entregada"""
		if (not self.isAlive()) or (not receptor.isAlive()):
			self.felicidad -= 2*self.calcularDistancias(receptor)
			print (self.nodo.indice)
			print ("Ha muerto")
			return None
		self.energia -= 2
		espacio = receptor.getCapacidadCarga()-receptor.inventario
		regalo = min(espacio,self.inventario)
		self.inventario -= regalo
		receptor.inventario += regalo
		self.felicidad += regalo*self.calcularDistancias(receptor)
		print (self.nodo.indice)
		print ("DarComida")

	def llorar(self):
		if not self.isAlive():
			print (self.nodo.indice)
			print ("Ha muerto")
			return None
		self.energia -= 1
		print (self.nodo.indice)
		print ("llorar")


# Vivir
	def isAlive(self):
		"""Aqui se ve si la edad le pasa factura"""
		if self.energia > 0:
			muerte = (self.edad - self.cromosoma["esperanzaVida"])*INCREMENTOVIDA
			if muerte >= random.random():
				#self.nodo.muerteFamiliar()
				self.energia = -1
				return False
			return True
		else:
			#self.nodo.muerteFamiliar()
			return False

	def crecer(self):
		self.edad+=1
		self.felicidad -= 5
		if self.edad == self.cromosoma["madurezSexual"]:
			self.habilidades["iniciativa"] += self.cromosoma["percepcion"]
			self.felicidad = 50

	def vivir(self):
		self.crecer()
		return self.parir()
		
	def serComido(self, dolor):
		"""En esta versión los conejos que son cazados son completamente devorados
		El dolor es un bonus por aprovechar bien la carne"""
		bonus = 5 if self.cinta != (0 or 1) else 0

		comida = self.cromosoma["constitucion"] + min(self.edad, self.cromosoma["esperanzaVida"]/3)+dolor+self.energia
		self.energia =-1
		return comida


	def migrar(self, viaje, viajes):
		"""Usaremos una lista de viajes, los nomadas son vulnerables completamente
		Puede pasar que uno migre y sus hijos nazcan en el nodo anterior :("""
		if not self.isAlive():
			print (self.nodo.indice)
			print ("Ha muerto")
			return None

		self.energia -= 2
		viajes.append(viaje)
		print (self.nodo.indice)
		print ("migrar")
		

# Acciones
	def getDecision(self, opciones, orgia, llorones, victimas):
		"""Debe dar una tupla con el individuo y la acción que se meterá en una lista"""
		decisiones = [] # Son tuplas (opcion,fitness)
		for opcion in opciones:
			if opcion[0] == None:
				pass

			elif opcion[0] == "Reproducirse": #Reproducirse y DdV van por lo mismo
				decisiones.append(self.wannaFuck(opcion))
			
			elif opcion[0] == "DanzaDelVientre":
				decisiones.append(self.wannaFuck(opcion))

			elif opcion[0] == "Comer":
				decisiones.append(self.wannaEat(opcion))

			elif opcion[0] == "Silflar":
				decisiones.append(self.wannaSilflar(opcion))

			elif opcion[0] == "DarComida":
				decisiones.append(self.wannaDarComida(opcion))

			elif opcion[0] == "Defender":
				decisiones.append(self.wannaProtec(opcion))

			elif opcion[0] == "Esconder":
				decisiones.append(self.wannaHide(opcion))

			elif opcion[0] == "AlarmaHambre":
				decisiones.append(self.wannaCry(opcion))

			elif opcion[0] == "Descansar":
				decisiones.append(self.wannaDescansar(opcion))

			elif opcion[0] == "Migrar":
				decisiones.append(self.wannaMigrar(opcion))

			elif opcion[0] == "Combatir":
				decisiones.append(self.wannaCombatir(opcion))

		decision = self.compararOpciones(decisiones)
		if decision[0] == "DanzaDelVientre":
			orgia.append(self)
		elif decision[0] == "AlarmaHambre":
			llorones.append(self)
		elif decision[0] == "Silflar" and isinstance(self, Zorro):
			victimas.append(decision[1])

		# Hay que añadir las cosas de los lobos, aun me falta añadir como funcionaria todo con herencia
		return decision

	def actuar(self, decision, viajes):
		"""Podriamos haber añadido aqui mejor la comprobación de que estamos vivos"""
		if decision[0] == "Reproducirse": #Reproducirse y DdVientre van por lo mismo
			self.procrear(decision[1])
		
		elif decision[0] == "DanzaDelVientre":
			self.danzaDelVientre()

		elif decision[0] == "Comer":
			self.comer()

		elif decision[0] == "Silflar":
			self.silflar(decision[1])

		elif decision[0] == "DarComida":
			self.darComida(decision[1])

		elif decision[0] == "Defender":
			self.defender(decision[1])

		elif decision[0] == "Esconder":
			self.esconder()

		elif decision[0] == "AlarmaHambre":
			self.llorar()

		elif decision[0] == "Migrar":
			self.migrar(decision[1], viajes)

		elif decision[0] == "Combatir":
			self.combatir(decision[1])

	def compararOpciones(self,opciones):
		opciones.sort(key=lambda opciones: opciones[1], reverse=True)
		#print ("Opciones")
		#print (opciones)
		return opciones[0][0]

	def wannaFuck(self, opcion):
		""" Habría que ver como evaluar si queremos reproducirnos"""
		#if self.energia > getCapacidadEnergia*0.70:
		#	return (opcion, 5) # Por el culo te la hinco, jaja
		#return (opcion, 2)
		if self.energia > self.getCapacidadEnergia()*0.60 and self.inventario > self.getCapacidadCarga()*0.60:
			return (opcion, 9)
		return (opcion, 0)

	def wannaEat(self, opcion):
		""" Habría que ver como evaluar si queremos reproducirnos"""
		if self.energia < self.getCapacidadEnergia()*0.25:
			return (opcion, 10)
		if self.energia < self.getCapacidadEnergia()*0.5:
			return (opcion, 5)
		if self.energia < self.getCapacidadEnergia()*0.75:
			return (opcion, 2)
		return (opcion, 0) 

	def wannaSilflar(self, opcion):
		""" Habría que ver como evaluar si queremos reproducirnos"""
		if self.inventario < self.getCapacidadCarga()*0.25:
			return (opcion, 8)
		if self.inventario < self.getCapacidadCarga()*0.5:
			return (opcion, 3)
		if self.inventario < self.getCapacidadCarga()*0.75:
			return (opcion, 1)
		# Falta añadir como motivan los llorones a buscar comida, por ahora somos felices recogiendo comida
		return (opcion, 0) 

	def wannaDarComida(self, opcion): # llega en opcion[1] una lista de llorones
		opciones = []
		for lloron in opcion[1]:
			opciones.append(self.evaluarCuidarLloron(lloron))
		opciones.sort(key=lambda opciones: opciones[1], reverse=True)
		decision = opciones[0]
		return decision


	def wannaCry(self, opcion):
		""" Habría que ver como evaluar si queremos reproducirnos"""
		return (opcion, 5) # Por el culo te la hinco, jaja

	def wannaDescansar(self,opcion):
		return (opcion, 0)

	def wannaMigrar(self,opcion):
		if self.felicidad < 20:
			return (opcion, 3)
		return (opcion, 1)

	def evaluarCuidarLloron(self, lloron):
		recompensa = self.energia * self.calcularDistancias(lloron)*2
		return (("DarComida", lloron), recompensa)


class Conejo(Individuo):
	"""docstring for Conejo"""
	def __init__(self, nodo, especie, edad, sexo, cromosoma):
		super(Conejo, self).__init__(nodo, especie, edad, sexo, cromosoma)
		self.escondido = False

	def evaluarCuidarVictima(self, victima):
		distancia = self.calcularDistancias(victima)
		if distancia == 1:
			return (("Defender", victima), 0)
		recompensa = self.energia * self.calcularDistancias(victima)*3 #No vamos a tener en cuenta la edad porque aumenta mucho la complejidad
		return (("Defender", victima), recompensa)

	def wannaProtec(self, opcion):
		opciones = []
		for victima in opcion[1]:
			opciones.append(self.evaluarCuidarVictima(victima))
		opciones.sort(key=lambda opciones: opciones[1], reverse=True)
		decision = opciones[0]
		return decision

	def wannaHide(self,opcion):
		return (opcion, 11)

	def silflar(self, victima):
		if not self.isAlive():
			print (self.nodo.indice)
			print ("Ha muerto")
			return None
		self.energia -= 2
		self.felicidad += 2
		comida = victima.serComido(self.cromosoma["destreza"]+ self.cromosoma["inteligencia"]*2+self.getBonus(self.habilidades["Silflar"]))
		self.habilidades["Silflar"] += comida
		self.inventario = min(self.inventario+comida, self.getCapacidadCarga())
		print (self.nodo.indice)
		print ("silflar")

	def parir(self): # Habrá que cambiarlo para camadas
		""" 
		Se usa el padre que esta en cinta y se generan tantas crias como en la fecundidad
		Se devuelven listas ya que a este metodo se le llama desde nuevo lo que sea"""
		crias = []
		self.escondido = False # ESTO NO DEBERIA ESTAR AQUI
		if self.cinta:
			self.felicidad += 10
			if self.sexo:
				self.cinta = None
			elif self.cinta[1] == self.edad:
				for i in range(0, math.ceil((self.cromosoma["fecundidad"]+self.cinta[0].cromosoma["fecundidad"])/2)):
					nodo = ae.Nodo(self.nodo, self.cinta[0].nodo, self.especie)
					print ("PARIENDO")
					print(nodo.indice)
					genes = self.cruce(self.cromosoma, self.cinta[0].cromosoma)
					crias.append(Conejo(nodo, self.especie, 0, random.randrange(0,2), genes))
				self.cinta = None
		return crias

	def esconder(self):
		self.escondido = True

	def defender(self, receptor):
		if not self.isAlive():
			print (self.nodo.indice)
			print ("Ha muerto")
			return None
		self.esconder()
		receptor.esconder()
		self.energia -= 5
		self.felicidad += 5*self.calcularDistancias(receptor)
		print (self.nodo.indice)
		print ("defender")

class Zorro(Individuo):
	"""docstring for Zorro"""
	def __init__(self, nodo, especie, edad, sexo, cromosoma):
		super(Zorro, self).__init__(nodo, especie, edad, sexo, cromosoma)

	def silflar(self, victima):
		"""Para los zorros es cazar"""
		if not self.isAlive():
			print (self.nodo.indice)
			print ("Ha muerto")
			return None
		self.energia -= 2
		if victima.escondido:
			print ("Sa escapado")
			return
		self.felicidad += 2
		comida = victima.serComido(self.cromosoma["destreza"]+self.getBonus(self.habilidades["Silflar"]))
		self.habilidades["Silflar"] += comida
		self.inventario = min(self.inventario+comida, self.getCapacidadCarga())
		print (self.nodo.indice)
		print ("silflar")

	def parir(self): # Habrá que cambiarlo para camadas
		""" 
		Se usa el padre que esta en cinta y se generan tantas crias como en la fecundidad
		Se devuelven listas ya que a este metodo se le llama desde nuevo lo que sea"""
		crias = []
		if self.cinta:
			self.felicidad += 10
			if self.sexo:
				self.cinta = None
			elif self.cinta[1] == self.edad:
				for i in range(0, math.ceil((self.cromosoma["fecundidad"]+self.cinta[0].cromosoma["fecundidad"])/2)):
					nodo = ae.Nodo(self.nodo, self.cinta[0].nodo, self.especie)
					print ("PARIENDO")
					print(nodo.indice)
					genes = self.cruce(self.cromosoma, self.cinta[0].cromosoma)
					crias.append(Zorro(nodo, self.especie, 0, random.randrange(0,2), genes))
				self.cinta = None
		return crias

class DawkinsEEE(Individuo):
	"""docstring for DawkinsEEE"""
	def __init__(self, nodo, especie, edad, sexo, cromosoma):
		super(DawkinsEEE, self).__init__(nodo, especie, edad, sexo, cromosoma)
		#0 es paloma
		#1 es halcon

	def vivir(self):
		self.felicidad = 0
		return self.parir()

	def parir(self):
		nodo = ae.Nodo(None, None, self.especie)
		genes = self.cromosoma
		return [DawkinsEEE(nodo, self.especie, self.cromosoma["madurezSexual"], random.randrange(0,2), genes)]

	def combatir(self,victimas):
		#print("combate")
		#print(str(self.cromosoma["estrategia"]) + " VS " + str(victima.cromosoma["estrategia"]))
		#print(str(self.felicidad) + "  " + str(victima.felicidad))
		for victima in victimas:
			if self.cromosoma["estrategia"] == 0:
				if victima.cromosoma["estrategia"] == 0: # paloma VS paloma
					if random.randrange(0,2):
						self.felicidad += 40
						victima.felicidad -= 10
					else:
						victima.felicidad += 40
						self.felicidad -= 10
				else: # paloma VS halcón
					victima.felicidad += 50
			else:
				if victima.cromosoma["estrategia"] == 0: # halcón VS paloma
					self.felicidad += 50
				else: # halcón VS halcón
					if random.randrange(0,2):
						self.felicidad += 50
						victima.felicidad -= 100
					else:
						victima.felicidad += 50
						self.felicidad -= 100
			print(str(self.felicidad) + "  " + str(victima.felicidad))

	def wannaCombatir(self, opcion):
		return (opcion, 100)
