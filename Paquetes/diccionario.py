def obtener_claves(diccionario):
    return list(diccionario.keys())

def obtener_valores(diccionario):
    return list(diccionario.values())

def obtener_elemento(diccionario, clave):
    return diccionario.get(clave)

def agregar_elemento(diccionario, clave, valor):
    diccionario[clave] = valor

def eliminar_elemento(diccionario, clave):
    diccionario.pop(clave, None)