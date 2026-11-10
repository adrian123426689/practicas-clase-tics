deportes=["futbol"]
dep=input("ingresa un deporte")
deportes.append(dep)
print(deportes)
dep2=input("ingresa otro deporte")
deportes.append(dep2)
print(deportes)
depBorrar=input("Cual quieres borrar")
deportes.remove(depBorrar)
print(deportes)
dep3=input("Dime otro deporte")
pos=int(input("En que posicion"))
deportes.insert(pos,dep3)
print(deportes)



#Tarea 1
palabra=input("escribe algo")
letra=input("escribe una letra")
if letra in palabra:
    print("LA LETRA SI ESTA EN LA PALABRA")
else:
    print("LA LETRA NO ESTA EN LA PALABRA")
cantidad=palabra.lower(count)(letra)
print("la letra aparece"(cantidad),"veces")
palabraNueva=palabra.replace(letra,"X")
cantidadletras=len(palabra)
if len(palabra)>5:
    print("tiene mas de 5")
else:
    print("tiene menos de 5")
