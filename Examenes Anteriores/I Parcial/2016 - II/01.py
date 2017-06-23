vocales = list("aeiou".upper())
consonantes = list("bcdfghjklmnpqrstvwxyz".upper())

cadena = input("Ingrese frase: ")
cadena = cadena.replace(".", " ").strip()

while len(cadena) == 0:
	cadena = input("Ingrese frase: ")
	cadena = cadena.replace(".", " ").strip()

cadena = cadena.upper()
cantidadPalabras = 0
palabras = cadena.split()

for palabra in palabras:
	cVocales = cConsonantes = 0
	if palabra.isalpha():
		for caracter in palabra:
			if caracter in vocales:
				cVocales += 1
			elif caracter in consonantes:
				cConsonantes += 1
		if cVocales == cConsonantes:
			cantidadPalabras += 1

print(cantidadPalabras)