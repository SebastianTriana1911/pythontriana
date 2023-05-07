lista = []
numero_final = int(input("Ingrese en numero que indique el final de la lista: "))
num1 = 0
num2 = 1
for i in range (numero_final):
    result = num1 + num2
    num1 = num2
    num2 = result
    lista.append(result)
print (lista)

