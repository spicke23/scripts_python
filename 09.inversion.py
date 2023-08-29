capital = float(input("Ingrese cantidad de capital a invertir: "))
interes = float(input("Indique el porcentaje anual: "))
años = int(input("Años de inversión: "))
print("El capital final será de: " + str(round(capital * (interes / 100 + 1) ** años, 2)))