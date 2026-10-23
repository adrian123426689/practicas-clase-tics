#Solicitar una temperatura
temp=float(input("Ingrese su temperatura"))
if temp>=40:
    input("Hace mucho calor")
elif temp>=30 and temp<40:
    input ("Esta templadito")
elif temp>=20 and temp<30:
    input("Esta fresco")
elif temp <=20:
    input("Hace frio")
else:
    input("no valido")