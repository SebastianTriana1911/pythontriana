# Se crea una variable llamada i la cual se le asigna un valor de 1
i=1
# Se crea una variable llamada sum la cual se le asigna un valor de 0
sum=0
# Se crea un bucle while, cabe recalcar que los bucles while solo funcionan si la condicion que se le asigna es 
# verdadero "True" o simplemente se le coloca al lado del while el True y Python lo toma como que el bucle ya es
# verdadero, en el ejercicio podemos ver que al bucle while se le asigna una condicion la cual es que i <= 5 lo
# que quiere decir que si se cumple la condicion ya que 1 - 5 por consiguiente el bucle es verdadero y podra
# ejecutarse las siguientes lineas de codigo 
while i<=5:
    # Se le asigna la tarea de mostrar en pantalla el valor de i
    print(i)
    # Se asigna a la variable sum el resultado entre la suma del valor de la variable sum y la variable i
    sum=sum+i
    # Se asigna a la variable i la suma del valor de i + 1 
    i+=1 #i=i+1 
    # Se dice que muestre por pantalla cada uno de los numeros que sea sum y cuando llegue a ser igual a 
    # 5 pare el blucle y muestre la suma entre todos los numeros que se guardaron en la variable sum
print(f'la suma es ={sum}')