x = int(input("Ingrese primer valor: "))
y = int(input("Ingrese segundo valor: "))

if x > y:
    print("El numero mayor entre",x,"y",y," es: ",x)
elif x < y:
    print("El numero mayor entre",x,"y",y," es: ",y)
else: # a == b
    print("Ambos numeros",x,"y",y,"son iguales")
