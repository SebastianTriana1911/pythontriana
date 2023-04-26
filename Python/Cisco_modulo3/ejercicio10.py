# El ejercicio 10 constara de un codigo donde el usuario pueda ingresar una palabra y pueda ingresar el numero de 
# veces que quiera que esta se visualize en la consola 

palabra = input("Escriba una palabra: ")
veces = int(input("Escriba el numero de veces que desea ver la palabra "))

for i in range(veces):
    i = i + 1
    print(palabra)