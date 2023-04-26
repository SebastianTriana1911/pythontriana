# El ejercicio 8 constara de un codigo que permita que un usuario ingrese un numero y la consola le 
# muestre los numeros del 1 al 10 multiplicados por el numero que ingreso

numero = int(input("Escriba el numero que va hacer el multiplicador: ")) 
resultado = 0

for i in range (0,10,1):
    i = i + 1
    resultado = i * numero
    
    print(f"{numero} x {i} = {resultado}")