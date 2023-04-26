# El ejercicio 7 constara de un codigo que permita que un usuario pueda insertar un numero positivo
# por consola y esta le mostrara la secuencia de ese numero hasta 0

numero = int(input("Escriba un numero que sea positivo: "))

for i in range(numero,0,-1):
    numero = i - 1
    print(numero)