from math import floor, ceil, log
from config import * # Dicen que hacer esto es feo, pero me parece necesario
from needs import need_to_rest_tree, need_to_procreate_tree, need_to_protect_oneself_tree, need_to_collect_tree, need_to_eat_tree, need_to_collect_tree, need_to_feed_tree, need_to_collect_tree
import copy
import random

class Reasonings():
    # Necesidades
    def what_i_need(self, territory, light, temperature):
        """
        En esta versión, sólo se contempla la satisfacción de una necesidad por iteración.
        No se contempla la imposibilidad de realizar una acción para satisfacer una necesidad.
        """
        need_to_eat             = self.need_to_eat(territory, light, temperature)
        need_to_collect         = self.need_to_collect(territory, light, temperature)
        need_to_protect_oneself = self.need_to_protect_oneself(territory, light, temperature)
        need_to_rest            = self.need_to_rest(territory, light, temperature)
        need_to_feed            = self.need_to_feed(territory, light, temperature)
        need_to_procreate       = self.need_to_procreate(territory, light, temperature)

        needs = [need_to_eat, need_to_collect, need_to_protect_oneself, need_to_rest, need_to_feed, need_to_procreate]
        needs.sort(key=lambda need: need[1], reverse=True) # Las ordena de mayor a menor urgencia

        return needs[0][0] # String con el nombre de la necesidad.

    def need_to_eat(self, territory, light, temperature):
        return ("To Eat", max(0, self.genome['hungry'] - self.energy))

    def need_to_collect(self, territory, light, temperature):
        return ("To Collect", max(0, self.genome['provision'] - self.get_bab_occupancy_rate()))

    def need_to_protect_oneself(self, territory, light, temperature):
        """
        Habría que revisar esta función
        """
        return ("To Protect Oneself", len(self.to_detect_danger(territory)) * 100)

    def need_to_rest(self, territory, light, temperature):
        if self.maturity_level == 1:
            return ("To Rest", self.fatigue * par_need_to_rest_madurity_1)
        elif self.maturity_level == 2:
            return ("To Rest", self.fatigue * par_need_to_rest_madurity_2)
        elif self.maturity_level == 3:
            return ("To Rest", self.fatigue * par_need_to_rest_madurity_3)
        elif self.maturity_level < 0:
            return ("To Rest", self.fatigue * par_need_to_rest_madurity_4)

    def need_to_feed(self, territory, light, temperature):
        offsprings = self.are_there_any_offspring(territory)
        need_value = 0
        for offspring in offsprings: # Recordemos que offsprings son objetos OffspringMemory
            need_value += max(0, self.genome['provision'] - offspring.agent.get_bab_occupancy_rate())
        return ("To Feed", need_value)

    def need_to_procreate(self, territory, light, temperature):
        if self.maturity_level != 3 or type(self.pregnant) is list:
            return ("To Procreate", -9000)
        return ("To Procreate", self.pregnant * self.genome['libido'])
            


    def make_a_decision(self, territory, light, temperature):
        """
        Comprueba que necesidad se quiere satisfacer y utiliza los árboles para saber que acción realizar y colocarla en la inercia.
        """
        need = self.what_i_need(territory, light, temperature)
        if need == "To Eat":
            posible_inercia = (need_to_eat_tree.run((self, territory, light, temperature), (None,))[1], 1)
            if self.inertia[0][0] == posible_inercia[0][0]: # Estamos haciendo la misma acción que en la iteración anterior.
                self.inertia = (self.inertia[0], self.inertia[1] + 1)
            else:
                self.inertia = posible_inercia

        elif need == "To Collect":
            if self.inertia[0][0] == "To Collect": # Estamos haciendo la misma acción que en la iteración anterior.
                self.inertia = (self.inertia[0], self.inertia[1] + 1)
            else:
                self.inertia = (need_to_collect_tree.run((self, territory, light, temperature), (None,))[1], 1)

        elif need == "To Protect Oneself":
            self.inertia = (need_to_protect_oneself_tree.run((self, territory, light, temperature), (None,))[1], 1)

        elif need == "To Rest":
            if self.inertia[0][0] == "To Rest": # Estamos haciendo la misma acción que en la iteración anterior.
                self.inertia = (self.inertia[0], self.inertia[1] + 1)
            else:
                self.inertia = (need_to_rest_tree.run((self, territory, light, temperature), (None,))[1], 1)

        elif need == "To Feed":
            posible_inercia = (need_to_feed_tree.run((self, territory, light, temperature), (None,))[1], 1)
            if self.inertia[0][0] == posible_inercia[0][0]: # Estamos haciendo la misma acción que en la iteración anterior.
                self.inertia = (self.inertia[0], self.inertia[1] + 1)
            else:
                self.inertia = posible_inercia

        elif need == "To Procreate":
            self.inertia = (need_to_procreate_tree.run((self, territory, light, temperature), (None,))[1], 1)




    # Buen lugar para descansar
    def is_good_place_to_rest(self, territory, temperature):
        if ((- self.comfortable_place(temperature) - ceil(territory.size - (self.get_size_category() + 1) * 2 * par_minimum_size_category)) + self.fatigue) > 0:
            return True
        return False

    def get_places(self, territory):
        places = []
        for place in territory.neighbors:
            if (place.size > self.size) and not place.is_full():
                places.append(place)
        return places

    def to_choose_good_place(self, territories):
        """
        Usa una lista de territorios y devuelve uno.
        """
        territories.sort(key=lambda territories: territories.size, reverse=False) # Los ordena de menor a mayor tamaño
        return territories[0]


    # Reproducirse
    def are_there_any_partners(self, territory):
        partners = []
        for agent in territory.elements['animals']:
            if (agent.genome['sex'] != self.genome['sex']) and (not type(agent.pregnant) is list) and (self.genetic_node.species is agent.genetic_node.species) and (agent.maturity_level == 3): # Es de distinto sexo, no está embarazada, es fértil y somos de la misma especie.
                partners.append(agent)
        return partners

    def to_choose_partner(self, partners):
        partners.sort(key=lambda partners: partners.genome['fertility'], reverse=True) # Los ordena de menor a mayor tamaño
        return partners[0]

    def to_search_partner(self, territories):
        """
        @brief      Busca parejas en los territorios adyacentes.
        
        En esta versión devuelve el que tenga más agentes animales.

        @param      self         The object
        @param      territories  The territories
        
        @return     The best territory for to find partner.
        """
        territories.sort(key=lambda territory: len(territory.elements['animals']), reverse=True) # Los ordena de mayor a menor tamaño
        return territories[0]

    # Protegerse
    def to_detect_danger(self, territory):
        aggressors = []
        for animal in territory.elements['animals']:
            if animal.inertia[0][0] == 'To Attack' and animal.inertia[0][1] is self:
                aggressors.append(animal)
            else:
                for enemy in self.memories.hostile_creature_memories:
                    if animal.genetic_node is enemy.creature:
                        aggressors.append(animal)
                        break
        return aggressors

    def to_evaluadted_confrontation(self, aggressors):
        """
        En futuras versiones habría que añadir los músculos y las heridas actuales.
        """
        danger = 0
        for aggressor in aggressors:
            danger += aggressor.size
        if (self.size + self.genome['aggressiveness'] - self.genome['fear'] - danger) > 0:
            return True # Queremos luchar
        return False

    def to_choose_enemy_to_attack(self, enemies):
        return random.choice(enemies)


    # Acumular alimento
    def have_space_in_bag(self):
        return bool(100 - self.get_bab_occupancy_rate())

    def are_there_any_food(self, territory):
        return territory.elements['aliments'] + territory.elements['vegetables']

    def to_choose_food(self, aliments):
        """
        @brief      Selecciona un alimento de todos los posibles.
        
        Comprueba para cada alimento en el territorio si tiene recuerdos sobre su valor nutritivo.
        En caso de no recordarlo, le asigna el valor de la curiosidad.

        Habría que ver que hacer con el umbral de cuanto de malo tiene que ser para no comerlo.
        
        @param      self      The object
        @param      aliments  The aliments
        
        @return     El alimento con mayor valor nutritivo.
        """
        options = []
        for aliment in aliments:
            for aliment_memory in self.memories.food_memories:
                if (aliment.genetic_node == aliment_memory.species):
                    options.append((aliment, aliment_memory.nutritional_value))
                    break
            options.append((aliment, self.genome['curiosity']))
        options.sort(key=lambda aliment: aliment[1], reverse=True) # Los ordena de mayor a menor valor
        return options[0][0]

    def are_there_any_prey(self, territory):
        all_preys = territory.elements['animals'][:]
        all_preys.remove(self) # Quitamos a uno mismo
        return all_preys

    def to_choose_prey(self, preys):
        options = []
        for prey in preys:
            for food_memory in self.memories.food_memories:
                if (prey.genetic_node.species == food_memory.species):
                    options.append((prey, food_memory.nutritional_value))
                    break
            options.append((prey, self.genome['curiosity'] + self.genome['aggressiveness']))
        options.sort(key=lambda prey: prey[1], reverse=True) # Los ordena de mayor a menor valor
        return options[0][0]

    def to_search_food(self, territories):
        territories.sort(key=lambda territory: (territory.elements['aliments'] + territory.elements['animals'] + territory.elements['vegetables']), reverse=True) # Los ordena de mayor a menor tamaño
        return territories[0]


    # Alimentarse
    def to_have_food(self):
        return bool(self.bag)


    # Alimentar a las crías
    def are_there_any_offspring(self, territory):
        """
        Se guardan los recuerdos en vez de los agentes porque son sólo los recuerdos de los que están en el territorio y se tiene a meno tanto el agente como el valor de distancia genética.
        """
        offsprings_memories = []
        for animal in territory.elements['animals']:
            for memory in self.memories.offspring_memories:
                if animal is memory.agent:
                    offsprings_memories.append(memory)
                    break
        return offsprings_memories

    def to_choose_offspring_to_feed(self, offsprings):
        offsprings.sort(key=lambda offsprings: (1 - offsprings.agent.get_bab_occupancy_rate()) * offsprings.genetic_distance, reverse=True) # Los ordena de mayor a menor urgencia.
        return offsprings[0].agent