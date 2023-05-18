# Tamaño lista (por pueblo): minimo 200 maximo 2500.{validación}
# Llenar Icfes {Resultados. 100 - 500}
import random
listaOrig = []
def llenarLista (lista):
    tam = random.randrange(6,13)
    lista = [random.randrange(10,50) for i in range (tam)]
    return lista
listaOrig = llenarLista(listaOrig)
print (f"Los valores de la lista son: {listaOrig}")

# Hallar valor de cada cuartil
def organizar_lista(lista):
    for i in range (len(lista)):
        for a in range (i + 1, len(lista)):
            if lista[i] > lista[a]:
                aux = lista[a]
                lista[a] = lista[i]
                lista[i] = aux
    return lista
listaOrig = organizar_lista(listaOrig)
print (f"La lista organizada de manera ascendente {listaOrig}")

Q1 = []
Q2 = []
Q3 = []
for i in range (1, 4):
    posicion = i * (((len(listaOrig) + 1) / 4))
    print(f"El Q{i} esta en la posicion {posicion}")
    redondeo = round(posicion)
    if posicion > redondeo:
        resultado = (listaOrig[redondeo] + listaOrig[redondeo -1]) / 2
        print (f"El valor del Q{i} es: {resultado}")
    elif posicion < redondeo:
        redondeo = redondeo - 1
        resultado = (listaOrig[redondeo -1] + listaOrig[redondeo]) / 2
        print (f"El valor del Q{i} es: {resultado}")
    elif posicion == redondeo:
        resultado = listaOrig[redondeo -1]
        print (f"El valor del Q{i} es: {resultado}")
    # if i == 1:
    #     Q1.append(resultado)
    #     resultQ1 = Q1[0]
    #     print (Q1)
    # if i == 2:
    #     Q2.append(resultado)
    #     print (Q2)
    # if i == 3:
    #     Q3.append(resultado)
    #     print (Q3)

# Hallar valor de cada quintil
# Funcion que retorne el valor y la posicion dada la lista y el numero de cuartil y quintil
# Promedio por cada cuartil 
# Promedio por cada quintil
# Mayor y menor por separado de cada cuartil y quintil respectivamente
# Generar listas separadas por cuartil y quintil
