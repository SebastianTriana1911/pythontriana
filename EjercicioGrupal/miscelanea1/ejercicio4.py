# Determine cuales y cuantos numeros perfectos hay entre 1 y 100

result = 0 
cont = 0
perfect = 0
cont1 = 0
num = 1
for j in range (1,10):
    print (f"j{j}")
    for i in range (1,j):
        print (f"i {i}")
        result = j % i
    
        if result == 0:
            perfect = perfect + i

    if perfect == num:
        print (f"El numero {num} es perfecto")
    
    else:
        print (f"El numero {num} no es perfecto") 