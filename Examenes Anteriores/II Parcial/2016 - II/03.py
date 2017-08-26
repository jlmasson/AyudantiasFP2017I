transacciones = ["centro|Bahia|futbol|zapatos-Adidas|290.78|25-03-2013",
    	"centro|Malecon2000|natación|chaleco-Fins|110.92|01-02-2014",
    	"sur|MallDelSur|natacion|gafasPiscina-Swingo|90.07|13-05-2014",
    	"centro|Bahia|natacion|zapatos-Nike|315.72|13-12-2015",
    	"norte|CityMall|natacion|gafasPiscina-Adidas|310.19|31-05-2016"]

# Se procede a crear una lista para cada sector. 
sur = []
centro = []
norte = []

# Literal a

# Se recorre cada transacción, para luego obtener el sector
# y la tienda. Con el sector se procede a agregar a la lista
# correspondiente y de manera única.
for transaccion in transacciones:
	componentes = transaccion.strip().split("|")
	sector = componentes[0].strip().lower()
	tienda = componentes[1].strip()
	if sector == "sur":
		if tienda not in sur:
			sur.append(tienda)
	elif sector == "centro":
		if tienda not in centro:
			centro.append(tienda)
	elif sector == "norte":
		if tienda not in norte:
			norte.append(tienda)

# Literal b
# Se inicializa el acumulador en 0
totalVentas = 0
anio = int(input("Ingrese anio: "))

# Se recorre cada transacción, para luego obtener la fecha
# y también el producto, puesto que se desea obtener
# la marca y también el mes (adidas y mayo respectivamente)
# Con el año que se le pide al usuario, se lo compara
# con el el año de la transacción, y si cumplen las condiciones
# establecidas, se procede a acumular la venta de esa transacción.
for transaccion in transacciones:
	componentes = transaccion.strip().split("|")
	fecha = componentes[-1]
	producto = componentes[3]
	d, m , a = fecha.split("-")
	m = int(m)
	a = int(a)
	nomb, marca = producto.split("-")
	marca = marca.lower().strip()
	if m == 5 and a == anio and marca == "adidas":
		venta = float(componentes[-2])
		totalVentas += venta

print("Total de ventas en el mes de mayo de {} es {:.2f}".format(anio, totalVentas))