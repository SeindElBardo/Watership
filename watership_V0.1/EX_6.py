import arbolDistanciaGenetica2 as ae # arbolEspecie
import mapa
import individuo
import planta
import random

#Crear territorio
territorios = []
granValle = mapa.Territorio(50,True,0,[])
granValle2 = mapa.Territorio(50,True,0,[granValle])
territorios.append(granValle)
#territorios.append(granValle2)

#Crear plantas (Se añaden como listas)
#granValle.newPlanta([planta.Planta(5, 10, 5, 10)])
granValle.newPlanta([planta.Planta(2, 40, 10, 40)])
granValle.newPlanta([planta.Planta(2, 40, 10, 40)])
#granValle.newPlanta([planta.Planta(3, 20, 15, 20)])

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
		'madurezSexual': 5}
cromosoma2 = {
		'fuerza' : 5,
		'destreza' : 6,
		'constitucion' : 4,
		'velocidad' : 121,
		'inteligencia' : 1,
		'percepcion' : 16,
		'esperanzaVida' : 60,
		'fecundidad' : 1,
		'madurezSexual': 5}

cromosoma3 = {
		'fuerza' : 6,
		'destreza' : 4,
		'constitucion' : 4,
		'velocidad' : 3,
		'inteligencia' : 1,
		'percepcion' : 8,
		'esperanzaVida' : 60,
		'fecundidad' : 1,
		'madurezSexual': 1}

cromosoma4 = {
		'fuerza' : 4,
		'destreza' : 5,
		'constitucion' : 4,
		'velocidad' : 10,
		'inteligencia' : 1,
		'percepcion' : 6,
		'esperanzaVida' : 60,
		'fecundidad' : 1,
		'madurezSexual': 1}

#_init__(self, nodo, especie, edad, sexo, cromosoma):
nodo = ae.Nodo(None,None,oCuniculus)
granValle.newConejo([individuo.Conejo(nodo, oCuniculus, 5, 1, cromosoma2)])
#nodo = ae.Nodo(None,None,oCuniculus)
#granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 5, 1, cromosoma3)])
nodo = ae.Nodo(None,None,oCuniculus)
granValle.newConejo([individuo.Conejo(nodo, oCuniculus, 5, 0, cromosoma1)])
#nodo = ae.Nodo(None,None,oCuniculus)
#granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 5, 0, cromosoma4)])
#nodo = ae.Nodo(None,None,oCuniculus)
#granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 5, 1, cromosoma2)])
#nodo = ae.Nodo(None,None,oCuniculus)
#granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 5, 1, cromosoma3)])
#nodo = ae.Nodo(None,None,oCuniculus)
#granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 5, 0, cromosoma1)])
#nodo = ae.Nodo(None,None,oCuniculus)
#granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 5, 0, cromosoma4)])

#Crear lobos
CanisLupus = ae.ArbolEspecie() # Lobo
#nodo = ae.Nodo(None,None,CanisLupus)
#granValle.newZorro([individuo.Zorro(nodo, CanisLupus, 5, 0, cromosoma4)])

for i in range(0,20):
	viajes = []
	for tierra in territorios:
		if len(tierra.conejos) == 3:
			nodo = ae.Nodo(None,None,CanisLupus)
			granValle.newZorro([individuo.Zorro(nodo, CanisLupus, 5, 0, cromosoma4)])
		orgia = []
		llorones = []
		victimas = []
		turnos = []
		print("\n#########  DECLARAR  #########")
		declara = tierra.getDeclaraciones()
		for i in declara:
			print (str(i) + " " + str(i.nodo.indice))
			print("Energia " + str(i.energia) + "/" + str(i.getCapacidadEnergia()))
			print("Inventario " + str(i.inventario) + "/" + str(i.getCapacidadCarga()))
			print("Felicidad " + str(i.felicidad))
			decision = i.getDecision(tierra.getAcciones(i, orgia, llorones, victimas), orgia, llorones, victimas) # Decision es una tupla
			turnos.append((i, decision))
			print (decision)
			print ("\n")
		print("\n#########  ACTUAR  #########")
		tierra.getIniciativas(turnos)
		for i in turnos:
			i[0].actuar(i[1], viajes)
		print("\n\n\n")
	for tierra in territorios:
		tierra.elMundoSeMueve()























#_7#for i in range(0,200):
#_7#	viajes = []
#_7#	for tierra in territorios:
#_7#		orgia = []
#_7#		llorones = []
#_7#		victimas = []
#_7#		turnos = []
#_7#		print("\n\ndeclara")
#_7#		declara = tierra.getDeclaraciones()
#_7#		for i in declara:
#_7#			decision = i.getDecision(tierra.getAcciones(i, orgia, llorones, victimas), orgia, llorones, victimas) # Decision es una tupla
#_7#			turnos.append((i, decision))
#_7#			print (i.nodo.indice)
#_7#			print(str(i.energia) + "/" + str(i.getCapacidadEnergia()))
#_7#			print(str(i.inventario) + "/" + str(i.getCapacidadCarga()))
#_7#			print(i.felicidad)
#_7#			print (decision)
#_7#		print("\n\naccion")
#_7#		tierra.getIniciativas(turnos)
#_7#		for i in turnos:
#_7#			i[0].actuar(i[1], viajes)
#_7#		print("\n\n\n")
#_7#
#_7#	for viaje in viajes:
#_7#		print ("jajajaajajajajajaa")
#_7#		print(len(granValle.conejos))
#_7#		print(len(granValle2.conejos))
#_7#		viaje[0].viajar(viaje[1],viaje[2])
#_7#		print(len(granValle.conejos))
#_7#		print(len(granValle2.conejos))
#_7#	for tierra in territorios:
#_7#		tierra.elMundoSeMueve()
#_7#
#_7#print(len(granValle.conejos))
#_7#print(len(granValle2.conejos))
#_7#
























#_6#for i in range(0,500):
#_6#	orgia = []
#_6#	llorones = []
#_6#	victimas = []
#_6#	turnos = []
#_6#	print("\n\ndeclara")
#_6#	declara = granValle.getDeclaraciones()
#_6#	for i in declara:
#_6#		decision = i.getDecision(granValle.getAcciones(i, orgia, llorones, victimas), orgia, llorones, victimas) # Decision es una tupla
#_6#		turnos.append((i, decision))
#_6#		print (i.nodo.indice)
#_6#		print(str(i.energia) + "/" + str(i.getCapacidadEnergia()))
#_6#		print(str(i.inventario) + "/" + str(i.getCapacidadCarga()))
#_6#		print (decision)
#_6#	print("\n\naccion")
#_6#	granValle.getIniciativas(turnos)
#_6#	for i in turnos:
#_6#		i[0].actuar(i[1])
#_6#
#_6#	granValle.elMundoSeMueve()
#_6#	print("\n\n\n")
#_6#print(len(granValle.conejos))
































#_5#nodo = ae.Nodo(None,None,oCuniculus)
#_5#granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 5, 1, cromosoma2)])
#_5#nodo = ae.Nodo(None,None,oCuniculus)
#_5#granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 5, 1, cromosoma2)])
#_5#nodo = ae.Nodo(None,None,oCuniculus)
#_5#granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 5, 0, cromosoma1)])
#_5#nodo = ae.Nodo(None,None,oCuniculus)
#_5#granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 5, 0, cromosoma1)])
#_5#
#_5#orgia = []
#_5#declara = granValle.getDeclaraciones()
#_5#turnos = []
#_5#print("percepcion")
#_5#for i in declara:
#_5#	print (i.nodo.indice)
#_5#	print (i.cromosoma)
#_5#	turnos.append(granValle.getAcciones(i, orgia))
#_5#print("\n\naccion")
#_5#granValle.getIniciativas(turnos)
#_5#for i in turnos:
#_5#	print (i[0].nodo.indice)
#_5#	print ("\n")
#_5#	for a in turnos:
#_5#		print ("estado")
#_5#		print(a[0].nodo.indice)
#_5#		print (a[0].isFertil())
#_5#	print ("\n\n")
#_5#	if i[1] == "reproducirse":
#_5#		if i[0].isFertil() and i[2].isFertil():
#_5#			print ("proc")
#_5#			print(i[0].nodo.indice)
#_5#			print(i[2].nodo.indice)
#_5#			i[0].procrear(i[2])
#_5#for i in granValle.conejos:
#_5#	if i.cinta:
#_5#		if i.sexo:
#_5#			i.parir()
#_5#		else:
#_5#			granValle.newConejo([i.parir()])
#_5#print(len(granValle.conejos))




#nodo = ae.Nodo(None,None,oCuniculus)
#granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 5, 1, cromosoma2)])
#nodo = ae.Nodo(None,None,oCuniculus)
#granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 5, 1, cromosoma3)])
#nodo = ae.Nodo(None,None,oCuniculus)
#granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 5, 0, cromosoma4)])

#_4#for h in range(0,1):
#_4#	print("\n\nNewronda")
#_4#	orgia = []
#_4#
#_4#	for i in granValle.conejos:
#_4#		print (i.nodo.indice)
#_4#		print (i.cromosoma)
#_4#
#_4#	print ("\n\n")
#_4#	declara = granValle.getDeclaraciones()
#_4#	turnos = []
#_4#	print("percepcion")
#_4#	for i in declara:
#_4#		print (i.nodo.indice)
#_4#		print (i.cromosoma)
#_4#		turnos.append(granValle.getAcciones(i, orgia))
#_4#	print("\n\naccion")
#_4#	granValle.getIniciativas(turnos)
#_4#	for i in turnos:
#_4#		print (i[0].nodo.indice)
#_4#		print ("\n")
#_4#		for a in turnos:
#_4#			print ("estado")
#_4#			print(a[0].nodo.indice)
#_4#			print (a[0].isFertil())
#_4#		print ("\n\n")
#_4#		if i[1] == "reproducirse":
#_4#			if i[0].isFertil() and i[2].isFertil():
#_4#				print ("proc")
#_4#				print(i[0].nodo.indice)
#_4#				print(i[2].nodo.indice)
#_4#				i[0].procrear(i[2])
#_4#
#_4#	for i in granValle.conejos:
#_4#		if i.cinta:
#_4#			granValle.newConejo([i.parir()])
#_4#
#_4#
#_4#
#_4#













######nodo = ae.Nodo(None,None,oCuniculus)
######granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 1, 1, 1,10,1,80,1,2,0)])
######nodo = ae.Nodo(None,None,oCuniculus)
######granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 1, 1, 1,5,1,100,1,1,0)])
######nodo = ae.Nodo(None,None,oCuniculus)
######granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 1, 1, 1,4,1,30,1,5,0)])
######nodo = ae.Nodo(None,None,oCuniculus)
######granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 1, 1, 1,1,1,50,1,3,0)])
######nodo = ae.Nodo(None,None,oCuniculus)
######granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 1, 1, 1,8,1,81,1,4,0)])


#_3#
#_3#a = granValle.conejos
#_3#for i in granValle.conejos:
#_3#	print (i.nodo.indice)
#_3#	print (i.cromosoma)
#_3#
#_3#print ("\n\n")
#_3#declara = granValle.getDeclaraciones()
#_3#turnos = []
#_3#print("percepcion")
#_3#for i in declara:
#_3#	print (i.nodo.indice)
#_3#	print (i.cromosoma)
#_3#	turnos.append((i, "jaja"))
#_3#print("\n\naccion")
#_3#granValle.getIniciativas(turnos)
#_3#for i in turnos:
#_3#	print (i[0].nodo.indice)
#_3#	print (i[0].cromosoma)
#_3#
#_3#
#_3#









#_2#for i in range(0,2):
#_2#	nodo = ae.Nodo(None,None,oCuniculus)
#_2#	granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 1, 1, 1,1,1,80,1,1,0)])
#_2#	nodo = ae.Nodo(None,None,oCuniculus)
#_2#	granValle.newConejo([individuo.Individuo(nodo, oCuniculus, 2, 2, 2,2,2,80,2,2,1)])
#_2#	for i in granValle.conejos:
#_2#		print (i.nodo.indice)
#_2#		print (i.cromosoma)
#_2#	print("\n")
#_2#	granValle.conejos[0].procrear(granValle.conejos[1])
#_2#	granValle.newConejo([granValle.conejos[0].parir()])
#_2#	for i in granValle.conejos:
#_2#		print (i.nodo.indice)
#_2#		print (i.cromosoma)
#_2#	print("\n\n")
#_2#print(oCuniculus.getDistancia(granValle.conejos[0].nodo.indice, granValle.conejos[1].nodo.indice))
#_2#print(oCuniculus.getDistancia(granValle.conejos[0].nodo.indice, granValle.conejos[2].nodo.indice))
#_2#print(oCuniculus.getDistancia(granValle.conejos[0].nodo.indice, granValle.conejos[3].nodo.indice))
#_2#print(oCuniculus.getDistancia(granValle.conejos[0].nodo.indice, granValle.conejos[4].nodo.indice))
#_2#print(oCuniculus.getDistancia(granValle.conejos[0].nodo.indice, granValle.conejos[5].nodo.indice))
#_2#print(oCuniculus.getDistancia(granValle.conejos[1].nodo.indice, granValle.conejos[2].nodo.indice))
#_2#print(oCuniculus.getDistancia(granValle.conejos[5].nodo.indice, granValle.conejos[2].nodo.indice))
#_2#print(oCuniculus.getDistancia(granValle.conejos[5].nodo.indice, granValle.conejos[3].nodo.indice))
#_2#print(oCuniculus.getDistancia(granValle.conejos[5].nodo.indice, granValle.conejos[4].nodo.indice))
#_2#granValle.conejos[2].procrear(granValle.conejos[4])
#_2#granValle.newConejo([granValle.conejos[2].parir()])
#_2#print(oCuniculus.getDistancia(granValle.conejos[0].nodo.indice, granValle.conejos[6].nodo.indice))
#_2#print(oCuniculus.getDistancia(granValle.conejos[1].nodo.indice, granValle.conejos[6].nodo.indice))
#_2#print(oCuniculus.getDistancia(granValle.conejos[3].nodo.indice, granValle.conejos[6].nodo.indice))
#_2#print(oCuniculus.getDistancia(granValle.conejos[5].nodo.indice, granValle.conejos[6].nodo.indice))





#_#
#_##Crear lobos
#_#CanisLupus = ae.ArbolEspecie() # Lobo
#_#
#_##Bucle
#_#for i in range(0,15000):
#_#	#Conejos comen
#_#	for conejo in granValle.conejos:
#_#		planta = random.choice(granValle.plantas)
#_#		if (planta.serComido(conejo.obtenerComida())):
#_#			granValle.morirPlanta(planta)
#_#
#_#	#print("conejos comen")
#_#	#for planta in granValle.plantas:
#_#	#	print (planta.__dict__)	
#_#	#plantas hacen
#_#	plantitas = []
#_#	for planta in granValle.plantas:
#_#		plantitas += planta.crecer()
#_#	granValle.NewPlanta(plantitas)
#_#
#_#	if not i%5:
#_#		esporas = 0
#_#		madurez = 0
#_#		crecimiento = 0
#_#		if not i%100 and len(granValle.plantas) == 100 and i<1200:
#_#			for h in range(0,20):
#_#				nodo = ae.Nodo(None,None,oCuniculus)
#_#				granValle.newConejo([individuo.Individuo(nodo, 1, 1, 1, 1,1,1,80,1,1)])
#_#		for planta in granValle.plantas:
#_#			esporas += planta.cromosoma['esporas']
#_#			madurez += planta.cromosoma['madurez']
#_#			crecimiento += planta.cromosoma['crecimiento']
#_#		print ("REPORT " + str(i))
#_#		print (esporas/len(granValle.plantas))
#_#		print (madurez/len(granValle.plantas))
#_#		print (crecimiento/len(granValle.plantas))
#_#		#print (planta.__dict__)
#_#		print (len(granValle.plantas))