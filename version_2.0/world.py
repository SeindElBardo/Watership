from math import floor, log, radians, cos, sin
from config import * # Dicen que hacer esto es feo, pero me parece necesario

class World(object):
    def __init__(self, light_power, time):
        self.light_power = light_power
        self.planets = []
        self.time = time

    def to_proceed():
        for planet in self.planets:
            planet_position = planet.get_position(self.time)
            planet_rotation = planet.get_rotation(self.time)
            for region in planet.regions:
                region.set_light(planet_position, planet_rotation)
                region.set_temperature(planet_position, planet_rotation)
                for territory in region.territories:
                    territory.to_proceed(region.light, region.temperature)
            for region in planet.regions: # Los viajes se realizan cuando no quedan acciones por realizar en el territorio        
                region.to_take_journeys()
            for region in planets.regions:
                for territory in region.territories: # Con las acciones realizadas y los agentes en el territorio en el que deben acabar la iteración, todos realizan sus procesos.
                    territory.to_live(region.light, region.temperature)
                region.to_dissipate_heat()
        self.time += 1



class Planet(object):
    def __init__(self, radius_planet, shaft_tilt, rotation_speed, translation_speed, elipse_orbit_x, elipse_orbit_y, elipse_orbit_z, displacement_orbit_x, displacement_orbit_y, displacement_orbit_z):
        self.radius_planet = radius_planet
        self.shaft_tilt = (sin(shaft_tilt), cos(shaft_tilt), 0) # Vector unitario de rotación. Se esperan radianes.
        self.rotation_speed = rotation_speed
        self.translation_speed = translation_speed
        self.elipse_orbit_x = elipse_orbit_x
        self.elipse_orbit_y = elipse_orbit_y
        self.elipse_orbit_z = elipse_orbit_z
        self.displacement_orbit_x = displacement_orbit_x
        self.displacement_orbit_y = displacement_orbit_y
        self.displacement_orbit_z = displacement_orbit_z
        self.regions = []

# AÑADIR VELOCIDAD DE TRASLACIÓN
    def get_position(self, time):
        teta = math.radians(time/60/60) # Sólo va a rotar en un plano (quizá esto me lo esté inventado)
        fi = math.radians(0)
        x = self.displacement_orbit_x + self.elipse_orbit_x * cos(teta) * cos(fi)
        y = self.displacement_orbit_y + self.elipse_orbit_y * sin(teta) * cos(fi)
        z = self.displacement_orbit_z + self.elipse_orbit_z * sin(fi)
        return (x, y, z)

    def get_rotation(self, time):
        pass



class Region(object):
    def __init__(self, filtration, retention, coordinate_x, coordinate_y, coordinate_z):
        self.filtration = filtration
        self.retention = retention
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.coordinate_z = coordinate_z
        self.light = 100
        self.temperature = 300
        self.wind = (0,1)
        self.territories = []

    def set_light(self, position, rotation):
        pass

    def set_temperature(self, position, rotation):
        pass

    def to_dissipate_heat():
        pass

    def to_take_journeys(): # Se hacen todos los cambios de territorios al final para no generar inconsistencias.
        for territory in self.territories:
            for journey in territory.journeys:
                territory.to_travel(journey[0], journey[1])

class Territory(object):
    def __init__(self, size, capacity):
        self.size = size
        self.capacity = capacity
        self.load = 0
        self.elements = {'aliments' : [], 'animals' : [], 'vegetables' : []}
        self.smell = []
        self.neighbors = []

        self.journeys = [] # Tuplas de agentes y el territorio al que se mueven

    def to_link_neighbors(self, neighbors): # Cuidado con meter dos veces el mismo.
        for i in neighbors:
            self.neighbors.append(i)
            i.neighbors.append(self)

    def get_declaration_order(self, light):
        declaration_order = self.elements['animals'][:]
        declaration_order.sort(key=lambda agent: agent.get_perception(light), reverse=False) # Los que tienen menor percepción declaran primero. De esa forma los que tienen mayor percepción cuentan con más información.
        return declaration_order

    def get_action_order(self):
        action_list = self.elements['animals'][:]
        action_list.sort(key=lambda agent: agent.get_speed(), reverse=True) # Los que tienen mayor velocidad actuan primero.
        return action_list

    def to_proceed(self, light, temperature):
        """
        @brief      Los animales del territorio realizan una acción
        
        @param      self         The object
        @param      light        The light
        @param      temperature  The temperature
        """
        declaration_order = self.get_declaration_order(light)
        for animal in declaration_order:
            animal.make_a_decision(self, light, temperature) # Se implementa en los árboles de comportamiento. La elección se guarda en la inercia del agente.
        action_order = self.get_action_order()
        for animal in action_order:
            if animal.is_alive():
                animal.to_do_action(self, light, temperature) # MIRAR QUE PARÁMETROS NECESITA

    def to_live(self, light, temperature):
        """
        @brief      Los agentes del territorio realizan sus procesos y se eliminan las fuentes de alimento vacías.
        
        @param      self         The object
        @param      light        The light
        @param      temperature  The temperature
        """
        agents = self.elements['animals'] + self.elements['vegetables']
        for agent in agents:
            agent.to_live(self, light, temperature)

        aliment_sources = self.elements['aliments'][:] # Se hace una copia porque se van a eliminar elementos de la lista sobre la que se está iterando.
        for aliment_source in aliment_sources:
            if not aliment_source.stack:
                self.elements['aliments'].remove(aliment_source)
        

    def to_spread_smell(self):
        pass

    def append_animal(self, animal):
        self.load += animal.size
        self.elements['animals'].append(animal)

    def remove_animal(self, animal):
        self.load -= animal.size
        self.elements['animals'].remove(animal)

    def to_travel(self, animal, territory):
        self.remove_animal(animal)
        territory.append_animal(animal)

    def is_full(self):
        return self.capacity < self.load
