# El ejercicio 6 constara de un codigo que permita que un usuario pueda realizar una operacion basica ingresando
# los dos numeros que quiere operar y la consola le muestre el resultado

numero1 = int(input("Escriba el primero numero que desea operar: "))
numero2 = int(input("Escriba el segundo numero que desea operar: "))

while True:
    a = input("Escriba que operacion desea realizar: suma, resta, multiplicacion, division, potenciacion: ")

    if a == "suma":
        b = numero1 + numero2 
        print ("La suma entre", numero1 , "y", numero2 , "fue: ",b)
        break

    elif a == "resta":
        b = numero1 - numero2 
        print ("La resta entre", numero1 , "y", numero2 , "fue: ",b)
        break

    elif a == "multiplicacion":
        b = numero1 * numero2 
        print ("La multiplicacion entre", numero1 , "y", numero2 , "fue: ",b)
        break

    elif a == "division":
        b = numero1 / numero2 
        print ("La division entre", numero1 , "y", numero2 , "fue: ",b)
        break

    elif a == "potenciacion":
        b = numero1 ** numero2 
        print ("La potencia entre", numero1 , "y", numero2 , "fue: ",b)
        break
    else: 
        print("Usted ingreso el nombre de la operacion mal por favor vuelva e ingreselo")