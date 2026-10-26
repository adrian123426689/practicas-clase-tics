nombre=(input("Ingrese su nombre"))
pagxhora=float(input("ingrese su sueldo por hora"))
horxmes=int(input("Ingrese sus horas trabajadas este mes"))
sueldo= pagxhora*horxmes
print("Tu sueldo es:",sueldo)
if sueldo>=100 and sueldo<=300:
    print("Tu sueldo con bono es",sueldo+500)
elif sueldo>300 and sueldo<=1500:
    print("Tu sueldo con bono es",sueldo+1700)
elif sueldo>1500 and sueldo<=3000:
    print("Tu sueldo con bono es",sueldo+3500)
elif sueldo>3000 and sueldo<=8000:
    print("Tu sueldo con bono es",sueldo+8500)
elif sueldo>8000:
    print("Tu sueldo con bono es",sueldo+10000)
else:
    print("No valido")