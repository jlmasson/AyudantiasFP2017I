import numpy as np

sur    = ['LosEsteros','Pradera', 'RiocentroSur']
centro = ['Bahia', 'Malecon2000', 'MaleconSalado']
norte  = ['MallDelSol', 'CityMall', 'RiocentroNorte']

futbol   = ['zapatos-Adidas', 'zapatos-Nike', 'rodilleras-Reebok']
natacion = ['short-Nike', 'gafasPiscina-Swingo', 'aletas-Speedo']

# Necesito las longitudes de cada lista
# Porque existen tres regiones en las filas
# y dos regiones en las columnas
s = len(sur)
c = len(centro)
n = len(norte)

f = len(futbol)
nat = len(natacion)


# La genero de manera automática para hacer pruebas.
M = np.random.randint(1, 100, (s + c + n, f + nat))

# Literal 1

# Sumo por columnas, y luego procedo a hacer
# slicing para obtener el total de fútbol
# y también para el total de natación
sumaProductos = M.sum(axis=0)
sumaFutbol = sumaProductos[ :f].sum()
sumaNatacion = sumaProductos[f: ].sum()

# Se hace la comparación respectiva, lo cual pide el literal
if sumaFutbol > sumaNatacion:
	print("Fútbol tiene más ventas: {:.2f}".format(sumaFutbol))
elif sumaFutbol < sumaNatacion:
	print("Natación tiene más ventas: {:.2f}".format(sumaNatacion))
else:
	print("Iguales: {:.2f}".format(sumaFutbol))

# Literal 2

# Se necesita obtener la tienda con mayor cantidad de ventas
# Por ende se procede a sumar las filas de la matriz M
sumaTiendas = M.sum(axis=1)

# Se obtiene el índice que contiene el valor que tiene la mayor
# cantidad de ventas.
indTiendaMax = sumaTiendas.argmax()

# Se obtiene el valor máximo a partir del índice
montoTiendaMax = sumaTiendas[indTiendaMax]

# Como existen regiones en las filas, se procede a trabajar con el
# índice especificando en qué región cae
# Para el sur -> M[:s]
# Para el centro -> M[s: s + c]
# Para el norte -> M[s + c: s + c + n]
# Como estoy trabajando de la matriz hacia las listas, procedo a 
# restar índices.
# Por ejemplo, supongamos que la matriz M tiene 9 filas, y que cada
# sector tiene 3 filas.
# Y la tienda que vendió más es Malecon2000, la cual está en la lista
# centro y su índice es 1, pero en la matriz tiene índice 4.
# Si utilizo directamente el índice obtenido a partir de la matriz (fila)
# el programa se cae, por ende, debo restar el desplazamiento de las filas,
# ya que las filas del centro se encuentran desplazadas s filas (donde s 
# representa la cantidad de tiendas en el sur).
# Para el norte, se encuentran desplazadas s + c filas.
# El sur no se encuentra desplazado, por ende el índice coincide y no se realiza
# ninguna resta.
# Por ende, del índice debe restarse la cantidad de filas desplazadas de acuerdo a
# la región en la que se encuentra la tienda con el valor máximo.

# Esto también aplica para las columnas que están divididas también por regiones.
tienda = ""
if indTiendaMax < s:
	tienda = sur[indTiendaMax]
elif indTiendaMax < s + c:
	tienda = centro[indTiendaMax - s]
elif indTiendaMax < s + c + n:
	tienda = norte[indTiendaMax - s - c]

print("{} con un monto de {:.2f}".format(tienda, montoTiendaMax))

# Literal 3

# Aquí se hace lo mismo que el literal 2, a excepción de trabajar por
# regiones, puesto que la única región a trabajar es la del norte
tiendasNorte = M[s + c: ]
sumaTiendasNorte = tiendasNorte.sum(axis=1)
indTiendaNorte = sumaTiendasNorte.argmax()
tiendaNorte = norte[indTiendaNorte]
montoNorte = sumaTiendasNorte[indTiendaNorte]
print("{} con un monto de {:.2f}".format(tiendaNorte, montoNorte))


# Literal 4

tiendasSur = M[: s]
sumaProductosSur = tiendasSur.sum(axis=0)
indProdSurMax = sumaProductosSur.argmax()

producto = ""

if indProdSurMax < f:
	producto = futbol[indProdSurMax]
elif indProdSurMax < f + nat:
	producto = natacion[indProdSurMax - f]

print(producto)

# Literal 5

tiendUsuario = input("Ingrese tienda: ")
tiendUsuario = tiendUsuario.strip()

# Debe validarse que la tienda exista para proceder
# con el algoritmo.
while tiendUsuario not in sur and tiendUsuario not in centro and tiendUsuario not in norte:
	print("Tienda no existente.")
	tiendUsuario = input("Ingrese tienda: ")
	tiendUsuario = tiendUsuario.strip()

# -1 lo utilizo para validar, y también por el alcance de la variable.
# Si se actualiza al final significa que puedo obtener la tienda
# sin problemas.
indTUsuario = -1
if tiendUsuario in sur:
	indTUsuario = sur.index(tiendUsuario)
elif tiendUsuario in centro:
	indTUsuario = centro.index(tiendUsuario) + s
elif tiendUsuario in norte:
	indTUsuario = norte.index(tiendUsuario) + s + c

if indTUsuario != -1:
	filaTUsuario = M[indTUsuario]
	# Obtengo los indices donde las ventas fueron mayores a 0
	# Puesto que sé que son los productos distintos que se vendieron.
	indProdDist = np.where(filaTUsuario > 0)
	# Creo una lista vacía que contendrá los productos distintos
	# vendidos
	prodDistintos = []

	for indice in indProdDist:
		# Pregunto si el índice es menor a la cantidad de columnas
		# que tiene futbol, puesto que existen dos regiones en ellas
		# las cuales son: fútbol y natación.
		if indice < f:
			prodDistintos.append(futbol[indice])
		elif indice < f + nat:
			prodDistintos.append(natacion[indice - f])

	print("Tienda: {}".format(tiendUsuario))
	print("Productos distintos vendidos: {}".format(len(prodDistintos)))
	print("Productos: {}".format(", ".join(prodDistintos)))

# Literal 6

# Necesito hacer slicing para todas las tiendas,
# pero considerando solo la categoría de natación
tiendasXNatacion = M[: , f: ]

# Sumo las ventas de productos de natación por tiendas.
sumTienNatacion = tiendasXNatacion.sum(axis=1)

# Solo me interesa saber las tiendas que tuvieron ventas
# en productos de natación/
tiendasConVentas = sumTienNatacion[sumTienNatacion > 0]

# Dado que es un arreglo de una sola dimensión,
# la tupla que devuelve shape tiene solo un elemento
# que representa el número de columnas de éste.
canTiendas = tiendasConVentas.shape[0]
tiendasTotales = s + c + n

porcentaje = (canTiendas / tiendasTotales) * 100
print("Porcentaje: {:.2f}".format(porcentaje))

# Literal 7
promedioFutbol = M[:, :f].mean()
print("Promedio de ventas de productos de fútbol: {:.2f}".format(promedioFutbol))