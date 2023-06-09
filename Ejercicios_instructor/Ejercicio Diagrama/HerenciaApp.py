from Cliente import *
from Productos import *

persona = Cliente(10,"Normal","Soy una persona individual")
persona2 = Cliente(20,"Normal","Soy una persona empresa")
print (persona.getDatos())
print (persona.setId(11))
print (persona.getDatos())

ob1 = Producto(1,"Arroz","Grano","Grasas",1000)
# ob2 = Producto(2,"Lenteja","Grano","Engorda")
persona.agregarProducto(ob1)
# persona.agregarProducto(ob2)
for producto in persona.getProductos():
    print (f"AGREGACION {producto.getProducto()}")

persona2.componerProducto(2,"Arroz","Grano","Grasas",2000)
for producto in persona2.getProductos():
    print (F"COMPOSICION {producto.getProducto()}")
