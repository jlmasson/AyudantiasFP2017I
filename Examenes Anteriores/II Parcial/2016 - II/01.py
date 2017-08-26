import numpy as np

def generarMatriz(listaMultas):
	multas = np.zeros((5, 5), int)
	for t in listaMultas:
		f, c, m = t
		multas[f, c] += m
	return multas

def sectorTop(matriz):
	sectores = {}
	sectores["Norte"] = matriz[0].sum()
	sectores["Sur"] = matriz[-1].sum()
	sectores["Oeste"] = matriz[1: -1, 0].sum()
	sectores["Este"] = matriz[1: -1, -1].sum()
	sectores["Centro"] = matriz[1: -1, 1: -1].sum()
	sectoresTop = sorted(sectores.items(), key=lambda sector : sector[1], reverse=True)
	return sectoresTop[0]