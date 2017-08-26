numeroImpar = int(input("Número impar: "))

maximoPermitido = numeroImpar // 2

listaPrimos = []

for i in range(2, maximoPermitido + 1):

	c = 0

	for j in range(1, i):

		if i % j == 0:

			c += 1

	if c ==WW 1:

		listaPrimos.append(i)

print(listaPrimos)
