class Memories(object):
    def __init__(self, memory_capacity):
        self.food_memories = []
        self.offspring_memories = [] # No aplican a la cantidad de recuerdos y nunca se olvidan (mientras vivan)
        self.territory_link_memories = []
        self.food_location_memories = []
        self.hostile_creature_memories = []
        self.lists_forgettable_memories = [self.food_memories, self.territory_link_memories, self.food_location_memories, self.hostile_creature_memories]
        self.memory_capacity = memory_capacity
        self.amount_memories = 0

    def to_forget(self):
        """
        Recoge todos los recuerdos que puedan ser olvidados y busca el más antiguo para eliminarlo.
        """
        lists_memories_to_forget = []
        for memory_list in lists_forgettable_memories: # Recabamos todos los recuerdos
            lists_memories_to_forget += memory_list
        lists_memories_to_forget.sort(key=lambda memories: memories.age, reverse=False) # Los ordena de más antiguo a más nuevo
        for memory_list in lists_forgettable_memories:
            if lists_memories_to_forget[0] in memory_list:
                memory_list.remove(lists_memories_to_forget[0])
                self.amount_memories -= 1
                return

#        lists_name_memories = self.__dict__.keys()
#        lists_name_memories.remove('offspring_memories') # Los recuerdos de las crías nunca se olvidan (mientras vivan)
#        lists_memories_to_forget = []
#        while not lists_memories_to_forget: # Escogemos una lista de recuerdos que no esté vacía
#            lists_memories_to_forget = self.__dict__.[random.choice(lists_name_memories)]
#        lists_memories_to_forget.remove(len(random.choice(lists_memories_to_forget)))


    def to_remember_food(self, age, food):
        """
        @brief      Crea un recuerdo de un alimento ingerido.
        
        @param      self               The object
        @param      age                The age
        @param      food               Tupla con el tipo de alimento, los 5 nutrientes digeridos y la toxicidad generada
        """
        nutritional_value = 0
        for nutrient in food[1]:
            nutritional_value += nutrient
        nutritional_value += food[1][0] - food[2] * 2
        self.food_memories.append(FoodMemory(age, food[0], nutritional_value))
        self.amount_memories += 1


    def to_remember_offspring(self, age, agent, genetic_distance):
        self.offspring_memories.append(OffspringMemory(age, agent, genetic_distance))

    def to_broatcast_birth_to_family(self, agent):
        """
        @brief      Genera en todos los agentes de la especie el recuerdo del nuevo agente.
        
        Esto permite aligerar el cálculo de distancia genética e informa a la familia de que existe un nuevo agente del que cuidar.
        Se podría añadir un parámetro para que solo generen el recuerdo los que tenga menos de cierta distancia genética.

        @param      self   The object
        @param      agent  The agent
        """
        for relative_node in agent.genetic_node.species.nodes:
            relative_node.agent.memories.to_remember_offspring(relative_node.agent.age, agent, relative_node.agent.get_genetic_distance(agent))

    def to_forget_offspring(self, agent):
        for offspring_memory in self.offspring_memories:
            if agent is offspring_memory.agent:
                self.offspring_memories.remove(offspring_memory)
                return

    def to_broatcast_death_to_family(self, agent):
        """
        @brief      Elimina en todos los agentes de la especie el recuerdo del agente muerto.

        @param      self   The object
        @param      age    The age
        @param      agent  The agent
        """
        for relative_node in agent.genetic_node.species.nodes:
            relative_node.agent.memories.to_forget_offspring(agent)


    def to_remember_territory_link(self, age, territory_1, territory_2):
        self.territory_link_memories.append(TerritoryLinkMemory(age, territory_1, territory_2))
        self.amount_memories += 1

    def to_remember_food_location(self, age, food, territory):
        self.food_location_memories.append(FoodLocationMemory(age, food[0], territory))
        self.amount_memories += 1

    def to_remember_hostile_creature(self, age, creature): # En esta versión se guarda la especie
        self.hostile_creature_memories.append(HostileCreatureMemory(age, creature))
        self.amount_memories += 1


class Memory(object):
    def __init__(self, age):
        self.age = age

class FoodMemory(Memory):
    def __init__(self, age, species, nutritional_value):
        super(FoodMemory, self).__init__(age)
        self.species = species
        self.nutritional_value = nutritional_value

class OffspringMemory(Memory):
    def __init__(self, age, agent, genetic_distance):
        super(OffspringMemory, self).__init__(age)
        self.agent = agent
        self.genetic_distance = genetic_distance

class TerritoryLinkMemory(Memory):
    def __init__(self, age, territory_1, territory_2):
        super(TerritoryLinkMemory, self).__init__(age)
        self.territory_1 = territory_1
        self.territory_2 = territory_2

class FoodLocationMemory(Memory):
    def __init__(self, age, food, territory):
        super(FoodLocationMemory, self).__init__(age)
        self.food = food
        self.territory = territory
        
class HostileCreatureMemory(Memory):
    def __init__(self, age, creature):
        super(HostileCreatureMemory, self).__init__(age)
        self.creature = creature
        