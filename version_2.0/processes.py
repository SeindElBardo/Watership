from math import floor, ceil, log
from config import * # Dicen que hacer esto es feo, pero me parece necesario
from animal import Animal

class Processes():
    # Vivir
    def to_live(self, territory, light, temperature): # La temperatura no se usa pero así la llamada es igual que la de los vegetales.
        """
        Vivir es la función que engloba todos los procesos para que se realicen en la iteración.
        to_live determina el orden en el que se realizan los procesos.
        """
        self.to_exist(temperature)
        self.to_digest_food()
        self.to_absorb_nutrients()
        self.to_use_nutrients()
        self.to_remove_toxicity()
        self.to_heal()
        self.to_gestate_offspring(territory)
        self.to_age()
        if not self.is_alive():
            self.to_die(territory)

            
    # Existir
    def to_exist(self, temperature):
        self.energy -= self.energy_cost_to_exist(temperature)
        self.fatigue += self.fatigue_cost_to_exist()

    def energy_cost_to_exist(self, temperature):
        return max(1, len(self.bag) - self.muscles['lower'] * par_muscles_to_carry_ratio) + self.comfortable_place(temperature) * par_uncomfortable_place_penalty

    def fatigue_cost_to_exist(self):
        return max(1, floor(len(self.bag) - self.muscles['lower'] * par_muscles_to_carry_ratio) * self.health_condition_penalty())


    # Gestar Crías
    def to_gestate_offspring(self, territory):
        if type(self.pregnant) is type([]): # Siginifica que es una hembra embarazada
            self.energy -= par_energy_cost_gestate_for_agent * len(self.pregnant)
            for offspring in self.pregnant:
                offspring.energy += par_energy_cost_gestate_for_agent
                offspring.age += 1
                if offspring.age == offspring.genome['rhythm_growth_1']: # Cuando una de las crías tiene que nacer, nacen todas.
                    self.to_give_birth(territory)
                    return
        else:
            self.pregnant += 1 # Cuenta las iteraciones sin procrear


    # Envejecer
    def to_age(self):
        """
        Esta función hay que revisarla ya que no existe un mecanismo que evite que se alcance una fase antes que otra.
        """
        self.age += 1
        if self.age < self.genome['rhythm_growth_1']:
            self.maturity_level = 0
            return
        if self.age < self.genome['rhythm_growth_2']:
            self.maturity_level = 1
            return
        if self.age < self.genome['rhythm_growth_3']:
            self.maturity_level = 2
            if self.age == self.genome['rhythm_growth_2']:
                self.to_mature()
            return
        if self.age <= self.genome['rhythm_growth_4']:
            self.maturity_level = 3
            return
        if self.age > self.genome['rhythm_growth_4']:
            self.maturity_level = self.age - self.genome['rhythm_growth_4']


    # Digerir alimento
    def to_digest_food(self):
        if not len(self.stomach): # Debe haber comida que digerir
            return
        food = self.stomach.pop()
        carbohydrates = ceil(food.nutrients['carbohydrates'] * self.genome['digestive_capacity_carbohydrates'] / 100)
        proteins      = ceil(food.nutrients['proteins'] * self.genome['digestive_capacity_proteins'] / 100)
        fats          = ceil(food.nutrients['fats'] * self.genome['digestive_capacity_fats'] / 100)
        vitamins      = ceil(food.nutrients['vitamins'] * self.genome['digestive_capacity_vitamins'] / 100)
        minerals      = ceil(food.nutrients['minerals'] * self.genome['digestive_capacity_minerals'] / 100)
        toxicity_generated = (food.nutrients['carbohydrates'] - carbohydrates) + (food.nutrients['proteins'] - proteins) + (food.nutrients['fats'] - fats) + (food.nutrients['vitamins'] - vitamins) + (food.nutrients['minerals'] - minerals) # Se aumenta la toxicidad en función de lo no digerido
        self.toxicity += toxicity_generated
        self.memories.to_remember_food(self.age, (food.especies, (carbohydrates, proteins, fats, vitamins, minerals), toxicity_generated))
        self.bowel.append({'carbohydrates' : carbohydrates, 'proteins' : proteins, 'fats' : fats, 'vitamins' : vitamins, 'minerals' : minerals})


    # Absorber nutrientes
    def to_absorb_nutrients(self):
        if not len(self.bowel): # Debe haber nutrientes que absorber
            return
        food_nutrients = self.bowel.pop()
        self.nutrients['carbohydrates'] += ceil(food_nutrients['carbohydrates'] * self.genome['absorption_capacity_carbohydrates'] / 100)
        self.nutrients['proteins']      += ceil(food_nutrients['proteins'] * self.genome['absorption_capacity_proteins'] / 100)
        self.nutrients['fats']          += ceil(food_nutrients['fats'] * self.genome['absorption_capacity_fats'] / 100)
        self.nutrients['vitamins']      += ceil(food_nutrients['vitamins'] * self.genome['absorption_capacity_vitamins'] / 100)
        self.nutrients['minerals']      += ceil(food_nutrients['minerals'] * self.genome['absorption_capacity_minerals'] / 100)


    # Usar nutrientes
    def to_use_nutrients(self):
        self.nutrients['proteins'] = max(self.nutrients['proteins'] - 1, 0)
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

        self.muscles['upper'] = self.get_upper_muscles()
        self.muscles['lower'] = self.get_lower_muscles()

    def get_over_fat(self):
        return max(0, self.nutrients['fats'] - self.size * par_size_to_fats_capacity_ratio)

    def get_upper_muscles(self):
        return floor((self.nutrients['proteins'] + self.genome['muscles_upper']) / par_proteins_to_muscles_ratio)

    def get_lower_muscles(self):
        return floor((self.nutrients['proteins'] + self.genome['muscles_lower']) / par_proteins_to_muscles_ratio)


    # Eliminar toxicidad
    def to_remove_toxicity(self):
        toxicity_removed = max(0, floor(((self.nutrients['vitamins'] + self.genome['immune_constitution']) / par_vitamins_to_toxicity_ratio) - (self.toxicity + log(self.toxicity + 1))))
        self.toxicity = max(0, self.toxicity - toxicity_removed)


    # Sanar heridas
    def to_heal(self):
        if self.wounds == 0:
            return
        if self.nutrients['vitamins'] >= (self.wounds * par_vitamins_to_wounds_ratio - self.genome['immune_constitution']):
            self.wounds -= 1