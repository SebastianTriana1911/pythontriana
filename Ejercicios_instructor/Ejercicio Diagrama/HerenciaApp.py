from Cliente import *
from Productos import *
from Individual import *

persona = Cliente(10,"Normal","individual","hola")
persona2 = Cliente(20,"Normal","empresa","hola")
persona3 = Individual (20,"persona3","Indi","hola","sebas@gmail.com", 313802, "xra2" )
print (persona.getDatos())
print (persona.setId(11))
print (persona.getDatos())

ob1 = Producto(1,"Arroz","Grano","Grasas",1000)
ob2 = Producto(2,"Lenteja","Grano","Engorda",2000)
print(ob1.getProducto())
print(ob2.getProducto())

persona.agregarProducto(ob1)
persona.agregarProducto(ob2)

for producto in persona.getProductos():
    print (f"AGREGACION {producto.getProducto()}")

persona2.componerProducto(2,"Arroz","Grano","Grasas",2000)
persona2.componerProducto(3,"Arroz","Grano","Grasas",2000)
for producto in persona2.getProductos():
    print (f"COMPOSICION {producto.getProducto()}")


print(persona3.getDatos())
print(isinstance(persona3,Individual))
producto = Producto (4, "Agua", "Bebida", "Lite", 1500)
persona3.agregarProducto(producto)
for i in persona3.getProductosList():
    print (f"Instanciado de Individual {i.getProducto()}")

print(persona3.descuentoProducto(1500))






