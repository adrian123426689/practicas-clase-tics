numeros=[]
numpares=[]
i=0
while i<10:
    num=int(input("ingresa un numero:"))
    numeros.append(num)
    i=i+1
print("numeros pares")
for num in numeros:
    if num % 2==0:
        numpares.append(num)
        print(num)   
print("Lista de numeros pares",numpares)