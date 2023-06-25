from Usuario import *
from Ocupacion import *
class Empresa (Usuario):
    empresasCreadas = []
    def __init__ (self,nombre):
        Usuario.__init__ (self,nombre)
        self.__id = int(input("Ingrese su id: "))
        self.__telefono = int(input("Ingrese su telefono: "))
        self.__descripcion = input ("Ingrese una descripcion como empresa: ")
        self.__correo = input("Ingrese su correo: ")
        self.__tipo = input ("Ingrese de que tipo es su empresa: ")
        self.__direccion = input ("Ingrese la direccion de su empresa: ")
        Empresa.empresasCreadas.append (self)
        Ocupacion.ocupacionEmpresa
        
    
    def getNombre(self):
        return super().getNombre()
    
    def getDatosEmpresa (self):
        return f"""Sus datos como empresa {self.getNombre()} serian 
Nombre: {self.getNombre()} 
Id: {self.__id}
Telefono: {self.__telefono}
Descripcion: {self.__descripcion}
Correo: {self.__correo}
Tipo: {self.__tipo}
Direccion: {self.__direccion}"""
    
    def getEmpresasList (self):
        cont = 0
        for i in Empresa.empresasCreadas:
            cont = cont + 1 
            print (f"{cont}: {Empresa.getDatosEmpresa(i)}")