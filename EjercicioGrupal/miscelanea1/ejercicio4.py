# Determine cuales y cuantos numeros perfectos hay entre 1 y 1000
perf = 0
cont = 0
for i in range (1,1000):
    perf = 0
    for a in range (1,i):
        resultado = i % a 
        if resultado == 0:
            perf = perf + a

    if perf == i:
        cont = cont + 1
        print (f"El numero {i} es perfecto")
        
print(f"Hay una cantidad de {cont} numeros perfectos")
    