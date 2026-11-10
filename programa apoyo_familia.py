sexo=(input("Ingresa tu sexo"))
edad=int(input("Escribe tu edad"))
estaci=float(input("Ingresa tu estado civil"))
hijos=int(input("¿Cuantos hijos tienes?"))
if sexo=="mujer" and hijos==1 and edad<18:
    print("“Eres mujer,tienes un hijo y eres menor de edad entonces el apoyo seráde $800”")
elif sexo=="mujer" and hijos==1 and edad>18:
    print("“Eres mujer,tienes un hijo y eres mayor de edad entonces el apoyo será de $300”")
elif sexo=="mujer" and hijos>1 and edad<18:
    print("“Eres mujer,tienes más de un hijo y eres menorde edad entonces el apoyo es de $1500”")
elif sexo=="mujer" and hijos>1 and edad>=18:
    print("“Eres mujer,tienes más de un hijo y ya eres mayor de edad entonces el apoyo es de $500”")
elif sexo=="hombre" and hijos>1 and estaci=="soltero":
    print("“Eres hombre y tienes hijos el apoyo es de $780”")
else:
    print("no valido")