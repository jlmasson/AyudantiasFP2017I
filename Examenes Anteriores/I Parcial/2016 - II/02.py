import numpy as np

s = len(sur)
c = len(centro)
n = len(norte)

f = len(futbol)
nat = len(natacion)


# La genero de manera automática para hacer pruebas.
M = np.random.randint(1, 100, (s + c + n, f + nat))

# Literal 1
sumaProductos = M.sum(axis=0)
sumaFutbol = sumaProductos[ :f].sum()
sumaNatacion = sumaProductos[f: ].sum()

if sumaFutbol > sumaNatacion:
	print("Fútbol tiene más ventas: {:.2f}".format(sumaFutbol))
elif sumaFutbol < sumaNatacion:
	print("Natación tiene más ventas: {:.2f}".format(sumaNatacion))
else:
	print("Iguales: {:.2f}".format(sumaFutbol))

# Literal 2
sumaTiendas = M.sum(axis=1)
indTiendaMax = sumaTiendas.argmax()
montoTiendaMax = sumaTiendas[indTiendaMax]
tienda = ""
if indTiendaMax < s:
	tienda = sur[indTiendaMax]
elif indTiendaMax < s + c:
	tienda = centro[indTiendaMax - s]
elif indTiendaMax < s + c + n:
	tienda = norte[indTiendaMax - s - c]

print("{} con un monto de {:.2f}".format(tienda, montoTiendaMax))

# Literal 3
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
while tiendUsuario not in sur and tiendUsuario not in centro and tiendUsuario not in norte:
	print("Tienda no existente.")
	tiendUsuario = input("Ingrese tienda: ")
	tiendUsuario = tiendUsuario.strip()

indTUsuario = -1
if tiendUsuario in sur:
	indTUsuario = sur.index(tiendUsuario)
elif tiendUsuario in centro:
	indTUsuario = centro.index(tiendUsuario) + s
elif tiendUsuario in norte:
	indTUsuario = norte.index(tiendUsuario) + s + c

if indTUsuario != -1:
	filaTUsuario = M[indTUsuario]
	indProdDist = np.where(filaTUsuario > 0)
	prodDistintos = []
	for indice in indProdDist:
		if indice < f:
			prodDistintos.append(futbol[indice])
		elif indice < f + nat:
			prodDistintos.append(natacion[indice - f])

	print("Tienda: {}".format(tiendUsuario))
	print("Productos distintos vendidos: {}".format(len(prodDistintos)))
	print("Productos: {}".format(", ".join(prodDistintos)))

# Literal 6
tiendasXNatacion = M[: , f: ]
sumTienNatacion = tiendasXNatacion.sum(axis=1)
tiendasConVentas = sumTienNatacion[sumTienNatacion > 0]

canTiendas = tiendasConVentas.shape[0]
tiendasTotales = s + c + n

porcentaje = (canTiendas / tiendasTotales) * 100
print("Porcentaje: {:.2f}".format(porcentaje))

# Literal 7
promedioFutbol = M[:, :f].mean()
print("Promedio de ventas de productos de fútbol: {:.2f}".format(promedioFutbol))