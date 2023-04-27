# El ejercicio 3 constara de un codigo que permita que un usuario ingrese un numero por consola y esta haga una
# lista de numeros desde el 1 hatas el numero que el usuario ingreso, diciendole si es multiplo de 2 o no lo es
# con el bucle while

i = 0
numero = int(input("Escriba un numero: "))

while i < numero:
    i += 1
    resultado = i % 2

    if resultado == 0:
        print("El numero", i , "si multiplo de 2")

    else:
        print("El numero", i , "no es multiplo de 2")