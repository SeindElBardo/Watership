from math import floor, log
from config import * # Dicen que hacer esto es feo, pero me parece necesario

class Processes():
    # Vivir
    def to_live(self, territory, light, temperature):
        """
        Vivir es la función que engloba todos los procesos para que se realicen en la iteración.
        to_live determina el orden en el que se realizan los procesos.
        """
        self.to_exist(temperature)
        self.to_do_photosynthesis(light)
        self.to_use_nutrients(territory)
        self.to_remove_toxicity()
        self.to_age(territory)
        if not self.is_alive():
            self.to_die(territory)


    # Existir
    def to_exist(self, temperature):
        self.energy -= self.energy_cost_to_exist(temperature)

    def energy_cost_to_exist(self, temperature):
        return max(1, self.comfortable_place(temperature) * floor(1 + self.toxicity_penalty() / 100) * par_uncomfortable_place_penalty)


    # Fotosíntesis
    def to_do_photosynthesis(self, light):
        nutrients_generated = light / par_light_to_nutrients # Este cálculo es común para todas las plantas de la región.
        self.nutrients['carbohydrates'] += floor(nutrients_generated * self.genome['absorption_capacity_carbohydrates'] / 100)
        self.nutrients['proteins']      += floor(nutrients_generated * self.genome['absorption_capacity_proteins'] / 100)
        self.nutrients['fats']          += floor(nutrients_generated * self.genome['absorption_capacity_fats'] / 100)
        self.nutrients['vitamins']      += floor(nutrients_generated * self.genome['absorption_capacity_vitamins'] / 100)
        self.nutrients['minerals']      += floor(nutrients_generated * self.genome['absorption_capacity_minerals'] / 100)


    # Usar nutrientes
    def to_use_nutrients(self, territoty):
        self.nutrients['vitamins'] = max(self.nutrients['vitamins'] - 1, 0)
        self.nutrients['minerals'] = max(self.nutrients['minerals'] - 1, 0)

        over_fat = self.get_over_fat()
        self.toxicity += over_fat
        self.nutrients['fats'] -= over_fat

        if self.nutrients['carbohydrates']:
            self.nutrients['carbohydrates'] -= 1
            self.energy += par_energy_by_carbohydrate
        if (self.energy < par_critical_level_energy) and self.nutrients['fats']:
            self.nutrients['fats'] -= 1
            self.energy += par_energy_by_fat

        if self.nutrients['proteins'] and (self.size < self.genome['maturity_size']):
            self.nutrients['proteins'] -= 1 # Esto hay que revisarlo porque las plantas crecen que dan miedo
            self.size += self.genome['constitution_growth_rate']
        elif (self.nutrients['proteins'] > self.genome['seeds_cost']) and (self.size >= self.genome['maturity_size']):
            self.nutrients['proteins'] -= self.genome['seeds_cost']
            self.to_reproduce(territoty)

    def get_over_fat(self):
        return max(0, self.nutrients['fats'] - self.genome['fat_retention'])


    # Eliminar toxicidad
    def to_remove_toxicity(self):
        toxicity_removed = max(0, floor(((self.nutrients['vitamins'] + self.genome['immune_constitution']) / par_vitamins_to_toxicity_ratio) - (self.toxicity + log(self.toxicity + 1))))
        self.toxicity = max(0, self.toxicity - toxicity_removed)


    # Envejecer
    def to_age(self, territoty):
        self.age += 1
        if self.age == self.genome['life_expectancy']:
            self.to_die(territoty)