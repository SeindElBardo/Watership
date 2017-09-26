import arbolDistanciaGenetica2 as ae # arbolEspecie
import mapa
import individuo
import planta
import random

#Crear territorio
territorios = []
granValle = mapa.Territorio(50,True,0,[])
granValle2 = mapa.Territorio(50,True,0,[granValle])
granValle3 = mapa.Territorio(50,True,0,[granValle, granValle2])
granValle4 = mapa.Territorio(50,True,0,[granValle, granValle2, granValle3])
territorios.append(granValle)
territorios.append(granValle2)
territorios.append(granValle3)
territorios.append(granValle4)

#Crear plantas (Se añaden como listas)
granValle.newPlanta([planta.Planta(5, 10, 5, 10)])
granValle.newPlanta([planta.Planta(2, 40, 10, 40)])
granValle.newPlanta([planta.Planta(3, 20, 15, 20)])

granValle2.newPlanta([planta.Planta(5, 10, 5, 10)])
granValle2.newPlanta([planta.Planta(2, 40, 10, 40)])
granValle2.newPlanta([planta.Planta(3, 20, 15, 20)])

granValle3.newPlanta([planta.Planta(5, 10, 5, 10)])
granValle3.newPlanta([planta.Planta(2, 40, 10, 40)])
granValle3.newPlanta([planta.Planta(3, 20, 15, 20)])

granValle4.newPlanta([planta.Planta(5, 10, 5, 10)])
granValle4.newPlanta([planta.Planta(2, 40, 10, 40)])
granValle4.newPlanta([planta.Planta(3, 20, 15, 20)])


#Crear conejos
oCuniculus = ae.ArbolEspecie() # Conejo
cromosoma1 = {
		'fuerza' : 5,
		'destreza' : 15,
		'constitucion' : 5,
		'velocidad' : 21,
		'inteligencia' : 4,
		'percepcion' : 11,
		'esperanzaVida' : 60,
		'fecundidad' : 1,
		'madurezSexual': 10}
cromosoma2 = {
		'fuerza' : 5,
		'destreza' : 6,
		'constitucion' : 4,
		'velocidad' : 21,
		'inteligencia' : 1,
		'percepcion' : 16,
		'esperanzaVida' : 60,
		'fecundidad' : 1,
		'madurezSexual': 10}

cromosoma3 = {
		'fuerza' : 6,
		'destreza' : 4,
		'constitucion' : 4,
		'velocidad' : 3,
		'inteligencia' : 1,
		'percepcion' : 8,
		'esperanzaVida' : 60,
		'fecundidad' : 1,
		'madurezSexual': 10}

cromosoma4 = {
		'fuerza' : 4,
		'destreza' : 5,
		'constitucion' : 4,
		'velocidad' : 10,
		'inteligencia' : 1,
		'percepcion' : 6,
		'esperanzaVida' : 60,
		'fecundidad' : 1,
		'madurezSexual': 10}

cromosoma5 = {
		'fuerza' : 4,
		'destreza' : 5,
		'constitucion' : 10,
		'velocidad' : 10,
		'inteligencia' : 1,
		'percepcion' : 6,
		'esperanzaVida' : 60,
		'fecundidad' : 1,
		'madurezSexual': 10}

#_init__(self, nodo, especie, edad, sexo, cromosoma):
nodo = ae.Nodo(None,None,oCuniculus)
granValle.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 1, cromosoma2)])
nodo = ae.Nodo(None,None,oCuniculus)
granValle.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 1, cromosoma3)])
nodo = ae.Nodo(None,None,oCuniculus)
granValle.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 1, cromosoma1)])
nodo = ae.Nodo(None,None,oCuniculus)
granValle.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 1, cromosoma4)])
nodo = ae.Nodo(None,None,oCuniculus)
granValle2.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 0, cromosoma1)])
nodo = ae.Nodo(None,None,oCuniculus)
granValle2.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 0, cromosoma4)])
nodo = ae.Nodo(None,None,oCuniculus)
granValle2.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 0, cromosoma2)])
nodo = ae.Nodo(None,None,oCuniculus)
granValle2.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 0, cromosoma3)])

#Crear zorros
CanisVulpini = ae.ArbolEspecie() # Zorro

nodo = ae.Nodo(None,None,CanisVulpini)
granValle3.newZorro([individuo.Zorro(nodo, CanisVulpini, 16, 1, cromosoma5)])
nodo = ae.Nodo(None,None,CanisVulpini)
granValle4.newZorro([individuo.Zorro(nodo, CanisVulpini, 16, 0, cromosoma5)])

for dia in range(0,40):
	viajes = []
	for tierra in territorios:
		print ("Día " + str(dia) + " en " + str(tierra))
		orgia = []
		llorones = []
		victimas = []
		turnos = []
		print("#########  DECLARAR  #########")
		declara = tierra.getDeclaraciones()
		for theIndividuo in declara:
			print (str(theIndividuo) + " " + str(theIndividuo.nodo.indice))
			print("Energia " + str(theIndividuo.energia) + "/" + str(theIndividuo.getCapacidadEnergia()))
			print("Inventario " + str(theIndividuo.inventario) + "/" + str(theIndividuo.getCapacidadCarga()))
			print("Felicidad " + str(theIndividuo.felicidad))
			decision = theIndividuo.getDecision(tierra.getAcciones(theIndividuo, orgia, llorones, victimas), orgia, llorones, victimas) # Decision es una tupla
			turnos.append((theIndividuo, decision))
			print (decision)
			print ("\n")
		print("\n#########  ACTUAR  #########")
		tierra.getIniciativas(turnos)
		for ii in turnos:
			ii[0].actuar(ii[1], viajes)
		print("\n\n\n")
	for viaje in viajes:
		viaje[0].viajar(viaje[1],viaje[2])
	for tierra in territorios:
		tierra.elMundoSeMueve()
