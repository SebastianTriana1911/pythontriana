# Hacer un codigo que tenga una lista de tamaño del 10 al 20 gnerando numeros aleatorios del 0 al 100 y con esos numeros sacar la suma de todos los 
# elementos de la lista, el promedio, el mayor, el menor, la mediana, la moda y la deviacion estandar 

import random 
lista = []
suma = 0
promedio = 0
mayor = 0
menor = 100000
tam = random.randint(10,20)
print(tam)

for i in range (tam):
    num = random.randrange(100)
    lista.append (num)
    suma = suma + num
promedio = suma // tam

print (f"{lista}")
print (f"La suma de todos los numeros es {suma}")
print (f"El promedio de la lista es {promedio}")

for n in lista:
    if n > mayor:
        mayor = n 
    if n < menor:
        menor = n
print (f"El numero mayor es {mayor}")
print (f"El numero menor es {menor}")

for lista in range (mayor,menor,-1):
    print (lista)