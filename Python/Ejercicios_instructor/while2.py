# Se crean dos variables donde se le asignan dos valores a cada una
x,y=3,5
# Se crea una variable con un valor a 1
cont=1
# Se crea un bucle while y hasta que sea verdadera iniciara como los argumentos insertados al lado del while no son verdaderos no iniciara 
# el bucle por esa razon es que se encierran en parentecis y al lado izquierdo se le asigna la funcion not que esta lo que quiere decir es
# que invierte el False de los argumentos encerrados a un True 
while not(x%y==0 or y%x==0):
    
    print(f'intento numero {cont}')
    x=int(input('ingrese numero'))
    y=int(input('ingrese numero'))
    cont+=1

print(f'{x} y {y} son factor')