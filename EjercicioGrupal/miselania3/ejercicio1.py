# Llenar un arreglo de n elementos con numeros generados con la fncion random. N es ingresado por el usuario. Disene un menu con las siguientes 
# operaciones

import random


# Agregar numeros aleatorios a una lista con una longitud aleatoria
def num_random (tam,numero):
    lista = []
    lista = [random.randrange (numero) for w in range (tam)]
    return lista 
lista2 = num_random(8,30)
print (lista2)

# Hacer una suma con todos los elementos de la lista
def suma_lista (lista):
    suma = 0
    for q in lista:
        suma = suma + q
    return suma
print(f"La suma de todos los elementos es: {suma_lista(lista2)}")

# Hallar el promedio de la lista
def promedio_lista (lista):
    return suma_lista(lista) / len(lista)
print(f"El promedio de la lista es: {promedio_lista(lista2)}")

# Hallar el numero mayor de toda la lista
def mayor_lista (lista):
    mayor = 0
    for e in lista:
        if e > mayor:
            mayor = e
    return mayor
print (f"El numero mayor de la lista es: {mayor_lista(lista2)}")

# Hallar el numero menor de toda la lista 
def menor_lista (lista):
    menor = 10000
    for r in lista:
        if r < menor:
            menor = r
    return menor
print (f"El numero menor de la lista es: {menor_lista(lista2)}")

# Organizar la lista de menor a mayor 
def asendente (lista):
    for t in range (len(lista)):
        for y in range (t+1, len(lista)):
            if lista[t] > lista[y]:
                aux = lista[y]
                lista[y] = lista[t]
                lista[t] = aux
    return lista
print (f"La lista de menor a mayor: {asendente(lista2)}")

# Organizar la lista de mayor a menor 
def desendente (lista):
    for t in range (len(lista)):
        for y in range (t+1, len(lista)):
            if lista[t] < lista[y]:
                aux = lista[y]
                lista[y] = lista[t]
                lista[t] = aux
    return lista
print (f"La lista de mayor a menor: {desendente(lista2)}")

# Hallar la moda de la lista
def moda_lista (lista):
    maximo = 0
    moda = 0
    for num1 in lista:
        cont = 0
        for num2 in lista:
            if num1 == num2:
                cont = cont + 1
        if cont > maximo:
            maximo = cont
            moda = num1
    if cont == maximo:
        return "no hay moda"
    return f"La moda de la lista es: {moda}"
print(moda_lista(lista2))
