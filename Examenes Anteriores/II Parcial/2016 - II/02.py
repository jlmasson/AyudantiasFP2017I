# Función que permite cargar un archivo y retorna un diccionario de ciudades
# con sus respectivas métricas.
# Ejemplo de la estructura clave - valor
# ciudad : {metrica1: valor1, metrica2: valor2}
def cargarDatos(nomFile):
	d = {}
	f = open(nomFile)
	for line in f:
		campos = line.strip().split(",")
		ciudad = campos[0].strip()
		# Si la ciudad no existe como clave en el diccionario, procedemos a 
		# asignarle como valor un diccionario vacío
		if ciudad not in d:
			d[ciudad] = {}
		# Obtenemos el diccionario que tiene asignado como valor la ciudad, este
		# puede ser vacío (puesto que la ciudad recién haya sido agregada por el
		# condicional anterior, o ya contenga información, en caso que el valor de
		# verdad de la expresión en el condicional sea falso)
		# Como se explicó en otros ejercicios, se utiliza el concepto de referencia
		# donde si tenemos por ejemplo:
		# a = [2, 4, 6]
		# b = a
		# b[0] = 10
		# Entonces la referencia ha sido modificada, y se tiene -> [10, 4, 6]
		# Este mismo concepto aplica para el diccionario y demás colecciones.
		metricas = d[ciudad]
		metrica = campos[1].strip()
		if metrica not in metricas:
			valorMetrica = int(campos[2])
			metricas[metrica] = valorMetrica
	f.close()
	return d

# Función que permite calcular el promedio de las métricas por cada país existente en el
# diccionario datos
# Estructura del par clave - valor del diccionario que se retornará
# pais : {metrica1: promedio1, metrica2: promedio2}
def metricaPais(datos, paises):
	promedios = {}
	# Dado que la clave del diccionario será el país, se procede a recorrer el diccionario
	# países, para eso se obtienen el par clave valor, donde la clave es el país,
	# y el valor es la lista de ciudades, misma que nos permitirá saber si la ciudad (clave)
	# del diccionario datos pertenece a ella, si pertenece a esta lista, significa que es de
	# ese país y se procederá a acumular el valor de sus métricas.
	for pais, listaCiudades in paises.items():
		# Variable que hará de contadora de las ciudades que pertenecen al país en cuestión.
		# Nótese que este contador está en base a las ciudades que son las claves del diccionario
		# datos.
		ciudadesXPais = 0
		# Diccionario que se crea por cada país existente en el diccionario paises
		# Contendrá los promedios por métrica y únicamente será agregado al diccionario promedios
		# si la variable ciudadesXPais sea mayor que 0
		metricasXPais = {}
		# Obtengo el par clave - valor del diccionario datos, donde la ciudad es la clave, y el valor
		# es el diccionario metricas, cuyo par clave - valor es la metrica y su correspondiente valor.
		for ciudad, metricas in datos.items():
			# Solo se agrega al diccionario por pais siempre y cuando la ciudad pertenece a la lista
			# de ciudades. En caso de hacerlo, significa que la ciudad pertenece a ese país, y por ende
			# el contador de las ciudades se incrementa en uno, asi como sus respectivas métricas en el
			# diccionario metricasXPais.
			if ciudad in listaCiudades:
				ciudadesXPais += 1
				for metrica, valorMetrica in metricas.items():
					if metrica not in metricasXPais:
						metricasXPais[metrica] = 0
					metricasXPais[metrica] += valorMetrica
		# Solo se calcula el promedio siempre y cuando la cantidad de ciudades existentes en el diccionario
		# por el país que se está preguntando sea mayor a 0, en caso de serlo, significa que se lo calculará
		# y procederá a agregar al diccionario promedios.
		if ciudadesXPais > 0:
			for metrica in metricasXPais:
				metricasXPais[metrica] /= ciudadesXPais
			promedios[pais] = metricasXPais
	return promedios

# Función que genera un archivo cuyo nombre es metrica.csv, donde metrica puede ser únicamente:
# precioCasas o temperatura.
def generaPaises(promedios, metrica, minimo, maximo):
	# El archivo puede ser visto como una cadena de caracteres, por lo cual se procede a armar la cadena
	# de acuerdo a las condiciones planteadas.
	cadena = ""
	# Obtengo el país, y las métricas referentes al él, luego se trabaja con la métrica que se pasa como
	# parámetro en la función para así obtener su valor respectivo y compararlo con los límites permitidos
	# De pertenecer el valor de la métrica en ese intervalo, se procede a agregar esa información a la cadena
	# de caracteres.
	for pais, metricas in promedios.items():
		if metrica in metricas:
			valorMetrica = metricas[metrica]
			if valorMetrica >= minimo and valorMetrica <= maximo:
				cadena += "{},{},{}\n".format(pais, metrica, valorMetrica)
	# Se busca que no existan archivos vacíos, para lo cual se procede a preguntar si la longitud de la cadena es
	# mayor a 0, indicando que si se añadió información a esta y por ende, existe el archivo.
	if len(cadena) > 0:
		f = open("{}.csv".format(metrica), "w")
		f.write(cadena)
		f.close()

# Cargando el diccionario
datos = cargarDatos("datos.txt")
print("\nDatos:\n\n{}\n".format(datos))

# Creando un diccionario países de prueba
paises = {}
paises["Ecuador"] = ["Guayaquil", "Quito", "Cuenca"]
paises["Colombia"] = ["Bogota", "Cali", "Barranquilla"]

# Cargando el diccionario de promedios por pais
promedios = metricaPais(datos, paises)

print("Promedios:\n\n{}\n".format(promedios))

generaPaises(promedios, "temperatura", 23, 26)