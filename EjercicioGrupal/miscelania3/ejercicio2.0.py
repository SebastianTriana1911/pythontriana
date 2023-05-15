# Llenar dos arreglos de n elementos con números generados con la función random. Compararlos y decir:
import random

lista1 = []
lista2 = []
def llenarLista (lista):
    lista = []
    tam = random.randrange (5,15)
    for i in range (tam):
        numero = int (random.randrange(0,50))
        lista.append(numero)
    return lista

lista1 = llenarLista(lista1)
lista2 = llenarLista(lista2)
print (f"La lista1 es: {lista1}")
print (f"La lista2 es: {lista2}")

# Cuál de los dos tiene la suma más alta
def sumaLista (lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma
sumal1 = sumaLista(lista1)
sumal2 = sumaLista(lista2)
print (f"La suma de la lista1 es de: {sumaLista(lista1)}")
print (f"La suma de la lista2 es de: {sumaLista(lista2)}")

def sumaMayor ():
    if sumaLista(lista1) > sumaLista(lista2):
        return f"La suma mayor es la de la lista1 con la suma de: {sumaLista(lista1)}"
    else:
        return f"La suma mayor es la de la lista2 con la suma de: {sumaLista(lista2)}"
print (sumaMayor())

# Cuál de los dos tiene el número mayor
def mayorLista (lista):
    mayor = 0
    for e in lista:
        if e > mayor:
            mayor = e
    return mayor
print (f"El numero mayor de la lista1 es: {mayorLista(lista1)} ")
print (f"El numero mayor de la lista2 es: {mayorLista(lista2)} ")

def maxLista ():
    if mayorLista(lista1) > mayorLista(lista2):
        return f"La lista con numero mayor es la lista1 y su numero es: {mayorLista(lista1)}"
    elif mayorLista(lista1) < mayorLista(lista2):
        return f"La lista con numero mayor es la lista2 y su numero es: {mayorLista(lista2)}"
    else:
        return f"Las dos listas tienen el mismo numero mayor y es: {mayorLista(lista1)}"
print (maxLista())

# Cuál de los dos tiene el número menor
def menorLista (lista):
    menor = 10000
    for e in lista:
        if e < menor:
            menor = e
    return menor
print (f"El numero menor de la lista1 es: {menorLista(lista1)} ")
print (f"El numero menor de la lista2 es: {menorLista(lista2)} ")

def minLista ():
    if menorLista(lista1) > menorLista(lista2):
        return f"La lista con numero menor es la lista1 y su numero es: {menorLista(lista1)}"
    elif menorLista(lista1) < menorLista(lista2):
        return f"La lista con numero menor es la lista2 y su numero es: {menorLista(lista2)}"
    else:
        return f"Las dos listas tienen el mismo numero menor y es: {menorLista(lista1)}"
print (minLista())

# Cuál es el promedio conjunto (uniendo los dos arreglos)
def promedioConj ():
    sumaTotal = sumal1 + sumal2
    elementoTotal = len(lista1) + len(lista2)
    promConj = sumaTotal / elementoTotal
    return promConj
print (promedioConj())

