numeros=[]
resultados=[]
i=0
while i<5:
    num=int(input("ingresa un numero:"))
    numeros.append(num)
    i=i+1
multiplicador=int(input("Por cuanto deseas multiplicar?:"))

for num in numeros:
    resultado=num*multiplicador
    resultados.append(resultado)

print("Numeros originales:",numeros)
print("Resultados:",resultados)
buscar=int(input("Que numero quieres buscar en la lista de resultados?:"))
if buscar in resultados:
    print("si aparece",buscar,"en la lista de resultados")
else:
    print("no aparece",buscar,"en la lista de resultados")