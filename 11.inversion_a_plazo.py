inversion = float(input("Introduce el valor de la inversión inicial: "))
interes = 0.04
balance = 1
n = int(input("Introduce cantidad de años a mantener la inversion: "))
for i in range(1,n+1):
    if i == 1:
        balance = inversion * (1 + interes)
        print("Balance para el año ",i, "es de: " + str(round(balance, 2)))
    else:
        balance *= (1 + interes)
        print("Balance para el año ",i, "es de: " + str(round(balance, 2)))