# Literal a
def buscar(listaAnidada, valor):
	# Recorro cada fila de la lista anidada
	for fila in listaAnidada:
		# Recorro cada celda de la fila
		for celda in fila:
			# Si el valor de la celda es el mismo
			# al valor que se pasa como parámetro se retorna
			# True indicando que sí existe.
			if celda == valor:
				return True
			# Nótese que no se usa un else, por la sencilla razón
			# que no es necesario, puesto que se tiene el siguiente
			# ejemplo.
			# Supongamos que L = [[2, 3], [1]]
			# Y que valor = 1
			# Si se desea saber si ese valor, la función debe retornar
			# True que es lo que se espera, pero si se usara un else
			# retornaría False en la primera iteración, lo cual no es
			# verdad, puesto que debe retornar False cuando haya recorrido
			# toda la lista y nunca lo haya encontrado.
			# Por esa razón es que no se utiliza la estructura de control
			# else
	return False

# Literal b
L = [[3, 2, 5], [1], [7, 9]]
X = int(input("Ingrese valor por teclado: "))

# Uso de la función buscar
if buscar(L, X):
	print("Valor sí existe")
else:
	print("Valor no existe")

# Literal c
def operarLista(listaAnidada, operacion="sumar"):
	resultado = 0
	if operacion == "multiplicar":
		resultado = 1
	for fila in listaAnidada:
		for celda in fila:
			if operacion == "sumar":
				resultado += celda
			elif operacion == "multiplicar":
				resultado *= celda
	return resultado