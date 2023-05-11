# Llenar un arreglo de n elementos con números generados con la función random. No puede haber números repetidos. 
# Si intenta ingresar al arreglo un número que ya existe, imprimirlo para anunciar que ese número ya está en el 
# arreglo.
import random

lista1 = []

#def arreglo (lista):
tam = random.randrange (5,20) 
lista1 = [random.randrange (0,20) for i in (tam)]
print (lista1)

