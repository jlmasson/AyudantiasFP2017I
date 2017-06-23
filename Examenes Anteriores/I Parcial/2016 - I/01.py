lista = ["www.espol.edu.ec",
"www.google.com",
"www.sri.gob.ec",
"www.fiec.espol.edu.ec",
"www.uess.edu.ec",
"www.FIEC.espol.edu.ec",
"www.fict.espol.edu.ec",
"www.fcnm.Espol.edu.ec",
"www.ucsg.edu.ec",
"www.Stanford.edu",
"www.harvard.edu",
"www.stanford.edu",
"www.UCSG.edu.ec",
"www.google.com.ec",
"www.facebook.com",
"www.opensource.org",
"www.educacionbc.edu.mx"]


# Lista que contendrá todas las universidades
universidades = []

# Lista que contendrá universidades del ecuador
ecuador = []

# Lista que contendrá los sitios web de las universidades
sitiosWeb = []

# Educación
tipoDom = 'edu'

# Algoritmo para los dos primeros literales
# Recorro cada sitio de la lista
for sitio in lista:

  # Todo se trabajará con minúscula.
  sitio = sitio.lower().strip()
	componentes = sitio.split('.')

  # Pregunto si 'edu' forma parte de los componentes
  # del nombre del sitio web
	if tipoDom in componentes:
    # De ser verdad, obtengo el índice.
    # Se sabe que el nombre de la institucíón se encuentra
    # a la izquierda de 'edu', por ende se resta 1 al índice.
    # El sistema de referencia es donde se encuentra ubicado 'edu'
		indEdu = componentes.index(tipoDom)
		nombreUniversidad = componentes[indEdu - 1].strip()

    # Debo asegurar unicidad, por ende debo preguntar si el
    # sitio no se encuentra para agregarlo por vez única
		if nombreUniversidad not in universidades:
			universidades.append(nombreUniversidad)

      # Así mismo obtengo el sitio web de la misma.
			sitioUniversidad = ".".join(componentes[indEdu - 1: ])
			sitiosWeb.append(sitioUniversidad)

      # Aprovechando la unicidad, se pregunta si este sitio
      # es de Ecuador
			if 'ec' in componentes:
				ecuador.append(nombreUniversidad)

# Literal a
print('En la lista aparecen {} universidades'.format(len(universidades)))
for i, univ in enumerate(universidades):
	print("\t{}) {}".format(i + 1, univ.upper()))

# Literal b
print('\nEn la lista aparecen {} universidades de Ecuador'.format(len(ecuador)))
for i, univ in enumerate(ecuador):
  print("\t{}) {}".format(i + 1, univ.upper()))

# Literal c
usuario = input("Ingrese el usuario: ")
usuario = usuario.strip()

# Se valida que el usuario no ingrese una cadena vacía.
while len(usuario) == 0:
  print("Nombre de usuario no válido.")
  usuario = input("Ingrese el usuario: ")
  usuario = usuario.strip()

siglaUniversidad = input("Ingrese el nombre/sigla de la universidad: ")
siglaUniversidad = siglaUniversidad.lower().strip()

# Se valida el nombre de la universidad
while siglaUniversidad not in universidades:
  print("Nombre de universidad no válido.")
  siglaUniversidad = input("Ingrese el nombre/sigla de la universidad: ")
  siglaUniversidad = siglaUniversidad.lower().strip()

# Una vez validado la universidad se procede a obtener su índice correspondiente
# en la lista de universidades, para obtener el sitio web correspondiente
indUni = universidades.index(siglaUniversidad)
sitioUni = sitiosWeb[indUni]

# Se arma el correo electrónico del usuario
correo = usuario + "@" + sitioUni

print("El correo electrónico del usuario es:", correo)