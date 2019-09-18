class GeneticTree():
	def __init__(self):
		self.genetic_matrix = []
		self.free_indexes = []
		self.nodes = []

	def get_index(self):
		if self.free_indexes:
			return self.free_indexes.pop()
		self.genetic_matrix.append([]) # Añadimos la nueva fila
		self.nodes.append("x") # Es necesario crear la posicion
		return len(self.genetic_matrix)-1

	def get_distance(self, index_1, index_2):
		return self.genetic_matrix[index_1][index_2]


class Node():
	def __init__(self, parent_1, parent_2, species):
		self.index = species.get_index()
		self.parents = (parent_1, parent_2) # referencias a los Nodes de los parents
		self.species = species
		self.update_matrix()	
		self.species.nodes[self.index] = self
		self.agent = None

	def get_parents(self):
		if None in self.parents:
			return []
		return list(self.parents)

	def update_matrix(self):
		lineage = self.get_lineage()
		is_new_colum = self.index == len(self.species.genetic_matrix)-1 # Vemos si hay que añadir nuevas columnas o sobreescribir

		for i in range(0, len(self.species.genetic_matrix)):
			if self.index != i:
				distance = self.get_distance(self.species.nodes[i],lineage) #VAMOS A CAMBIAR ESTO, CUIDAO
			else:
				distance = 1
			if is_new_colum:
				if i == self.index:
					self.species.genetic_matrix[i].append(distance)
				else:
					self.species.genetic_matrix[i].append(distance)
					self.species.genetic_matrix[self.index].append(distance)
			else:
				self.species.genetic_matrix[i][self.index] = distance
				self.species.genetic_matrix[self.index][i] = distance

	def get_distance(self, agent, self_lineage):
		if not self.get_parents:
			return 0
		lineage_index = agent.get_lineage()
		distances = [] # Pueden darse varias coincidencias, así que nos quedaremos con la mejor
		self_distance = 1
		distance_index = 1
		for i in range(0, len(self_lineage)): # Comprobamos si son descendents directos
			if agent in self_lineage[i]:
				return (1/(2**(i+1)))
		# Comprobamos relacion familiar indirecta
		for i in self_lineage:
			for j in lineage_index:
				aux_distance = len([ x for x in i if x in j ]) # Contamos ascendentes comunes
				if  aux_distance == 1:
					distances.append(1/(2**(self_distance+distance_index)))
				elif aux_distance > 1: # Si tiene más de una coincidencia pensaremos que tienen 2 familiares en común y por tanto la distance se multiplica por 2.
					distances.append(1/(2**(self_distance+distance_index-1)))
				distance_index +=1
			distance_index = 1
			self_distance +=1
		if distances: # Si no hay datos en distances es que no tienen niguna relación
			return max(distances)
		return 0




	"""
	Utilizando estos 2 metodos obtendremos una lista con listas de parents
	abuelos, bisabuelos y tatarabuelos.
	"""
	def get_lineage(self): # -1 = yo, 0 = papas, 1 = abuelos, 2 = bisabuelos, 3 = tatarabuelo
		if self.parents[0] == None:
			return []
		generation = 0
		lineage = []
		lineage.append(self.get_parents())
		while generation < 3:
			auxlist = self.get_direct_lineage(lineage[generation])
			if auxlist:
				lineage.append(auxlist)
				generation+=1
			else:
				generation = 8000 # Si no hay ascendentes salimos
		return lineage

	def get_direct_lineage(self, descendents):
		direct_lineage = []
		for i in descendents:
			direct_lineage += i.get_parents()
		return direct_lineage

	def muerteFamiliar(self):
		for i in range(0, len(self.species.genetic_matrix)):
			self.species.genetic_matrix[i][self.index] = 0
			self.species.genetic_matrix[self.index][i] = 0
		self.species.nodes[self.index] = None
		self.species.free_indexes.append(self.index)

class VegetableNode():
	def __init__(self, species):
		self.species = species

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
#_#species = GeneticTree()
#_#pepe = Node(None,None,species)
#_#pepa = Node(None,None,species)
#_#pepo = Node(None,None,species)
#_#pipi = Node(pepe,pepa,species)
#_#popo = Node(pepo,pepa,species)
#_#popo2 = Node(pepo,pepa,species)
#_#pepin = Node(pipi,popo,species)
#_#pepinio = Node(pepin,popo2,species)
#_#print (species.genetic_matrix)
#_#if species.genetic_matrix == m1:
#_#	print("SUCCESSFUL")
#_#pipi.muerteFamiliar()
#_#print (species.genetic_matrix)
#_#if species.genetic_matrix == m2:
#_#	print("SUCCESSFUL")
#_#pepinio2 = Node(pepin,popo2,species)
#_#print (species.genetic_matrix)
#_#if species.genetic_matrix == m3:
#_#	print("SUCCESSFUL")

# [0.125, 0.25, 0.25, 1, 0.25, 0.5, 0.5, 0.5, ]]
# [0.125, 0.25, 0.25, 1, 0.25, 0.5, 0.5, 0.5]
#pandoc planteamientoTFG.md --latex-engine=xelatex -o planteamientoTFG.pdf
