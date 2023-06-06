lista = []
def llenarList (lista,tam,num):
    import random
    lista = [random.randrange(num) for i in range (tam)]
    return lista

def sumar_elementos(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

def obtener_elemento_mayor(lista):
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor

def obtener_elemento_menor(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return menor

def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

def invertir_lista(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

lista = llenarList(lista,10,10)
print (lista)
print (sumar_elementos(lista))