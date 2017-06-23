transacciones = ["centro|Bahia|futbol|zapatos-Adidas|290.78|25-03-2013",
    	"centro|Malecon2000|natación|chaleco-Fins|110.92|01-02-2014",
    	"sur|MallDelSur|natacion|gafasPiscina-Swingo|90.07|13-05-2014",
    	"centro|Bahia|natacion|zapatos-Nike|315.72|13-12-2015",
    	"norte|CityMall|natacion|gafasPiscina-Adidas|310.19|31-05-2016"]
 
sur = []
centro = []
norte = []

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

totalVentas = 0
anio = int(input("Ingrese anio: "))

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