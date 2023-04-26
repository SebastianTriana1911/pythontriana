# El ejercicio 1 consta de un codigo que haga un bucle del 1 al 10 y haga la suma de todos los numeros pares y por
# aparte la suma de todos los numeros impares 

i = 0
sumpar = 0
sumimp = 0

for i in range (0,5,):
    sumpar = sumpar + i
    i = i + 1
    resultado = sumpar % 2
    if resultado == 0:
        print(f"La suma de los numeros pares es: {sumpar}")

    else:
        sumimp = sumimp + 1
        print(f"La suma de los numeros impares es: {sumimp}")