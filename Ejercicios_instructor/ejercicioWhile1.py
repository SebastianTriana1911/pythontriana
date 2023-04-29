# Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste 
# exactamente sí (en minúsculas y con tilde).

val2 = input("Desea continuar con el programa: ")

while val2 == "si":
    val2 = input("Desea continuar con el programa: ")
    break


print("Termino el programa: ")
    
