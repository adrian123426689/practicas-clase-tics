#Programa que me indica si reprobe o aprobe
#Solicitar dato,calif
calif= float (input("ingresa la calificacion"))
#SI LA CALIFICACION >=6: APROBO
if calif >=6:
    print("Aprobaste")
else:
    print("Reprobaste")

#Programa que solocita mi edad
#Indica sin soy mayor de edad
edad=float (input("ingresa tu edad"))
if edad >=18:
    print("eres mayor de edad")
else:
    print("eres menor de edad" )
#programa que solicita una temperatura
#Indica si la temp>=35 hace mucho calor
#si no hace tanto calor
temp= float (input("ingresa la temperatura"))
if temp >=35:
    print("Hace mucho calor")
else:
    print("No hace tanto calor")
