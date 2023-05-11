# Llenar un arreglo de n elementos con números generados con la función random. Cada número siguiente debe ser mayor que el
# anterior, pero no puede exceder el valor de la siguiente decena.
import random

lista = []
tam = random.randrange(8,15)
aux = 0
numero = 0
acum = 0
for i in range (tam):
    numero = random.randrange(5,50)
    print (f"El numero es {numero}")
    acum = numero
    acum = acum + 10
    print (f"acumulador {acum}")
    if acum <= acum:
        aux = numero
        print (aux)
        lista.append(numero)
print (lista)