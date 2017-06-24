# Lista de vocales, consonantes y vocales tildadas

vocales = list("aeiou".upper())
consonantes = list("bcdfghjklmnpqrstvwxyz".upper())
vocalesTildes = list('ÁÉÍÓÚ')

# Ingreso de frase y limpieza de espacios
cadena = input("Ingrese frase: ")
cadena = cadena.strip()

# Valido que no ingrese cadenas vacías
while len(cadena) == 0:
	print("Cadena no válida.")
	cadena = input("Ingrese frase: ")
	cadena = cadena.strip()

# Reemplazo los puntos por espacios para realizar
# un solo split
cadena = cadena.replace(".", " ")

# Trabajaré todo con mayúscula
cadena = cadena.upper()

# Reemplazo vocales tildadas, por las vocales sin tilde
for i, vocalTildada in enumerate(vocalesTildes):
	vocalNoTildada = vocales[i]
	cadena = cadena.replace(vocalTildada, vocalNoTildada)

# Variable contadora de las palabras
# cuya cantidad de vocales sea la misma
# que la cantidad de consonantes.
cantidadPalabras = 0
palabras = cadena.split()

for palabra in palabras:
	palabra = palabra.strip()

	# Si la cadena solo contiene caracteres
	# alfabéticos se procede a contar
	# la cantidad de consonantes y vocales respectivamente
	if palabra.isalpha():
		cVocales = cConsonantes = 0
		for caracter in palabra:
			if caracter in vocales:
				cVocales += 1
			elif caracter in consonantes:
				cConsonantes += 1
		if cVocales == cConsonantes:
			cantidadPalabras += 1
			
print(cantidadPalabras)