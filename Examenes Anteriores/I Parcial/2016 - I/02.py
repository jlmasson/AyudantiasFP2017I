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

# Se obtiene el tiempo total de uso de internet
minutosTotales = minutos.sum()
print("\nTotal minutos de Internet: {}".format(minutosTotales))

# Literal b

# Para obtener el tiempo total por empleado, se procede a obtener
# la suma de las filas de la matriz, puesto que cada empleado es una
# fila de la matriz
minutosEmpleado = minutos.sum(axis=1)
print('\nTotal minutos por empleado: ')

# Utilizo enumerate puesto que me retorna el índice y el elemento
# correspondiente a ese índice.
# El arreglo es paralelo a la lista empleados, por eso necesito el índice
# para obtener el nombre del empleado.
# Por ejemplo:
# empleados = ['pepe', 'lucho']
# minutosEmpleado = [25 300]
# En la primera iteración, i = 0, minEmp = 25.
# Con el índice obtengo el nombre del empleado
# en este caso nombreEmpleado = empleados[i] <- 'pepe'
# y así sucesivamente.
for i, minEmp in enumerate(minutosEmpleado):
	nombreEmpleado = empleados[i]
	print("\t{}: {}".format(nombreEmpleado, minEmp))

# Literal c

# Para obtener el tiempo total por sitio, se procede a obtener la suma
# de las columnas de la matriz, puesto que cada sitio es una columna
# de la matriz.
minutosSitio = minutos.sum(axis=0)
print('\nTotal minutos por sitio: ')

# Utilizo enumerate puesto que me retorna el índice y el elemento
# correspondiente a ese índice.
# El arreglo es paralelo a la lista trabajo y noTrabajo, por eso necesito el índice
# para obtener el nombre del sitio.
# Por ejemplo:
# trabajo = ['sri.gob.ec', 'espol.edu.ec']
# noTrabajo = ['facebook.com', 'twitter.com', 'eluniverso.com']
# minutosSitio = [25 300 400 100 250]
# En la primera iteración, i = 0, minSit = 25.
# Con el índice obtengo el nombre del sitio
# en este caso sitio = trabajo[i] <- 'sri.gob.ec'
# Sin embargo, tengo dos regiones en las columnas, por ende, pregunto si ese índice
# es menor a la cantidad de columnas que tiene la lista trabajo
# para así obtener el sitio de la lista de trabajo, caso contrario lo obtengo de la
# lista de no trabajo.
# Por ejemplo, cuando i = 2, minSit = 400.
# Sin embargo, p = 2, con lo cual i < p es Falso, y procede a trabajar directamente
# con la condición siguiente, ya que q = 3, y p + q = 5, por ende i < p + q, lo cual
# es Verdadero.
# Como está desplazado p columnas, al índice se le resta el valor de p desplazamientos.
# con lo cual obtengo el sitio correspondiente sitio = noTrabajo[i - p] <- 'facebook.com',
# puesto que para noTrabajo corresponde el índice 0, lo cual es correcto con la resta realizada.
for i, minSit in enumerate(minutosSitio):
	sitio = ""
	if i < p:
		sitio = trabajo[i]
	elif i < p + q:
		sitio = noTrabajo[i - p]

	print("\t{}: {}".format(sitio, minSit))

# Literal d

# A partir del arreglo de los minutos por sitio, procedo a hacer slicing para la región de Trabajo
# y obtengo su suma.
minutosTrabajo = minutosSitio[: p].sum()
print("\nTotal minutos de trabajo: {}".format(minutosTrabajo))

# Literal e

# Dado que tengo el tiempo total de consumo y el tiempo por sitios de trabajo, procedo a restar
# y obtengo el total por sitios de no trabajo.
minutosNoTrabajo = minutosTotales - minutosTrabajo
print("\nTotal minutos de no trabajo: {}".format(minutosNoTrabajo))

# Literal f

# Para obtener el empleado que estuvo más tiempo en sitios de no trabajo, se procede a obtener
# todas las filas de la matriz, pero solo la región con los sitios de no trabajo
matrizNoTrabajo = minutos[: , p :]

# Procedo a sumar las filas de la región obtenida, ya que representan a los empleados.
sumaNoTrabajo = matrizNoTrabajo.sum(axis=1)

# No me interesa el tiempo, sino el nombre del empleado en sí, por ende, obtengo el índice
# donde se encuentra el valor máximo, para así obtener el nombre del empleado de la lista
# empleados.
indiceEmpMax = sumaNoTrabajo.argmax()
usuarioMax = empleados[indiceEmpMax]
print("\nEmpleado con más minutos: {}".format(usuarioMax))

# Literal g

# Procedo a obtener la región de trabajo, a partir de la suma de cada sitio
sumaTrabajo = minutosSitio[: p]

# Similar al literal anterior, me interesa el índice para obtener el nombre del sitio
# de trabajo más visitado por los empleados.
indMaxTrab = sumaTrabajo.argmax()
sitioTrabMax = trabajo[indMaxTrab]

print("\nSitio de trabajo con más minutos: {}".format(sitioTrabMax))

# Literal h

# A partir del tiempo total por sitio de trabajo, y por sitio de no trabajo obtenidos en literales
# anteriores, procedo a obtener el costo total del uso del Internet.
costo = 0.05
costoTrabajo = minutosTrabajo * costo
costoNoTrabajo = minutosNoTrabajo * 2 * costo
costoTotal = costoTrabajo + costoNoTrabajo
print("\nCosto total por minutos utilizados: {:.2f} dólares".format(costoTotal))

# Literal i

# Para obtener las visitas de cada sitio, primero obtengo la matriz visitas a partir de la matriz
# minutos, para eso se usará la función where con otra forma.
# np.where(condicion, valorVerdadero, valorFalso), esto retorna una matriz.
# Si el sitio fue visitado (es decir, el tiempo es mayor a 0 minutos), entonces se procede a colocar
# un 1, caso contrario un 0.
# Luego sumo por columnas, para obtener el total de visitas que recibe cada uno.
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