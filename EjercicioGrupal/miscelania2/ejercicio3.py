import random
lista1 = []
lista2 = []
suma1 = 0
suma2 = 0
mayor1 = 0
mayor2 = 0
menor1 = 10000
menor2 = 10000
#
for i in range(8):
    num1 = random.randint(0,10)
    lista1.append(num1)
print (lista1)

for n in range(8):
    num2 = random.randint(0,10)
    lista2.append(num2)
print (lista2)
#
#
for s in lista1:
    suma1 = suma1 + s
    promedio1 = suma1 / 8
    
for e in lista1:
    suma2 = suma2 + e
    promedio2 = suma2 / 8
    
if suma1 > suma2:
    print (f"La suma mayor es la de la lista1 y la suma de sus elementos es: {suma1}")
else:
    print (f"La suma mayor es la de la lista2 y la suma de sus elementos es: {suma2}")
#
for a in lista1:
    if a > mayor1:
        mayor1 = a
    if a < menor1:
        menor1 = a
print (f"El numero mayor de la lista1 es: {mayor1}")
print (f"El numero menor de la lista1 es: {menor1}")

for b in lista2:
    if b > mayor2:
        mayor2 = b
    if b < menor2:
        menor2 = b
print (f"El numero mayor de la lista2 es: {mayor2}")
print (f"El numero menor de la lista2 es: {menor2}")

if mayor1 > mayor2:
    print(f"El numero mayor entre las dos listas es: {mayor1}")
elif mayor1 < mayor2:
    print(f"El numero mayor entre las dos listas es: {mayor2}")
else:
    print(f"Ambos numeros son iguales")

if menor1 > menor2:
    print(f"El numero menor entre las dos listas es: {menor2}")
elif menor1 < menor2:
    print(f"El numero menor entre las dos listas es: {menor1}")
else:
    print(f"Ambos numeros son iguales")
    
print (promedio1, promedio2)
promedio_conj = (promedio1 + promedio2) / 2
print (f"El promedio entre las dos listas es: {promedio_conj}")




