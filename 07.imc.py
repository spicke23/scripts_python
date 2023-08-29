peso = float(input("Ingresa tu peso en KG: "))
estatura = float(input("Ingresa tu estatura en MT: "))
imc = round(peso / (estatura ** 2),2)
print("Tu indice de masa es IMC: ", str(imc))