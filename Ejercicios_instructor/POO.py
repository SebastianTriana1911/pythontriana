# class persona:
#     def __init__(self,nombre,año):
#         self.nombre = nombre 
#         self.año = año
#     def descripcion (self):
#         return "{} tiene {} años ".format(self.nombre,self.año)
    
#     def comentario(self,frase):
#         return "{} dice {} ". format (self.nombre,frase)

# yo = persona("sebas", 18)
# print (yo.descripcion())
# print (yo.comentario("hola"))

class Ben10:
    pass
    def __init__ (self,nombre):
        self.nombre = nombre

class alien (Ben10):
    def descrip (self):
        return "{} es un alien".format (self.nombre)
    
class tip (Ben10):
    def tipo_alien (self,tipo):
        return "{} es un alien de tipo: {}".format (self.nombre,tipo)
    
Ben = tip ("Cuatro brasos")
print (Ben.tipo_alien("Tierra"))
