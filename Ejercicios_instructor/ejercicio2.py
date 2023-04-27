# El ejercicio 2 constara de un codigo donde el usuario pueda ingresar la hora, los minutos
# y los segundos actuales, el sistema le mostrara que horas son un segundo despues de la 
# hora que inserto 

hora = int(input("Ingrese la hora en horario militar: "))
min = int(input("Ingrese los minuto: "))
seg = int(input("Ingrese los segundos: "))

print (f"Segun la hora que ingreso deberian ser las: {hora}:{min}:{seg}")
if seg >= 60:
    seg = 0
    min = min + 1
    
    if seg < 60:
        seg = seg + 1

    if min >= 60 and seg == 60:
        hora = hora + 1

if hora > 24:
    hora == 0

print (f"La hora que ingreso mas un segundo de mas daria que son las: {hora}:{min}:{seg}")


