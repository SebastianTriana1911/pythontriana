# Calcular el máximo de números positivos introducidos por teclado, sabiendo que metemos números hasta 
# que introduzcamos uno negativo. El negativo no cuenta.
num = int(input("Ingrese un numero: "))
cont = 0
while num > 0:
    if num > 0:
        cont = cont + 1
    num = int(input("Ingrese un numero: "))
print (f"La cantidad de numeros introduciodos es de {cont}")
