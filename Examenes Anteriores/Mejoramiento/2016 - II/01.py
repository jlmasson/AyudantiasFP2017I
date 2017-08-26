def obtenerClientes(nombreArchivo):
	d = {}
	f = open(nombreArchivo)
	for line in f:
		line = line.strip()
		campos = line.split(",")
		cedula = campos[0].strip()
		if cedula not in d:
			d[cedula] = {}
		numeros = d[cedula]
		num = campos[1].strip()
		if num not in numeros:
			infoN = {}
			sector = campos[2].strip()
			estado = campos[-1].strip()
			local, inter = campos[-2].split("|")
			local = int(local)
			inter = int(inter)
			infoN["estado"] = estado
			infoN["sector"] = sector
			infoN["local"] = local
			infoN["inter"] = inter
			numeros[num] = infoN
	f.close()
	return d

def calcularCosto(minutos, tipo=1):
	costo = 0
	if tipo == 1:
		costo = 0.03
	elif tipo == 2:
		if minutos < 60:
			costo = 0.05
		elif minutos <= 90:
			costo = 0.04
		else:
			costo = 0.03
	return minutos * costo

def generarFactura(dClientes):
	for cliente, numeros in dClientes.items():
		f = open("{}.txt".format(cliente), 'w')
		factura = ""
		factura += "Empresa Telefonica de Guayaquil"
		factura += "\nCliente: {}".format(cliente)
		factura += "\nDetalle Deuda:"
		totalAPagar = 0
		for numero, infoNumero in numeros.items():
			local = infoNumero["local"]
			inter = infoNumero["inter"]
			costoN = calcularCosto(local)
			costoI = calcularCosto(inter, 2)
			costoT = costoN + costoI
			totalAPagar += costoT
			factura += "\n{} local:{} inter:{} total:{}".format(numero, costoN, costoI, costoT)
		f.write(factura)
		f.close()


def estadisticaSector(dClientes, area):
	promedios = {}
	promedios["Locales"] = promedios["Internacionales"] = 0
	totalNumeros = 0
	for numeros in dClientes.values():
		for infoNumero in numeros.values():
			areaN = infoNumero["area"].lower()
			estadoN = infoNumero["estado"].lower()
			if area.lower() == areaN and estadoN == "cortado":
				totalNumeros += 1
				promedios["Locales"] += infoNumero["local"]
				promedios["Internacionales"] += infoNumero["inter"]
	for tipoNumero in promedios:
		promedios[tipoNumero] /= totalNumeros
	return promedios