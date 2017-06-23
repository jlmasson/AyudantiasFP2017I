import numpy as np

# Tema 2
visitados = ["maria2|www.facebook.com|160", "xavi7|www.eluniverso.com|50",
       "jose15|www.sri.gob.ec|30", "maria2|www.twitter.com|30",
       "xavi7|www.inec.gob.ec|10", "maria2|www.espol.edu.ec|50",
	   "jose15|www.sri.gob.ec|120", "xavi7|www.sri.gob.ec|20", 
	   "maria2|www.twitter.com|20"]

empleados = ["maria2", "jose15", "xavi7"]
trabajo = ["www.espol.edu.ec", "www.inec.gob.ec", "www.sri.gob.ec"]

# Creo una lista vacía que almacenará los sitios que son de no trabajo
noTrabajo = []

# Recorro cada elemento de la lista visitados
# La trato como visita
for visita in visitados:
	componentes = visita.strip().split("|")
	sitio = componentes[1].strip().lower()

	# Para saber si un sitio es de no trabajo,
	# debo asegurarme que no existe en la lista trabajo
	if sitio not in trabajo:
		# Una vez que se sabe que es de no trabajo
		# se debe validar que no se encuentre en la lista
		# de no trabajo, puesto que solo debe estar una sola vez.
		if sitio not in noTrabajo:
			noTrabajo.append(sitio)

# Literal b
n = len(empleados) # Total de empleados
p = len(trabajo) # Total de sitios de trabajo
q = len(noTrabajo) # Total de sitio de no trabajo

m = p + q # Total de sitios

# Inicializo una matriz llena de ceros
# Las filas representan a los empleados
# Las columnas representan a los sitios.
# Las columnas se dividen en dos regiones:
# Trabajo y No Trabajo
minutos = np.zeros((n, m), int)

for visita in visitados:
	componentes = visita.strip().split("|")
	usuario = componentes[0].strip()
	sitio = componentes[1].strip()
	tiempo = int(componentes[-1])

	f = c = -1
	if usuario in empleados:
		f = empleados.index(usuario)
	if sitio in trabajo:
		c = trabajo.index(sitio)
	elif sitio in noTrabajo:
		c = noTrabajo.index(sitio) + p

	if f != -1 and c != -1:
		minutos[f, c] += tiempo

print(minutos)

# Tema 3
# Literal a
minutosTotales = minutos.sum()
print("\nTotal minutos de Internet: {}".format(minutosTotales))

# Literal b
minutosEmpleado = minutos.sum(axis=1)
print('\nTotal minutos por empleado: ')
for i, minEmp in enumerate(minutosEmpleado):
	nombreEmpleado = empleados[i]
	print("\t{}: {}".format(nombreEmpleado, minEmp))

# Literal c
minutosSitio = minutos.sum(axis=0)
print('\nTotal minutos por sitio: ')
for i, minSit in enumerate(minutosSitio):
	sitio = ""
	if i < p:
		sitio = trabajo[i]
	elif i < p + q:
		sitio = noTrabajo[i - p]

	print("\t{}: {}".format(sitio, minSit))

# Literal d
minutosTrabajo = minutosSitio[: p].sum()
print("\nTotal minutos de trabajo: {}".format(minutosTrabajo))

# Literal e
minutosNoTrabajo = minutosTotales - minutosTrabajo
print("\nTotal minutos de no trabajo: {}".format(minutosNoTrabajo))

# Literal f
matrizNoTrabajo = minutos[: , p :]
sumaNoTrabajo = matrizNoTrabajo.sum(axis=1)
indiceEmpMax = sumaNoTrabajo.argmax()
usuarioMax = empleados[indiceEmpMax]
print("\nEmpleado con más minutos: {}".format(usuarioMax))

# Literal g
sumaTrabajo = minutosSitio[: p]
indMaxTrab = sumaTrabajo.argmax()
sitioTrabMax = trabajo[indMaxTrab]

print("\nSitio de trabajo con más minutos: {}".format(sitioTrabMax))

# Literal h
costo = 0.05
costoTrabajo = minutosTrabajo * costo
costoNoTrabajo = minutosNoTrabajo * 2 * costo
costoTotal = costoTrabajo + costoNoTrabajo
print("\nCosto total por minutos utilizados: {:.2f} dólares".format(costoTotal))

# Literal i
visitas = np.where(minutos > 0, 1, 0)
visitasXSitio = visitas.sum(axis=0)
print('\nTotal visitas por sitio: ')
for i, visSit in enumerate(visitasXSitio):
	sitio = ""
	if i < p:
		sitio = trabajo[i]
	elif i < p + q:
		sitio = noTrabajo[i - p]

	print("\t{}: {}".format(sitio, visSit))