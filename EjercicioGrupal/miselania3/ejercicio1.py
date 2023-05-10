# Llenar un arreglo de n elementos con numeros generados con la fncion random. N es ingresado por el usuario. Disene un menu con las siguientes 
# operaciones

import random
lista = []

# Agregar numeros aleatorios a una lista con una longitud aleatoria
def num_random (tam,numero):
    lista = []
    lista = [random.randrange (numero) for w in range (tam)]
    return lista 
lista = num_random(8,30)
print (lista)

# Hacer una suma con todos los elementos de la lista
def suma_lista (lista):
    suma = 0
    for q in lista:
        suma = suma + q
    return suma
print(suma_lista(lista))

# Hallar el promedio de la lista
def promedio_lista (lista):
    return suma_lista(lista) / len(lista)
print(promedio_lista(lista))

# Hallar el numero mayor de toda la lista
def mayor_lista (lista):
    mayor = 0
    for e in lista:
        if e > mayor:
            mayor = e
    return mayor
print (mayor_lista(lista))