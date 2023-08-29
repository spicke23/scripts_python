def bilzPap(n):
    largo = n+1
    for number in range(1,largo):
        if (number % 3 == 0) and (number % 5 == 0):
            print("BilzPap")
            continue
        elif (number % 3 == 0):
            print("Bilz")
            continue
        elif (number % 5 == 0):
            print("Pap")
            continue
        print(number)

####################### PRINCIPAL #######################
n = input("Ingrese Valor de N: ")
n = int(n)
bilzPap(n)