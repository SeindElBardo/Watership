from math import floor
import copy
from config import * # Dicen que hacer esto es feo, pero me parece necesario
import genes
import genetic_tree as gt
from aliment import Aliment, AlimentSource

class Procedures():
    # Convertir en alimento
    def to_become_food(self):
        self.nutrients['proteins']      += floor((self.muscles['upper'] + self.muscles['upper']) / par_proteins_to_muscles_ratio)
        self.nutrients['carbohydrates'] += floor((self.energy / 2)) / par_energy_by_carbohydrate
        self.nutrients['fats']          += floor((self.energy / 2)) / par_energy_by_fat
        return AlimentSource(Aliment(self.genetic_node.species, self.nutrients), floor(self.size / par_size_to_food_ratio))

    # Madurar
    def to_mature(self):
        self.size = ((2 ** (self.get_size_category() + 1)) * par_minimum_size_category) * (1 + self.genome['constitution_size_modification'] / 100)
        
    # Reproducirse
    def to_reproduce(self, partner):
        if self.genome['sex']: # Es macho
            female = partner
            male = self
        else:
            female = self
            male = partner

        male.pregnant = -1 # No queremos machos promiscuos
        female.pregnant = []
        num_offsprings = min(male.genome['fertility'], female.genome['fertility'])
        for i in range(num_offsprings):
            offspring = copy.copy(female)
            offspring.__init__(100, 100, 100, 100, 100, 100, 0, 100, 100, gt.Node(male.genetic_node, female.genetic_node, male.genetic_node.species), genes.genomes_crossing(female.genome, male.genome)) # Se realiza una copia e inicialización para mantener el tipo de objeto (si existe una manera mejor, lo ignoro)
            female.pregnant.append(offspring) 
            female.memories.to_broatcast_birth_to_family(offspring) # Se informa a toda la familia y vecinos de que viene un nuevo agente.


    # Dar a luz
    def to_give_birth(self, territory):
        while self.pregnant:
            territory.append_animal(self.pregnant.pop())
        self.pregnant = 0


    # Morir
    def to_die(self, territory):
        territory.remove_animal(self)
        territory.elements['aliments'].append(self.to_become_food())
        self.energy = - 9000 # Señal de estar muerto
        self.memories.to_broatcast_death_to_family(self) # Se informa a toda la familia y vecinos de que el agente ha muerto.
        if (type(self.pregnant) is list):
            for unborn in self.pregnant:
                unborn.memories.to_broatcast_death_to_family(self) # Se informa a toda la familia y vecinos de que los niños han muerto.