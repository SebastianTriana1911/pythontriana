# Llenar una lista con numeros aleatorios (reales con un decimal) y que representen calificaciones de un curso, se evaluan de 0 a 5.
# El curso puede tener entre 20 y 30 aprendices. 
# HALLAR
# 1. Genere listas nuevas para los aprobados y los reprobados (se aprueba con 3)
# 2. Genere listas nuevas por cada unidad. Es decir, los que sacan de 0 a 1 son un grupo, los de 1 a 2 otro grupo y asi sucesivamente 
# 3. Diga cual es el promedio de los que aprueban y los que reprueban por separados

import random


aprendices = random.randint(20,30)
print (aprendices)

lista = [round (random.random () * 5,1 ) for i in range (aprendices)]
print (lista)

for q in range (aprendices):
    for w in range (q+1,aprendices):
        if lista[q] > lista[w]:
            aux = lista[q]
            lista[q] = lista[w]
            lista[w] = aux
print (lista)

lista2 = ["Aprobo" if x >= 3.0 else "Reprobo" for x in lista ]
print (lista2)

# for q in range (aprendices):
#     for w in range (q+1,aprendices):
#         if lista[q] > lista[w]:
#             aux = lista[q]
#             lista[q] = lista[w]
#             lista[w] = aux
# print (lista)







# grupo1 = [a for a in lista if a <= 1.0]
# print (f"Grupo 1 {grupo1}")
# grupo2 = []
# grupo3 = []
# grupo4 = []
# grupo5 = []