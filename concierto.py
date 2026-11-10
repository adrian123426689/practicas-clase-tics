edad=float(input("Ingresa tu edad"))
permiso=input("¿Tienes permiso?")
acomp=input("¿Vienes acompañado?")
if edad>18 or permiso=="si" or acomp=="si":
    print("puedes pasar al concierto")
elif edad>18 or permiso=="no" or acomp=="no":
    print("No puedes pasar al concierto")
else:
    print("NO VALIDO")