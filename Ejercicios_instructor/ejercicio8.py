# Hacer un codigo que tenga una lista de tamaño del 10 al 20 generando numeros aleatorios del 0 al 100 y con esos numeros sacar la suma de todos los 
# elementos de la lista, el promedio, el mayor, el menor, la mediana, la moda y la deviacion estandar 

import random 
lista = []
suma = 0
promedio = 0
mayor = 0
menor = 100000
posicion = 0
# Arrojar un numero random 
tam = random.randint(10,20)
print(f"El tamaño de la lista va a ser de: {tam}")
# Hayar la suma de todos los numeros de la lista y hayar su promedio
for i in range (tam):
    num = random.randrange(100)
    lista.append (num)
    suma = suma + num
promedio = suma // tam

print (f"{lista}")
print (f"La suma de todos los numeros es: {suma}")
print (f"El promedio de la lista es: {promedio}")
# Hayar el numero mayor y el menor de la lista 
for a in lista:
    if a > mayor:
        mayor = a 
    if a < menor:
        menor = a
print (f"El numero mayor es: {mayor}")
print (f"El numero menor es: {menor}")
# Ordenar la lista de menor a mayor
lista.sort()
print (lista)
# Hayar la mediana de la lista 
if tam % 2 == 0:
    posicion = (tam - 1) // 2
    posicion2 = (lista [posicion])
    posicion3 = (lista[posicion + 1])
    posicion = posicion2 + posicion3
    posicion = posicion / 2
    print (f"La mediana de la lista es {posicion}")
elif tam % 2 != 0:
    posicion = (tam + 1) // 2
    print (f"La mediana de la lista es: {lista[posicion -1]}")

# for k in lista:
#     while k 
#     k1 = k
#     if k1 == k:
#         k2 = k2 + 1
#         print (f"La moda es {k1}")

# else:
#     continue
