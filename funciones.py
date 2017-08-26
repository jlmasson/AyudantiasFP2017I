# Para las funciones existen dos conceptos elementales los cuales son:
# Paso de parámetro por valor y paso de parámetro por referencia.

# Cuando se trata de paso de parámetros por valor; en la función, estos valores
# se copian dentro de ella, por lo cual el valor original
# no se ve alterado dentro de los procesos que se realizan en la función.
# Esto aplica para tipos de datos primitivos como lo son los números enteros y flotantes.

# Cuando se trata de paso de parámetros por referencia, en la función, se pasa directamente
# la dirección de memoria del dato con la cual se está trabajando, por ende, si se realizan cambios
# dentro de la función, la referencia también será afectada.
# Esto aplica para tipos de datos como:
# Colecciones:
# 	- Listas
# 	- Tuplas
# 	- Sets (Conjuntos)
# 	- Diccionarios
# Cadenas de caracteres (Strings)
# Arreglos de NumPy
# Objetos

# Para tenerlo claro se lo realizará con dos ejemplos:

def sumar(a, b):
	b += 1
	return a + b

def anadirElemento(lista, elemento):
	lista.append(elemento)

a = 4
b = 5
c = sumar(a, b)

print(a, b, c)

# En el primer ejemplo, se puede apreciar el paso de parámetros por valor, al momento
# de invocarla, se le pasa como argumentos, las variables a y b. Dentro de la función
# sumar el valor del parámetro b se incrementa en 1, pero este incremento ocurre en la copia,
# mas no en el valor original, por ende, la suma retorna 10.
# Lo que se muestra por pantalla es 4 5 10.

L = [3, 5, 6]
a = 10

anadirElemento(L, a)
print(L)

L[-1] = 15

print(a, L)

# En este ejemplo, se puede apreciar al mismo tiempo los dos casos mostrados:
# En el primer parámetro se cumple el paso de parámetro por referencia (dado que voy a trabajar
# con una lista, y esto se trata como referencia), y el segundo parámetro (dependiendo del tipo de dato)
# se trabajará como paso de parámetro por valor, o por referencia.
# Para este caso, trabajará como paso de parámetro por valor, puesto que se está trabajando con un
# dato primitivo.

# Como se puede apreciar, la lista se verá afectada, y su último valor será 10. -> L = [3, 5, 6, 10]
# Luego se cambia su último valor, quedando asi -> L = [3, 5, 6, 15]
# Sin embargo, el valor de la variable a se ve inalterado, puesto que al ser un dato de tipo primitivo,
# se trabajó con su copia dentro de la función.

b = [3, 5, 6]

anadirElemento(L, b)
print(L)

b[-1] = 40

print(L)
print(b)

# En este otro ejemplo, se están pasando los dos parámetros por referencia, por ende, la lista L
# quedará de la siguiente manera -> L = [3, 5, 6, 15, [3, 5, 6]]
# Luego se modifica un valor de la lista b, dado que se trabajó con referencias, también esto se
# modifica en la lista L, por ende -> L = [3, 5, 6, 15, [3, 5, 40]] y b = [3, 5, 40]