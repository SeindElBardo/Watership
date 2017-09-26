import arbolDistanciaGenetica2 as ae # arbolEspecie
import mapa
import individuo
import planta
import random

#Crear territorio
territorios = []
granValle = mapa.Territorio(200,True,0,[])
territorios.append(granValle)

#Crear plantas (Se añaden como listas)
granValle.newPlanta([planta.Planta(5, 10, 5, 10)])
granValle.newPlanta([planta.Planta(2, 40, 10, 40)])
granValle.newPlanta([planta.Planta(3, 20, 15, 20)])
granValle.newPlanta([planta.Planta(5, 10, 5, 10)])
granValle.newPlanta([planta.Planta(2, 40, 10, 40)])
granValle.newPlanta([planta.Planta(3, 20, 15, 20)])

#Crear conejos
oCuniculus = ae.ArbolEspecie() # Conejo
cromosoma1 = {
		'fuerza' : 5,
		'destreza' : 15,
		'constitucion' : 10,
		'velocidad' : 20,
		'inteligencia' : 4,
		'percepcion' : 11,
		'esperanzaVida' : 80,
		'fecundidad' : 1,
		'madurezSexual': 15}
cromosoma2 = {
		'fuerza' : 5,
		'destreza' : 6,
		'constitucion' : 4,
		'velocidad' : 121,
		'inteligencia' : 1,
		'percepcion' : 16,
		'esperanzaVida' : 60,
		'fecundidad' : 1,
		'madurezSexual': 15}

cromosoma3 = {
		'fuerza' : 6,
		'destreza' : 4,
		'constitucion' : 4,
		'velocidad' : 3,
		'inteligencia' : 1,
		'percepcion' : 8,
		'esperanzaVida' : 60,
		'fecundidad' : 1,
		'madurezSexual': 15}

cromosoma4 = {
		'fuerza' : 4,
		'destreza' : 5,
		'constitucion' : 4,
		'velocidad' : 10,
		'inteligencia' : 1,
		'percepcion' : 6,
		'esperanzaVida' : 60,
		'fecundidad' : 1,
		'madurezSexual': 15}

#_init__(self, nodo, especie, edad, sexo, cromosoma):
nodo = ae.Nodo(None,None,oCuniculus)
granValle.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 1, cromosoma2)])
nodo = ae.Nodo(None,None,oCuniculus)
granValle.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 1, cromosoma3)])
nodo = ae.Nodo(None,None,oCuniculus)
granValle.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 0, cromosoma1)])
nodo = ae.Nodo(None,None,oCuniculus)
granValle.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 0, cromosoma4)])
nodo = ae.Nodo(None,None,oCuniculus)
granValle.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 0, cromosoma2)])
nodo = ae.Nodo(None,None,oCuniculus)
granValle.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 0, cromosoma3)])
nodo = ae.Nodo(None,None,oCuniculus)
granValle.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 1, cromosoma1)])
nodo = ae.Nodo(None,None,oCuniculus)
granValle.newConejo([individuo.Conejo(nodo, oCuniculus, 16, 1, cromosoma4)])

#Crear zorros
CanisVulpini = ae.ArbolEspecie() # Zorro

for dia in range(0,1000):
	print ("Día " + str(dia))
	viajes = []
	for tierra in territorios:
		if dia == 130:
			nodo = ae.Nodo(None,None,CanisVulpini)
			granValle.newZorro([individuo.Zorro(nodo, CanisVulpini, 16, 1, cromosoma2)])
			nodo = ae.Nodo(None,None,CanisVulpini)
			granValle.newZorro([individuo.Zorro(nodo, CanisVulpini, 16, 1, cromosoma3)])
			nodo = ae.Nodo(None,None,CanisVulpini)
			granValle.newZorro([individuo.Zorro(nodo, CanisVulpini, 16, 0, cromosoma1)])
			nodo = ae.Nodo(None,None,CanisVulpini)
			granValle.newZorro([individuo.Zorro(nodo, CanisVulpini, 16, 0, cromosoma4)])
			nodo = ae.Nodo(None,None,CanisVulpini)
			granValle.newZorro([individuo.Zorro(nodo, CanisVulpini, 16, 0, cromosoma2)])
			nodo = ae.Nodo(None,None,CanisVulpini)
			granValle.newZorro([individuo.Zorro(nodo, CanisVulpini, 16, 0, cromosoma3)])
			nodo = ae.Nodo(None,None,CanisVulpini)
			granValle.newZorro([individuo.Zorro(nodo, CanisVulpini, 16, 1, cromosoma1)])
			nodo = ae.Nodo(None,None,CanisVulpini)
			granValle.newZorro([individuo.Zorro(nodo, CanisVulpini, 16, 1, cromosoma4)])
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
	for tierra in territorios:
		tierra.elMundoSeMueve()
