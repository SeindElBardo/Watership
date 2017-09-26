import arbolDistanciaGenetica2 as ae # arbolEspecie
import mapa
import individuo
import planta
import random

plantas = open("plantas.log", "w")
conejos = open("conejos.log", "w")
zorros = open("zorros.log", "w")

#Crear territorio
territorios = []
granValle = mapa.Territorio(200,True,0,[])
territorios.append(granValle)


cromosoma1 = {
		'fuerza' : 5,
		'destreza' : 9,
		'constitucion' : 10,
		'velocidad' : 8,
		'inteligencia' : 4,
		'percepcion' : 11,
		'esperanzaVida' : 80,
		'fecundidad' : 1,
		'madurezSexual': 15}
cromosoma2 = {
		'fuerza' : 5,
		'destreza' : 6,
		'constitucion' : 4,
		'velocidad' : 7,
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

#Crear plantas (Se añaden como listas)
for i in range(0,66):
	granValle.newPlanta([planta.Planta(5, 10, 5, 10)])
	granValle.newPlanta([planta.Planta(2, 40, 10, 40)])
	granValle.newPlanta([planta.Planta(3, 20, 15, 20)])

#Crear conejos
oCuniculus = ae.ArbolEspecie() # Conejo
for i in range(0,20):
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

for dia in range(0,200):
	print ("Día " + str(dia))
	viajes = []
	for tierra in territorios:
		if not dia%10:
			esporas = 0
			madurez = 0
			crecimiento = 0
			for planta in granValle.plantas:
				esporas += planta.cromosoma['esporas']
				madurez += planta.cromosoma['madurez']
				crecimiento += planta.cromosoma['crecimiento']
			lenPlantas = len(granValle.plantas) if granValle.plantas else float("infinity")
			plantas.write(str(esporas/lenPlantas)+","+str(madurez/lenPlantas)+","+str(crecimiento/lenPlantas)+"\n")
			
			fuerza = 0
			destreza = 0
			constitucion = 0
			velocidad = 0
			inteligencia = 0
			percepcion = 0
			esperanzaVida = 0
			fecundidad = 0
			madurezSexual = 0
			for conejo in granValle.conejos:
				fuerza += conejo.cromosoma['fuerza']
				destreza += conejo.cromosoma['destreza']
				constitucion += conejo.cromosoma['constitucion']
				velocidad += conejo.cromosoma['velocidad']
				inteligencia += conejo.cromosoma['inteligencia']
				percepcion += conejo.cromosoma['percepcion']
				esperanzaVida += conejo.cromosoma['esperanzaVida']
				fecundidad += conejo.cromosoma['fecundidad']
				madurezSexual += conejo.cromosoma['madurezSexual']

			lenConejos = len(granValle.conejos) if granValle.conejos else float("infinity")
			conejos.write(
				str(fuerza/lenConejos)+","+
				str(destreza/lenConejos)+","+
				str(constitucion/lenConejos)+","+
				str(velocidad/lenConejos)+","+
				str(inteligencia/lenConejos)+","+
				str(percepcion/lenConejos)+","+
				str(esperanzaVida/lenConejos)+","+
				str(fecundidad/lenConejos)+","+
				str(madurezSexual/lenConejos)+","+"\n")

			fuerza = 0
			destreza = 0
			constitucion = 0
			velocidad = 0
			inteligencia = 0
			percepcion = 0
			esperanzaVida = 0
			fecundidad = 0
			madurezSexual = 0
			for zorro in granValle.zorros:
				fuerza += zorro.cromosoma['fuerza']
				destreza += zorro.cromosoma['destreza']
				constitucion += zorro.cromosoma['constitucion']
				velocidad += zorro.cromosoma['velocidad']
				inteligencia += zorro.cromosoma['inteligencia']
				percepcion += zorro.cromosoma['percepcion']
				esperanzaVida += zorro.cromosoma['esperanzaVida']
				fecundidad += zorro.cromosoma['fecundidad']
				madurezSexual += zorro.cromosoma['madurezSexual']

			lenZorros = len(granValle.zorros) if granValle.zorros else float("infinity")
			zorros.write(
				str(fuerza/lenZorros)+","+
				str(destreza/lenZorros)+","+
				str(constitucion/lenZorros)+","+
				str(velocidad/lenZorros)+","+
				str(inteligencia/lenZorros)+","+
				str(percepcion/lenZorros)+","+
				str(esperanzaVida/lenZorros)+","+
				str(fecundidad/lenZorros)+","+
				str(madurezSexual/lenZorros)+","+"\n")
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

plantas.close()
conejos.close()
zorros.close()