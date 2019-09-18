import copy
from rabbit import Rabbit, rabbit_genome
from gooseberry import Gooseberry, gooseberry_genome
from genetic_tree import GeneticTree, Node, VegetableNode
from aliment import Aliment, AlimentSource
from world import Territory
from config import *


oryctolagus_cuniculus = GeneticTree()
ribes_rubrum = GeneticTree()

avellano = Rabbit(100, 100, 100, 100, 100, 100, 0, 1, 1, Node(None, None, oryctolagus_cuniculus), copy.copy(rabbit_genome))
avellano.genome['sex'] = 1
lola = Rabbit(100, 100, 100, 100, 100, 100, 0, 1, 1, Node(None, None, oryctolagus_cuniculus), copy.copy(rabbit_genome))
lola.genome['sex'] = 0
pepito = Rabbit(100, 100, 100, 100, 100, 100, 0, 1, 1, Node(None, None, oryctolagus_cuniculus), copy.copy(rabbit_genome))
pepito.genome['fertility'] = 555
pepito.genome['sex'] = 1
pepita = Rabbit(100, 100, 100, 100, 100, 100, 0, 1, 1, Node(None, None, oryctolagus_cuniculus), copy.copy(rabbit_genome))
pepita.genome['sex'] = 0
postre = Aliment(ribes_rubrum, {'carbohydrates' : 100, 'proteins' : 200, 'fats' : 300, 'vitamins' : 400, 'minerals' : 500})
postre_amigo = Aliment(oryctolagus_cuniculus, {'carbohydrates' : 5000, 'proteins' : 200, 'fats' : 300, 'vitamins' : 400, 'minerals' : 500})

avellano.memories.to_remember_food(avellano.age, (postre.species, (50,50,50,50,0), 50))
avellano.memories.to_remember_food(avellano.age, (postre_amigo.species, (50,50,50,50,50), 50))

avellano.maturity_level = 3
lola.maturity_level = 3
pepito.maturity_level = 3
pepita.maturity_level = 3

casa = Territory(2000, 2000)
escuela = Territory(800, 2000)
patio = Territory(800, 1000)
casa.to_link_neighbors([escuela, patio])
casa.append_animal(avellano)
casa.append_animal(lola)
casa.append_animal(pepito)
casa.append_animal(pepita)

mesita = AlimentSource(postre, 5)
banquete = AlimentSource(postre_amigo, 5)


plantita = Gooseberry(100, 100, 100, 100, 100, 100, 1, 100, VegetableNode(ribes_rubrum), copy.copy(gooseberry_genome))
casa.elements['vegetables'].append(plantita)
# AL PONER AQUÍ EL TAMAÑO, LAS CRÍAS NACEN MÁS GRANDES DE LO NORMAL
# ES PROBABLE QUE PASEN COSAS RARAS EN COMO SE CREAN LOS RECUERDOS, PERO A GROSO MODO, FUNCHULA
