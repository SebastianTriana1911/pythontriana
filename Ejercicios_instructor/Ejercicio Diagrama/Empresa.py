from Cliente import *

class Empresa(Cliente):
    def __init__(self,nombre,telefono,fax, precio):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__fax = fax
        self.__precio = precio
        
    def descuentoProducto (self,precio):
        self.__precio = precio
        precio = self.__precio * 0.35
        return f"El precio con descuento para una empresa es: {precio} "