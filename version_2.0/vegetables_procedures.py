from math import floor
import copy
import genes
import genetic_tree as gt
from config import * # Dicen que hacer esto es feo, pero me parece necesario
from aliment import Aliment, AlimentSource

class Procedures():
    # Convertir en alimento
    def be_eaten(self, territory):
        aliment_units = self.size / par_size_to_food_ratio
        nutrients = {
            'carbohydrates': floor((self.nutrients['carbohydrates'] / aliment_units) + ((self.energy / aliment_units) / 2) / par_energy_by_carbohydrate),
            'proteins'     : floor((self.nutrients['proteins'] / aliment_units)), # Si se cambia las proteinas necesarias para crecer, hay que añadir ese valor aquí
            'fats'         : floor((self.nutrients['fats'] / aliment_units) + ((self.energy / aliment_units) / 2) / par_energy_by_fat),
            'vitamins'     : floor(self.nutrients['vitamins'] / aliment_units),
            'minerals'     : floor(self.nutrients['minerals'] / aliment_units)}
        # Reflejamos la perdida de nutrientes y tamaño
        self.nutrients['carbohydrates'] -= nutrients['carbohydrates']
        self.nutrients['proteins']      -= nutrients['proteins']
        self.nutrients['fats']          -= nutrients['fats']
        self.nutrients['vitamins']      -= nutrients['vitamins']
        self.nutrients['minerals']      -= nutrients['minerals']
        self.size -= self.genome['constitution_growth_rate']
        if self.size < 0:
            self.to_die(territory)
        return Aliment(self.genetic_node.species, nutrients)

       
    # Reproducirse
    def to_reproduce(self, territory):
        for i in range(self.genome['fertility']):
            sprout = copy.copy(self)
            sprout.__init__(100, 100, 100, 100, 100, 100, 0, 1, self.genetic_node, genes.genomes_crossing(self.genome, self.genome)) # Se realiza una copia e inicialización para mantener el tipo de objeto (si existe una manera mejor, lo ignoro)
            territory.elements['vegetables'].append(sprout)


    # Morir
    def to_die(self, territory):
        territory.elements['vegetables'].remove(self)
        self.energy = -9000