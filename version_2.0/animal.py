#from genes import genomes_crossing, rabbit_genome
from math import floor
from memories import Memories
from config import * # Dicen que hacer esto es feo, pero me parece necesario
#import genetic_tree as gt

class Animal(object):
    def __init__(self, carbohydrates, proteins, fats, vitamins, minerals, energy, age, upper, lower, size, genetic_node, genome):
        self.bag            = []
        self.stomach        = [] # Quizá estas dos estén mejor como variables en vez de listas.
        self.bowel          = []
        self.nutrients      = {'carbohydrates' : carbohydrates, 'proteins' : proteins, 'fats' : fats, 'vitamins' : vitamins, 'minerals' : minerals}
        self.pregnant       = 0
        self.energy         = energy
        self.fatigue        = 0
        self.toxicity       = 0
        self.age            = age
        self.maturity_level = 1
        self.inertia        = (('To Rest',), 1)
        self.wounds         = 0
        self.muscles        = {'upper' : upper, 'lower' : lower}
        self.size           = ((2 ** size) * par_minimum_size_category) * (1 + genome['constitution_size_modification'] / 100)
        self.memories       = Memories(genome['intelligence_memory'])
        self.genetic_node   = genetic_node
        self.genome         = genome
        
        self.genetic_node.agent = self

    def get_genetic_distance(self, agent):
        """
        @brief      Calcula la distancia en el árbol genealogico que separa al individuo de agente.
        
        @param      self         The object
        @param      agent        The agent
        
        @return     Distancia genetica que los separa según la propuesta de Dawkins.
        """
        if agent.genetic_node.species is self.genetic_node.species:
            return self.genetic_node.species.get_distance(self.genetic_node.index, agent.genetic_node.index)
        return 0

    def get_perception(self, light):
        """
        @brief      Genera el valor de percepción que se utilizará para determinar el turno en la fase de declaración de intenciones.
        
        @param      self   The object
        @param      light  The light
        
        @return     Puntuación con la que competir en la fase de declaración de intenciones.
        """
        return self.visual_capacity(light) + self.genome['auditory_perception'] + self.genome['olfactory_perception'] + self.genome['sensory_perception'] + self.genome['alert']

    def get_speed(self):
        """
        @brief      Genera el valor de velocidad que se utilizará para determinar el turno en la fase de actuación.
        
        @param      self   The object
        
        @return     Puntuación con la que competir en la fase de actuación.
        """        
        return (self.muscles['upper'] + self.genome['dexterity']) * self.health_condition_penalty()


    def get_size_category(self):
        category = 0
        while self.size >= ((2 ** (category + 1)) * par_minimum_size_category):
            category += 1
        return category

    def get_bab_occupancy_rate(self):
        """
        La capacidad de la mochila, dado que sólo se guardan alimentos, es un cuarto del tamaño del agente, dividido entre el parámetro par_size_by_aliment
        """
        aliments_capacity = floor(self.size / 32)
        return floor((100 * len(self.bag)) / aliments_capacity) # Regla de tres

    def is_alive(self):
        if self.energy > 0:
            return True
        return False

    def fatigue_penalty(self):
        return floor(self.fatigue / par_fatigue_to_health_ratio)

    def toxicity_penalty(self):
        return floor(self.toxicity / par_toxicity_to_health_ratio)

    def maturity_penalty(self):
        if self.maturity_level == 1:
            return par_maturity_level_1_to_health_penalty
        if self.maturity_level == 2:
            return par_maturity_level_2_to_health_penalty
        if self.maturity_level == 3: # En este nivel no hay penalización
            return 100
        if self.maturity_level < 1:
            return 100 + floor(- self.maturity_level / 1440)

    def wounds_penalty(self): # Sólo se utiliza el límite superior porque al hacer return es necesariamente mayor
        if self.wounds < par_scratches_limit_value:
            return par_scratches_penalty
        if self.wounds < par_superficial_wounds_limit_value:
            return par_superficial_wounds_penalty
        if self.wounds < par_serious_wounds_limit_value:
            return par_serious_wounds_penalty
        if self.wounds < par_mortal_wounds_limit_value:
            return par_mortal_wounds_penalty


    def health_condition_penalty(self):
        return (self.fatigue_penalty() + self.toxicity_penalty() + self.maturity_penalty() + self.wounds_penalty()) / 100 + 1

    def comfortable_place(self, temperature):
        """
        @brief      Determina si un lugar es confortable

        Los lugares confortables son aquellos en los que la temperatura está dentro del rango de tolerancia del agente.
        
        @param      self         The object
        @param      temperature  The temperature
        
        @return     Unidades en valor absoluto en las que dista la temperatura del entorno de la que sería confortable para el agente
        """
        if ((self.genome['constitution_temperature'] - par_temperature_tolerance) > temperature) or (temperature > (self.genome['constitution_temperature'] + par_temperature_tolerance)): # Comprueba si la temperatura está fura del rengo de tolerancia.
            return min(abs(temperature - self.genome['constitution_temperature'] - par_temperature_tolerance),
                abs(temperature - self.genome['constitution_temperature'] + par_temperature_tolerance))
        return 0

    def visual_capacity(self, light):
        """
        @brief      Determina cuanto afecta negativamente la luz afecta a la percepción visual en una ciscunstancia concreta.

        Los agentes poseen un gen de sensibilidad a la luz que determina el rango de luminosidad en el que ven perfectamente. Fuera de ese rango sufren penalizaciones a su percepción visual.
        
        @param      self   The object
        @param      light  The light
        
        @return     Valor efectivo de percepción visual.
        """
        if ((self.genome['sensitivity_light'] - par_light_tolerance) > light) or (light > (self.genome['sensitivity_light'] + par_light_tolerance)): # Comprueba si la temperatura está fura del rengo de tolerancia.
            return self.genome['visual_perception'] - min(abs(light - self.genome['sensitivity_light'] - par_light_tolerance),
                abs(light - self.genome['sensitivity_light'] + par_light_tolerance))
        return self.genome['visual_perception']
