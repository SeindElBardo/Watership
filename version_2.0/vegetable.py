#from genes import genomes_crossing, rabbit_genome
from math import floor
from config import * # Dicen que hacer esto es feo, pero me parece necesario

class Vegetable(object):
    def __init__(self, carbohydrates, proteins, fats, vitamins, minerals, energy, age, size, genetic_node, genome):
        self.nutrients      = {'carbohydrates' : carbohydrates, 'proteins' : proteins, 'fats' : fats, 'vitamins' : vitamins, 'minerals' : minerals}
        self.energy         = energy
        self.toxicity       = 0
        self.age            = age
        self.size           = size
        self.produce        = []
        self.genetic_node   = genetic_node # Se usa la versión de los vegetales para controlar a que especie pertenecen
        self.genome         = genome

    def toxicity_penalty(self):
        return floor(self.toxicity / par_toxicity_to_health_ratio)

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

    def is_alive(self):
        if self.energy > 0:
            return True
        return False

    def is_eatable(self):
        return self.is_alive()