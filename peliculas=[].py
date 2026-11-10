peliculas=[]
cantidadPelis=int(input("cuantas peliculas vas a agregar"))
i=0
while i<cantidadPelis:
    peli=input("ingresar peli:")
    peliculas.append(peli)
    print(peliculas)
    i=i+1
peliBuscar=input("Que peli buscas")
if peliBuscar in peliculas:
    print("si esta")
else:
    print("No esta pero dejame la agrego")
    peliculas.append(peliBuscar)
    print(peliculas)
peliborrar=input("cual peli quieres borrar")
peliculas.remove(peliborrar)
print(peliculas)