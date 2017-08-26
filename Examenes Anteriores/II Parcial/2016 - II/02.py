def cargarDatos(nomFile):
	d = {}
	f = open(nomFile)
	for line in f:
		campos = line.strip().split(",")
		ciudad = campos[0].strip()
		if ciudad not in d:
			d[ciudad] = {}
		metricas = d[ciudad]
		metrica = campos[1].strip()
		if metrica not in metricas:
			valorMetrica = int(campos[2])
			metricas[metrica] = valorMetrica
	f.close()
	return d

def metricaPais(datos, paises):
	promedios = {}
	for pais, listaCiudades in paises.items():
		ciudadesXPais = 0
		metricasXPais = {}
		for ciudad, metricas in datos.items():
			if ciudad in listaCiudades:
				ciudadesXPais += 1
				for metrica, valorMetrica in metricas.items():
					if metrica not in metricasXPais:
						metricasXPais[metrica] = 0
					metricasXPais[metrica] += valorMetrica
		if ciudadesXPais > 0:
			for metrica in metricasXPais:
				metricasXPais[metrica] /= ciudadesXPais
			promedios[pais] = metricasXPais
	return promedios

def generaPaises(promedios, metrica, minimo, maximo):
	cadena = ""
	for pais, metricas in promedios.items():
		if metrica in metricas:
			valorMetrica = metricas[metrica]
			if valorMetrica >= minimo and valorMetrica <= maximo:
				cadena += "{},{},{}\n".format(pais, metrica, valorMetrica)
	if len(cadena) > 0:
		f = open("{}.csv".format(metrica), "w")
		f.write(cadena)
		f.close()