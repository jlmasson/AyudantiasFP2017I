import numpy as np

# Función que recibe una lista de multas, donde cada elemento es una tupla,
# mismo que tiene la estructura (coordX, coordY, multa), que permite acumular
# el valor correspondiente en cada celda de la matriz
def generarMatriz(listaMultas):
	multas = np.zeros((5, 5), int)
	for t in listaMultas:
		f, c, m = t
		multas[f, c] += m
	return multas

# Función que recibe una matriz con las multas asignadas en cada celda, y dada
# la distribución de ella explicada en el problema, se procederá a obtener
# la suma de las multas por cada sector y determinar cual es el que suma el mayor
# valor de multas
def sectorTop(matriz):
	# Diccionario que tendrá cuyos elementos par clave - valor, tendrá al sector
	# y el total de multas por cada sector, respectivamente.
	sectores = {}
	sectores["Norte"] = matriz[0].sum()
	sectores["Sur"] = matriz[-1].sum()
	sectores["Oeste"] = matriz[1: -1, 0].sum()
	sectores["Este"] = matriz[1: -1, -1].sum()
	sectores["Centro"] = matriz[1: -1, 1: -1].sum()
	# Utilizo la función sorted que retorna una lista, pasándole cualquier colección que sea
	# iterable como argumento, en este caso le paso los items de sectores, puesto que me conviene
	# ordenar por el valor, y al mismo tiempo mantener la clave.
	# Esta función recibe un parámetro que se llama key, misma que se conoce como la función de 
	# ordenamiento, en donde podemos especificarle como queremos que se ordene la colección.
	# Utilizo una función lambda (función anónima), para esto.
	# Estructura:
	# lambda parámetro : valor a retornar.
	# Defino el parámetro de la función lambda como sector, puesto que sector va a ser una tupla
	# donde el primer elemento representa a la clave (nombre del sector) y el segundo elemento, representa
	# el total acumulado por sector. Dado que me interesa ordenar por el total acumulado, por esa razón
	# retorno sector[1], y me interesa ordenar de mayor a menor, por lo tanto, le especifico que ordene
	# de mayor a menor.
	sectoresTop = sorted(sectores.items(), key=lambda sector : sector[1], reverse=True)
	return sectoresTop[0]

# Prueba de funciones
listaMultas = [(0, 0, 120), (1, 2, 330), (3, 4, 123), (4, 2, 62), (0, 0, 50),
 			   (4, 4, 89), (0, 3, 25), (2, 0, 43), (3, 2, 21), (0, 0, 120)]

multas = generarMatriz(listaMultas)
print("\nMatriz de multas:\n\n{}\n".format(multas))

tuplaSectorTop = sectorTop(multas)
print("Sector Top:\n\n{}\n".format(tuplaSectorTop))