from math import floor, log
from config import * # Dicen que hacer esto es feo, pero me parece necesario


class Actions():
    # Realizar acción
    def to_do_action(self, territory, light, temperature):
        if self.inertia[0][0] == "To Eat":
            self.to_eat()
        
        elif self.inertia[0][0] == "To Collect":
            self.to_collect(territory, light, self.inertia[0][1])

        elif self.inertia[0][0] == "To Attack":
            self.to_attack(territory, light, self.inertia[0][1])

        elif self.inertia[0][0] == "To Scape":
            self.to_escape(territory, self.inertia[0][1])

        elif self.inertia[0][0] == "To Rest":
            self.to_rest()

        elif self.inertia[0][0] == "To Move":
            self.to_move(territory, self.inertia[0][1])

        elif self.inertia[0][0] == "To Procreate":
            self.to_procreate(self.inertia[0][1])

        elif self.inertia[0][0] == "To Feed":
            self.to_feed(self.inertia[0][1])

    # Comer
    def to_eat(self):
        self.stomach.append(self.bag.pop())
        self.energy -= par_energy_cost_to_eat
        self.fatigue += par_fatigue_cost_to_eat


    # Recolectar
    def to_collect(self, territory, light, aliment_source):
        if not aliment_source.is_eatable():
            return
        self.energy -= par_energy_cost_to_collect
        self.fatigue += par_fatigue_cost_to_collect
        necessary_iterations = self.get_iterations_for_to_collect(territory, light, aliment_source)
        if not (self.inertia[1] % necessary_iterations):
            self.bag.append(aliment_source.be_eaten(territory))

    def get_iterations_for_to_collect(self, territory, light, aliment_source):
        return  max(2, floor(par_iterations_to_collect - (((self.muscles['upper'] + self.visual_capacity(light) + self.genome['olfactory_perception'] + self.genome['dexterity']) / 4) * self.health_condition_penalty())))

    # Atacar
    def to_attack(self, territory, light, victim):
        if not victim.is_alive() or victim in territory.journeys:
            return
        self.energy -= self.energy_cost_to_attack()
        self.fatigue += self.fatigue_cost_to_attack()
        victim.wounds += self.get_power_attack(light)
        if victim.wounds >= par_mortal_wounds_limit_value:
            victim.to_die(territory)

    def energy_cost_to_attack(self):
        return max(1, self.health_condition_penalty() * par_energy_cost_to_attack - self.genome['estructural_constitution'])

    def fatigue_cost_to_attack(self):
        return max(1, self.health_condition_penalty() * par_fatigue_cost_to_attack - self.muscles['upper'] - self.genome['estructural_constitution'])


    def get_power_attack(self, light):
        return floor((self.visual_capacity(light) + self.genome['dexterity'] + self.genome['sensory_perception']) / 2 + self.muscles['upper'] * par_muscles_to_hurt_ratio + self.size * par_size_to_hurt_ratio)


    # Moverse
    def to_move(self, territory_1, territory_2):
        self.energy -= par_energy_cost_to_move
        self.fatigue += par_fatigue_cost_to_move
        necessary_iterations = self.get_iterations_for_to_move()
        if not self.inertia[1] % necessary_iterations:
            territory_1.journeys.append((self, territory_2))

    def get_iterations_for_to_move(self):
        return  max(1, floor((par_iterations_to_move - self.muscles['lower'] - self.genome['estructural_constitution']) * self.health_condition_penalty()))


    # Dormir
    def to_rest(self):
        self.energy -= par_energy_cost_to_rest
        if not self.inertia[1] % par_iterations_to_rest:
            self.fatigue -= par_fatigue_cost_to_rest


    # Huir
    def to_escape(self, territory_1, territory_2):
        necessary_iterations = self.get_iterations_for_to_move()
        self.energy -= par_energy_cost_to_escape * necessary_iterations
        self.fatigue += par_fatigue_cost_to_escape * necessary_iterations
        territory_1.journeys.append((self, territory_2))



    # Alimentar
    def to_feed(self, beneficiary):
        if not beneficiary.is_alive():
            return
        self.energy -= par_energy_cost_to_feed
        self.fatigue += par_fatigue_cost_to_feed
        beneficiary.bag.append(self.bag.pop())


    # Procrear
    def to_procreate(self, partner):
        if not partner.is_alive():
            return
        self.energy -= par_energy_cost_to_procreate
        self.fatigue += par_fatigue_cost_to_procreate
        if partner.inertia[0][0] == "To Procreate" and partner is self.inertia[0][1] and partner.inertia[1] == 1: # El deseo de reproducción es reciproco y de esta iteración
            self.to_reproduce(partner)