from math import floor


class Aliment(object):
    def __init__(self, species, nutrients):
        self.species = species
        self.nutrients = nutrients

class AlimentSource(object):
    def __init__(self, aliment, amount):
        self.species = aliment.species
        self.genetic_node = aliment.species # Esto es una guarrada para que se pueda usar la self.genetic_node = species # Esto es una guarrada para que se pueda usar la misma llamado en plantas que en alimento.misma llamado en plantas que en alimento.
        self.stack = []
        aliment.nutrients['carbohydrates'] = floor(aliment.nutrients['carbohydrates'] / amount)
        aliment.nutrients['proteins']      = floor(aliment.nutrients['proteins'] / amount)
        aliment.nutrients['fats']          = floor(aliment.nutrients['fats'] / amount)
        aliment.nutrients['vitamins']      = floor(aliment.nutrients['vitamins'] / amount)
        aliment.nutrients['minerals']      = floor(aliment.nutrients['minerals'] / amount)
        for i in range(amount):
            self.stack.append(aliment)

    def be_eaten(self):
        return self.stack.pop()
        
    def is_eatable(self):
        return len(self.stack) > 0