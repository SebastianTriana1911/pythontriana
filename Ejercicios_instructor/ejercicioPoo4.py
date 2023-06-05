class Empleador:
    def __init__(self,nombre,cargo,salario):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario = salario
        
    def getNombre (self):
        return f"{self.__nombre},{self.__cargo},{self.__salario}"
    
    def getCargo (self):
        return f"{self.__cargo}"
    
    def getSalario (self):
        return f"{self.__salario}"
    
    def calculoHoras (self):
        a = self.__salario // 30
        resultado = a // 8
        return f"El salario que se gana por hora es: {resultado}"
    
    def recibeIncrement (self):
        ipc = 13.12
        if self.__salario <= 1160000:
            self.__salario = self.__salario // (ipc + 3)