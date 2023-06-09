from Cliente import *
class Individual(Cliente):
    def __init__(self,nombre,apellido,email,telefono,direccion, precio):
        super 
        self.__nombre = nombre 
        self.__apellido = apellido
        self.__email = email
        self.__telefono = telefono
        self.__direccion = direccion
        self.__precio= precio
        
    def descuentoProducto (self,precio):
        self.__precio = precio
        precio = self.__precio * 0.35
        return f"El precio con descuento para un individual es: {precio} "