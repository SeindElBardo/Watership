import math
import random


class Planta():
	"""Las plantas tienen 3 atributos,las esporas designan la cantidad de individuos
	que genera al reproducirse. Para reproducirse la salud debe ser igual al valor
	de madurez, y en cada asalto se regenerará o crecerá el valor de crecimiento.
	Cuando la salud llega a 0, la planta ha sido devorada por completo y muere."""
	def __init__(self, esporas, madurez, crecimiento, salud):
		self.cromosoma = {
		'esporas': esporas, # Cantidad de individuos que genera al reproducirse
		'madurez': madurez, # Estado de salud en el que puede reproducirse (es el maximo)
		'crecimiento': crecimiento} # Cantidad de salud que recupera por asalto
		self.salud = salud

	def vivir(self):
		"""Se usa el valor de crecimiento para sumarlo a la salud y se hace una proporcion
		de lo sobrante para reproducción parcial"""
		if self.cromosoma['madurez'] < (self.salud + self.cromosoma['crecimiento']):
			aux = self.salud + self.cromosoma['crecimiento'] - self.cromosoma['madurez']
			aux2 = self.cromosoma['crecimiento'] - aux
			aux = 1-aux2/aux
			self.salud = self.cromosoma['madurez']
			return self.reproducir(math.floor(self.cromosoma['esporas']*aux))
		else:
			self.salud += self.cromosoma['crecimiento']
			return []

	def fMutacion(self, atributo):
		"""Esta función sirve para generar una mutación en los atributos según la siguiente función"""
		aux = atributo+random.randint(-2, 2)
		return aux if aux >=0 else 0

	def reproducir(self, esporas):
		plantitas = []
		for i in range(0,esporas):
			plantitas.append(Planta(self.fMutacion(self.cromosoma['esporas']), self.fMutacion(self.cromosoma['madurez']), self.fMutacion(self.cromosoma['crecimiento']), 1))
		return plantitas

	def serComido(self, dolor):
		"""La salud de la planta es comida, no puede dar más comida que salud, y si la salud llega a 0 muere"""
		if self.salud > 0:
			if (self.salud - dolor) >= 0:
				self.salud -= dolor
				return dolor
			else:
				aux = self.salud
				self.salud = 0
				return aux
		else:
			 return 0

	def isAlive(self):
		return bool(self.salud > 0)
