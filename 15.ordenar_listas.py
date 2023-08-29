def burbuja(arr):
   largo = len(arr)
   for i in range(1,largo):
       for j in range(largo-1):
           if arr[j] > arr[i]:
               arr[j],arr[i] = arr[i],arr[j]
   print("Arreglo ordenado por 'Metodo Burbuja': ", arr)

arreglo = [9,3,5,1,7,2,8,6,4]
print("Arreglo inicial: ",arreglo)
burbuja(arreglo)

########################

def seleccion(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print("Arreglo ordenado por 'Seleccion Directa': ", arr)

arreglo = [4,2,3,5,1,6,7,9,8]
print("Arreglo inicial: ",arreglo)
seleccion(arreglo)
########################