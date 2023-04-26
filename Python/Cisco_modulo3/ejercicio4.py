# El ejercicio 4 constara de un codigo que permita que un usuario ingrese una contraseña por consola luego de haber
# echo esto, tendra que validarla nuevamente, si la contraseña no es valida tendra que volver a ingresarla hasta que 
# coinsida con la que ingreso la primera vez, esto se conseguira con el bucle whiley break 

contraseña1 = (input("Escriba una contraseña: "))

while True :

    contraseña2 = input("Escriba su contraseña nuevamente: ")

    if contraseña1 == contraseña2:
        print("Su autenticacion fue todo un exito")
        break

    else: 
        print ("Vuelva a ingresar su contraseña")
        
        