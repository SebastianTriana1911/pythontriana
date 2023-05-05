# Determine cuales y cuantos numeros perfectos hay entre 1 y 1000

num1 = 1
num2 = 1000
result = 0 
cont = 0
perfect = 0
cont1 = 0
num = 1
for j in range (1,1000):
    for i in range (1,num):
      result = num % i
    
    if result == 0:
        cont = cont + 1
        
        perfect = perfect + i
        
if perfect == num:
    print (f"El numero {num} es perfecto")
    
else:
    print (f"El numero {num} no es perfecto")
