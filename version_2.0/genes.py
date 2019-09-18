import random
from config import par_mutation_probability

genes = {   
    'visual_perception'                : (0, float('inf')),
    'sensitivity_light'                : (0, 100),
    'auditory_perception'              : (0, float('inf')),
    'olfactory_perception'             : (0, float('inf')),
    'sensory_perception'               : (0, float('inf')),
    'alert'                            : (0, float('inf')),
    'muscles_upper'                    : (0, float('inf')),
    'muscles_lower'                    : (0, float('inf')),
    'dexterity'                        : (0, float('inf')),
    'intelligence_memory'              : (0, float('inf')),
    'libido'                           : (0, float('inf')),
    'selfish_gen'                      : (0, float('inf')),
    'hungry'                           : (0, float('inf')),
    'provision'                        : (0, 100),
    'fear'                             : (float('-inf'), float('inf')),
    'aggressiveness'                   : (float('-inf'), float('inf')),
    'patience'                         : (0, float('inf')),
    'curiosity'                        : (0, float('inf')),
    'immune_constitution'              : (0, float('inf')),
    'estructural_constitution'         : (0, float('inf')),
    'constitution_size_modification'   : (0, 100),
    'constitution_smell_modification'  : (0, float('inf')),
    'constitution_temperature'         : (0, float('inf')),
    'skin_tone'                        : (-100, 100),
    'rhythm_growth_1'                  : (0, float('inf')),
    'rhythm_growth_2'                  : (0, float('inf')),
    'rhythm_growth_3'                  : (0, float('inf')),
    'rhythm_growth_4'                  : (0, float('inf')),
    'fertility'                        : (0, float('inf')),
    'sex'                              : (0, 1), # 0 = female; 1 = male
    'digestive_capacity_carbohydrates' : (0, 100),
    'digestive_capacity_proteins'      : (0, 100),
    'digestive_capacity_fats'          : (0, 100),
    'digestive_capacity_vitamins'      : (0, 100),
    'digestive_capacity_minerals'      : (0, 100),
    'absorption_capacity_carbohydrates': (0, 100),
    'absorption_capacity_proteins'     : (0, 100),
    'absorption_capacity_fats'         : (0, 100),
    'absorption_capacity_vitamins'     : (0, 100),
    'absorption_capacity_minerals'     : (0, 100),

    # Genes de las plantas
    'constitution_growth_rate'         : (0, float('inf')),
    'fat_retention'                    : (0, float('inf')),
    'maturity_size'                    : (0, float('inf')),
    'life_expectancy'                  : (0, float('inf')),
    'seeds_cost'                       : (0, float('inf'))
}

def genomes_crossing(genome1, genome2):
    """
    @brief      Genera un nuevo cromosoma mediante cruzamiento
    
    @param      genome1  The genome1
    @param      genome2  The genome2
    
    @return     The new genome.
    """
    genome = {}
    for gen in genome1:
        genome[gen] = genes_crossing(gen, genome1[gen], genome2[gen])
    return genome



def genes_crossing(gen_name, value1, value2):
    """
    @brief      Genera el valor de un gen mediente cruzamiento.
    
    @param      gen    The gen
    @param      value1  The value1
    @param      value2  The value2
    
    @return     The new value.
    """
    percentage = get_percentage()
    gen = value1 * percentage + value2 * (1 - percentage)
    if random.random() < par_mutation_probability:
        gen = mutate(gen)
    gen = check_ranges(gen_name, gen)
    return gen


def get_percentage():
    """
    @brief      Gets the percentage.

    El valor devuelto por esta función determina si el cruce se hace cogiendo unicamente el gen de uno de los progenitores, la mitad de cada uno, o un porcentaje acotado.
    
    @return     The percentage.
    """
    return random.randint(0, 1)

def mutate(value):
    """
    @brief      Muta el valor del parámetro según la función de mutación definida.

    La función de mutación debería ser más elaborada y quizá adaptarse a los rangos de los distintos genes. Esta implementación es para salir del paso.
    
    @param      value  The value
    
    @return     Valor mutado
    """
    return value + random.randint(-2, 2)

def check_ranges(key, value):
    """
    @brief      Check that the value is in the range.
    
    @param      key    The key
    @param      value  The value
    
    @return     The value in the range.
    """
    if value < genes[key][0]:
        value = genes[key][0]
    if value > genes[key][1]:
        value = genes[key][1]
    return value


# GENOMAS DE EJEMPLO, NO LOS TOQUES
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
    'hungry'                           : 100,
    'provision'                        : 60,
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
    'rhythm_growth_2'                  : 100,
    'rhythm_growth_3'                  : 100,
    'rhythm_growth_4'                  : 100,
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

