from Usuario import *
from Empresa import *
from Ubicacion import *
from Ocupacion import *
from Vacante import *

print ("""Seleccione segun el numero\n
1. Persona
2. Empresa
""")

usuario = input("Que tipo de usuario es: ")
match usuario:
    case "1":
        print ("persona")
    case  "2":
            print ("""\nOpciones que puede hacer como empresa:
1. Crear una empresa
""")
opcion = input ("Que opcion desea realizar: ")

if opcion == "1":
    nomEmpresa = input("Como se llama su empresa: ")
    empresa = Empresa(nomEmpresa)
    print ("¡¡Empresa creada con exito!!")
else: 
    print ("Asegurese que lo que ingrese sea un numero que este en el menu")

print ("""\nEstas son las opciones que puede hacer ya creo una empresa: 
1. Ver datos de su empresa
2. Ingresar Ocupacion
3. Ingresar Ubicacion
""")
opcion = input("Que opcion desea realizar: ")

if opcion == "1":
    print(empresa.getDatosEmpresa())

if opcion == "2":
    ocup = Ocupacion ()
    empresa = Ocupacion(ocup)
