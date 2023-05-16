# Tamaño lista (por pueblo): minimo 200 maximo 2500.{validación}
# Llenar Icfes {Resultados. 100 - 500}
# Hallar valor de cada cuartil
# Hallar valor de cada quintil
# Promedio por cada cuartil
# Promedio por cada quintil
# Mayor y menor por separado de cada cuartil y quintil respectivamente
# Generar listas separadas por cuartil y quintil

import random 
lista2 = [1,2,3,4,5,6,7,8,9,10,11,12]
lista1 = []
tam = random.randrange(10,30)
cuartil = []

# def llenarLista (lista):
    # lista = [random.randrange(100,500) for i in range (tam)]
    # return lista
# print (llenarLista(lista1))
# lista1 = llenarLista(lista1)

# def ordenarLista (lista):
    # for i in range(tam):
        # for j in range(i+1,tam):
            # if lista[i] > lista[j]:
                # aux=lista[i]
                # lista[i]=lista[j]
                # lista[j]=aux
    # return lista
# print (ordenarLista(lista1))

for i in range (1,4):
    if len(lista2) % 2 != 0:
        cuartil1 = i * (len(lista2) + 1) / 4
        cuartil.append(cuartil1)
print (cuartil)

for i in range (1,4):
    if len(lista2) % 2 == 0: 
        cuartil1 = i * (len(lista2) - 1) // 4
        cuartil2 = lista2[cuartil1]
        cuartil3 = lista2[cuartil1 + 1]
        cuartil1 = cuartil2 + cuartil3
        cuartil1 = cuartil1 / 2
        cuartil.append(cuartil)
print (cuartil)
 
