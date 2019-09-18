from animal import Animal
from processes import Processes
from procedures import Procedures
from actions import Actions
from reasonings import Reasonings
#from genetic_tree import GeneticTree
from config import *
import random

# oryctolagus_cuniculus = GeneticTree()

class Rabbit(Animal, Processes, Procedures, Actions, Reasonings):
    def __init__(self, carbohydrates, proteins, fats, vitamins, minerals, energy, age, upper, lower, genetic_node, genome):
        super(Rabbit, self).__init__(carbohydrates, proteins, fats, vitamins, minerals, energy, age, upper, lower, 1, genetic_node, genome)

rabbit_genome = {   
    'visual_perception'                : 100,
    'sensitivity_light'                : 70,
    'auditory_perception'              : 100,
    'olfactory_perception'             : 100,
    'sensory_perception'               : 100,
    'alert'                            : 100,
    'muscles_upper'                    : 100,
    'muscles_lower'                    : 100,
    'dexterity'                        : 100,
    'intelligence_memory'              : 100,
    'libido'                           : 100,
    'selfish_gen'                      : 100,
    'hungry'                           : 200,
    'provision'                        : 90,
    'fear'                             : -50,
    'aggressiveness'                   : -30,
    'patience'                         : 100,
    'curiosity'                        : 100,
    'immune_constitution'              : 100,
    'estructural_constitution'         : 100,
    'constitution_size_modification'   : 50,
    'constitution_smell_modification'  : 100,
    'constitution_temperature'         : 320,
    'skin_tone'                        : -40,
    'rhythm_growth_1'                  : 100,
    'rhythm_growth_2'                  : 200,
    'rhythm_growth_3'                  : 300,
    'rhythm_growth_4'                  : 400,
    'fertility'                        : 5,
    'sex'                              : random.randint(0, 1),
    'digestive_capacity_carbohydrates' : 60,
    'digestive_capacity_proteins'      : 60,
    'digestive_capacity_fats'          : 60,
    'digestive_capacity_vitamins'      : 60,
    'digestive_capacity_minerals'      : 60,
    'absorption_capacity_carbohydrates': 60,
    'absorption_capacity_proteins'     : 60,
    'absorption_capacity_fats'         : 60,
    'absorption_capacity_vitamins'     : 60,
    'absorption_capacity_minerals'     : 60,
}