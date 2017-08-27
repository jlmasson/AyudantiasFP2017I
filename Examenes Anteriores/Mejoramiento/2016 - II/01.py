# Función que permite la carga del archivo en un diccionario de 3 niveles.
def obtenerClientes(nombreArchivo):
	d = {}
	f = open(nombreArchivo)
	for line in f:
		line = line.strip()
		campos = line.split(",")
		cedula = campos[0].strip()
		# El truco para dejar el diccionario en 2 niveles, es eliminando un nivel
		# a través del número de cédula y de conceptos claves del 1er parcial
		if cedula not in d:
			d[cedula] = {}
		# Aquí aplica lo del 1er parcial visto en listas.
		# Para recordarlo se lo va a ilustrar de la siguiente manera:
		# a = [2, 3, 4]
		# b = a
		# b[0] = 10
		# Dado que se tiene una lista a con 3 valores, y una variable b que apunta
		# a la lista a (no a su copia), entonces todas las modificaciones que se hagan
		# con el identificador b, harán que se afecte la lista a y viceversa.
		# Este mismo concepto aplica con los diccionarios.
		# Supongamos lo siguiente:
		# d = {1: 3}
		# e = d
		# e[10] = 2
		# Con este cambio y el concepto claro, se tiene que d -> {1: 3, 10: 2}
		# Así mismo si realizo una modificación con d, por ejemplo:
		# d[1] = 4
		# Y muestro e, entonces quedaría -> {1: 4, 10: 2}
		# Y este concepto fundamental, permite que nuestro problema de 3 niveles, se convierta
		# en uno sencillo de dos, con más facilidades para su respectiva manipulación.
		
		# La variable numeros apunta al diccionario que contendra toda la informacion referente
		# a los numeros que tiene asociado el cliente.
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
			infoN["area"] = sector
			infoN["local"] = local
			infoN["inter"] = inter
			numeros[num] = infoN
	f.close()
	return d

# Función adicional (No pedida), que recibe como parámetro la cantidad de minutos
# y el tipo. Si tipo es 1, significa que es nacional, o si tipo es 2, es internacional.
# Cualquier otro tipo no es considerado para la modificación del costo del minuto.
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

# Función que genera la factura por cada cliente.
def generarFactura(dClientes):
	# Dado que el diccionario dClientes es de 3 niveles, se conoce que la clave va a ser
	# el número de cédula del cliente.
	for cliente, numeros in dClientes.items():
		# El archivo se abre en modo de escritura, porque se va a proceder a crear y 
		# añadir texto en él.
		f = open("{}.txt".format(cliente), 'w')
		# El archivo puede ser visto como una sola cadena de caracteres, por lo cual se procede
		# a construirla para de ahí escribirla en el archivo.
		factura = ""
		factura += "Empresa Telefonica de Guayaquil"
		factura += "\nCliente: {}".format(cliente)
		factura += "\nDetalle Deuda:"
		# Variable acumuladora que será utilizada para escribir al final el total a pagar
		# por cada cliente.
		totalAPagar = 0
		# Recorro el diccionario numeros, que tiene como clave el numero de teléfono, y como valor
		# un diccionario con la información referente a ese número.
		for numero, infoNumero in numeros.items():
			local = infoNumero["local"]
			inter = infoNumero["inter"]
			# Procedo a calcular el costo de los minutos, de acuerdo a su tipo
			# tipo = 1 -> nacional, tipo = 2 -> internacional
			costoN = calcularCosto(local)
			costoI = calcularCosto(inter, 2)
			# costoT representa el costo total por aquel número, y este se acumula para el 
			# total a pagar
			costoT = costoN + costoI
			totalAPagar += costoT
			factura += "\n{} local:{:.2f} inter:{:.2f} total:{:.2f}".format(numero, costoN, costoI, costoT)
		factura += "\nTotal a Pagar:{:.2f}\n".format(totalAPagar)
		# Se escribe en el archivo
		f.write(factura)
		# Se cierra el archivo.
		f.close()

# Función que obtiene el promedio de los minutos nacionales e internacionales de los teléfonos que se encuentran
# en el área especificada por el parámetro y su estado sea cortado.
def estadisticaSector(dClientes, area):
	promedios = {}
	promedios["Locales"] = promedios["Internacionales"] = 0
	# Variable contadora que me permitirá calcular el promedio una vez que haya acumulado
	# todos los minutos nacionales e internacionales de los números telefónicos que cumplan con la condición
	# que fue descrita al inicio de la función
	totalNumeros = 0
	for numeros in dClientes.values():
		for infoNumero in numeros.values():
			areaN = infoNumero["area"].lower()
			estadoN = infoNumero["estado"].lower()
			if area.lower() == areaN and estadoN == "cortado":
				totalNumeros += 1
				promedios["Locales"] += infoNumero["local"]
				promedios["Internacionales"] += infoNumero["inter"]
	# Se valida que el contador sea mayor que 0, puesto que no se puede realizar una división para 0.
	if totalNumeros > 0:
		for tipoNumero in promedios:
			promedios[tipoNumero] /= totalNumeros
	return promedios

# Carga de diccionario
clientes = obtenerClientes("clientes.txt")
print("\nClientes:\n\n{}\n".format(clientes))

# Generación de facturas por cada cliente
generarFactura(clientes)

# Estadísticas por sector
promediosNorte = estadisticaSector(clientes, "Norte")

print("Estadísticas Norte:\n\n{}\n".format(promediosNorte))
