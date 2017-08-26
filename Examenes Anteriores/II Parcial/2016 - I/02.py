def cargarDatos(nombreArchivo):
	d = {}
	f = open(nombreArchivo)
	for line in f:
		campos = line.strip().split("|")
		origen = campos[0].strip()
		destinos = {}
		for infoDestino in campos[1: ]:
			destino, distancia = infoDestino.strip().split(",")
			destino = destino.strip()
			distancia = int(distancia)
			destinos[destino] = distancia
		d[origen] = destinos
	f.close()
	return d

def ciudadesCercanas(distancias, km):
	cercanas = []
	for origen, destinos in distancias.items():
		for destino, distancia in destinos.items():
			if distancia <= km:
				t = (origen, destino, distancia)
				cercanas.append(t)
	return cercanas

def guardarCiudadesCercanas(distancias, listaKms):
	for km in listaKms:
		cercanas = ciudadesCercanas(distancias, km)
		if len(cercanas) > 0:
			nombreArchivo = "ciudades{}.txt".format(km)
			f = open(nombreArchivo, "w")
			for t in cercanas:
				linea = "{},{},{}\n".format(t[0], t[1], t[2])
				f.write(linea)
			f.close()

# Programa principal
d = cargarDatos("Ecuador_Distancias.txt")
guardarCiudadesCercanas(d, [150, 225, 320, 555])