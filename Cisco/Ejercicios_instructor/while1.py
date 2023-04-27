num=1
cont=0
sum=0
while num!=0:
    
    num=int(input('ingrese numero'))
    cont=cont+1
    
    sum=sum+num

print(f"fueron ingresados {cont-1} numeros")
print(f"La suma de los numeros ingresados da un total de: {sum}")
print(f"El promedio de los numeros ingrsados es {sum//(sum-1)}")

if num != 0:
    print
