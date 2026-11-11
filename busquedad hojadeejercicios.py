nombres=["Angel","Karla","Luis","Mateo","Maria","Luis","Karla"]
print(f"Los nombres que tienen son:{nombres}")
nombrebuscar=input("Que nombre quieres buscar?:")
encontrado=False
contador=0
i=0
while i<len(nombres):
    if nombres[i]==nombrebuscar:
        encontrado=True
        contador=contador+1
        print("Encontrado en la posocion:",i)
    i=i+1
if encontrado==True:
    print("Nombre encontrado")
    print("Aparece",contador,"veces")
else:
    print("nombre no encontrado")

if contador > 1:
    while nombrebuscar in nombres:
        nombres.remove(nombrebuscar)
        print("Se elimino porque aparecia 2 veces",nombrebuscar)