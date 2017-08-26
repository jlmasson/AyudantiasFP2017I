# Función que cuenta el número de veces que se repite
# una etiqueta en determinadas fechas.
def cuentaEtiquetas(tendencias, listaFechas):
	# Diccionario que tendrá como clave la etiqueta y como valor
	# el número de veces que se repite en la listaFechas
	etiquetas = {}
	for fecha in listaFechas:
		# Valido en caso que la fecha no se encuentra, entonces el
		# programa se cae puesto que la clave no existe.
		# Tome en cuenta que para el diccionario tendencias, la clave
		# es la fecha en formato mm-dd-yyyy y su valor es un conjunto
		# con las etiquetas que fueron tendencia en esa fecha
		if fecha in tendencias:
			# Obtengo el conjunto de etiquetas de esa fecha
			etiquetasFecha = tendencias[fecha]
			# Recorro cada etiqueta del conjunto para proceder a contarla
			# y actualizar el diccionario etiquetas
			for etiqueta in etiquetasFecha:
				if etiqueta not in etiquetas:
					etiquetas[etiqueta] = 1
				else:
					etiquetas[etiqueta] += 1
	return etiquetas

# Función que muestra por pantalla las etiquetas que fueron tendencia
# en todas las fechas que se encuentran en listaFechas y las que fueron
# tendencia en al menos una de ellas.
# Nótese que esta función no retorna un valor, puesto que solo muestra por
# pantalla.
def reportaTendencias(tendencias, listaFechas):
	# Aprovecho la función que cuenta las etiquetas para obtener
	# el diccionario con el conteo respectivo por cada etiqueta.
	etiquetas = cuentaEtiquetas(tendencias, listaFechas)
	# Creo dos listas vacías, una que contenga las etiquetas que fueron tendencia
	# en todas las fechas y otra que contenga a las que fueron tendencia por lo
	# menos en una fecha presente en listaFechas
	todas = []
	algunas = []
	todasLasFechas = "Etiquetas que fueron tendencia en todas las fechas:\n"
	unaDeLasFechas = "Etiquetas que fueron tendencia en al menos una de las fechas:\n"
	for etiqueta, numVeces in etiquetas.items():
		# Condición que asegura que el numero de veces que se repite la etiqueta
		# sea igual a la longitud de listaFechas (cantidad de fechas), indicando
		# así que esta etiqueta estuvo presente en todas las fechas de la lista.
		if numVeces == len(listaFechas):
			todas.append("\t{}\n".format(etiqueta))
		# Condición independiente de la primera, por esa razón no utilizo
		# un elif, puesto que una etiqueta que fue tendencia en todas las fechas
		# también lo es en al menos una de las fechas, por esa razón
		# la cantidad de repeticiones tiene que ser mayor o igual a 1.
		if numVeces >= 1:
			algunas.append("\t{}\n".format(etiqueta))
	
	print(todasLasFechas)
	mostrarEtiquetas(todas)

	print(unaDeLasFechas)
	mostrarEtiquetas(algunas)

# Función auxiliar que permite mostrar por pantalla las etiquetas
# dado que es el mismo procedimiento para ambas, se procedió a realizarla
# para evitarse escribir el código dos veces
# Esta función no es pedida en los literales del examen, pero también
# pueden hacerse sus propias funciones para estos casos
def mostrarEtiquetas(listaEtiquetas):
	if len(listaEtiquetas) > 0:
		etiquetas = "".join(listaEtiquetas)
		print(etiquetas)
	else:
		print("\tNinguna\n")

# Función que muestra por pantalla las etiquetas que fueron tendencia
# o en fecha1 o en fecha2 pero no en ambas.
# Esto es en otras palabras la definición "informal" de la diferencia
# simétrica que se procede a utilizar.
# No retorna ningún valor.
def tendenciasExcluyentes(tendencias, fecha1, fecha2):
	etiquetasF1 = tendencias[fecha1]
	etiquetasF2 = tendencias[fecha2]
	excluyentes = etiquetasF1 ^ etiquetasF2
	
	print("Tendencias excluyentes:\n")
	if len(excluyentes) > 0:
		i = 0
		for etiqueta in excluyentes:
			print("\t{}) {}".format(i + 1, etiqueta))
			i += 1
	else:
		print("\tNinguna\n")

# Programa principal de prueba
tendencias = {"08-22-2016": {"#Rio2016", "#BSC", "#ECU"}, 
			  "08-25-2016": {"#GYE", "#BRA"}, 
			  "08-27-2016": {"#YoSoyEspol", "#GYE", "#BSC"}}

listaFechas = ["08-22-2016", "08-25-2016", "08-27-2016"]
# Prueba de cuentaEtiquetas
print()
print(cuentaEtiquetas(tendencias, listaFechas))
print()

# Prueba de reportaTendencias
reportaTendencias(tendencias, listaFechas)

# Prueba de tendenciasExcluyentes
tendenciasExcluyentes(tendencias, "08-22-2016", "08-25-2016")
print()
