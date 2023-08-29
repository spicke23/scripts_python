peso_payaso = 0.112
peso_muneca = 0.075
cant_payaso = int(input("Ingrese cantidad de payasos vendidos: "))
cant_muneca = int(input("Ingrese cantidad de muñecas vendidas: "))
total = peso_payaso*cant_payaso + peso_muneca+cant_muneca
print("El peso total del paquete a enviar es de: {:,.3f}".format(total),"kilos")