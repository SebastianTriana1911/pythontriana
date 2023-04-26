# El ejercicio 9 constara de un codigo donde un usuario ingrese dos numeros por consola listandole todos los numeros
# desde el primero hasta el segundo diciendole cuales son par y cuales no 

numero1 = int(input("Escriba un numero entero: "))
numero2 = int(input(f"Escriba un numero mayor o igual a {numero1}: "))
resultado = 0

numero1 >= numero2

for i in range (numero1, numero2, 1):
            i = i + 1
            resultado = i % 2
            if resultado == 0:
             print (f"El numero {i} es par")      
            else:
                  print (f"El numero {i} es impar") 
                
numero1 < numero2
print (f"¡Le he pedido un número mayor o igual que {numero1} !")