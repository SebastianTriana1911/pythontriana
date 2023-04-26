# Cuando vamos a tulizar el ciclo for debemos asignarle una variable segido de in range luego de eso abriremos parentesis y si insertamos
# solo un argumento nos indicara el punto de partida del ciclo
for i in range(11):
    
    # La funcion if nos indica que si el residuo del numero que le corresponde a la variable "i" y el 3 es igual a 0  
    if i%3==0:
        
        # Debera imprimir en pantalla que el numero de la variable "i" es multiplo de 3
        print(f'{i} es multiplo de 3')
    
    else:
        # Si la variable i no es multiplo de 3 entonces debera solo imprimir el numero
        print(i)

# Cuando queremos iniciar desde un numero y terminar en otro numero ya preestablecido deberemos colocar dos valores separados por comas entre
# los parentecis de range, como el primer valor ya sabemos que es el numero en el que queremos que comience el ciclo, el segundo nos dire el
# numero en el que queremos que termine
for j in range(1,11):
    
    # Nos mostrara por consola todos los numeros desde el 1 hasta el 11 en este caso
    print(j)

# Ahora si queremos colocar una cantidad preestablecida de valoren en el que vaya aumentar el contador lo asignamos en el 3 valor, esto quiere
# decir que el primer valor significa el comienzo del contador el segundo valor significa en que numero va a terminar el contador, y el tercer
# valor significa la cantidad de numeros que va aumentar para mostrar el siguiente numero
for k in range(0,11,2):
    
    # Nos mostrara por consola un contador desde 1 aumentando de 2 en 2 hasta 11
    print(k)

# Cuando el tercer valor es negativo quiere decir que el contador va en reversa para lograr esto el primer valor osea el valor de partida
# tiene que ser mayor al valor que indica el final, si esto no es asi no se ejecutara el codigo
for i in range(20,0,-2):
    print(i)