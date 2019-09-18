from vegetable import Vegetable
from vegetables_processes import Processes
from vegetables_procedures import Procedures
from actions import Actions
from config import *
import random

# ribes_rubrum = GeneticTree()

class Gooseberry(Vegetable, Processes, Procedures):
    def __init__(self, carbohydrates, proteins, fats, vitamins, minerals, energy, age, size, genetic_node, genome):
        super(Gooseberry, self).__init__(carbohydrates, proteins, fats, vitamins, minerals, energy, age, size, genetic_node, genome)


gooseberry_genome = {
    'immune_constitution'              : 100,
    'constitution_smell_modification'  : 100,
    'constitution_temperature'         : 320,
    'fertility'                        : 5,
    'absorption_capacity_carbohydrates': 60,
    'absorption_capacity_proteins'     : 60,
    'absorption_capacity_fats'         : 60,
    'absorption_capacity_vitamins'     : 60,
    'absorption_capacity_minerals'     : 60,
    'constitution_growth_rate'         : 2,
    'fat_retention'                    : 1000,
    'maturity_size'                    : 100,
    'life_expectancy'                  : 90000,
    'seeds_cost'                       : 5
}