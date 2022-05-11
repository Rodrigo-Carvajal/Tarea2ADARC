#Hacer benchmark a algoritmos MERGE, QUICK, BUBBLE, RADIX, HEAP e INSERTION SORT ordenando un arreglo 
#Se deben considerar distintos arreglos de n tamaños con valores enteros generados aleatoriamente entre 1 y 10.000.000

#Generar arreglo de tamaño n
import random
import time

n=100000
Array = []

for i in range(n):
    Array.append(random.randint(1,100))

for i in range(n):
    print(Array[i])

################ MERGE SORT ################
ArrayOrdenadoMerge = Array
inicioMerge = time.time()

def merge(ArrayOrdenadoMerge):
    if len(ArrayOrdenadoMerge) > 1:
        mid = len(ArrayOrdenadoMerge) // 2
        left = ArrayOrdenadoMerge[:mid]
        right = ArrayOrdenadoMerge[mid:]

        # Recursive call on each half
        merge(left)
        merge(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
            
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                ArrayOrdenadoMerge[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                ArrayOrdenadoMerge[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            ArrayOrdenadoMerge[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            ArrayOrdenadoMerge[k]=right[j]
            j += 1
            k += 1

merge(ArrayOrdenadoMerge)
print(ArrayOrdenadoMerge)

finMerge = time.time()
print("El tiempo que tomó ordenar el arreglo de tamaño ", n ," mediante el algoritmo MERGE SORT fue de ", finMerge-inicioMerge)

################ QUICK SORT ################
ArrayOrdenadoQuick = Array
inicioQuick = time.time()

def quick(ArrayOrdenadoQuick):
    izquierda = []
    centro = []
    derecha = []
    if len(ArrayOrdenadoQuick) > 1:
        pivote = ArrayOrdenadoQuick[0]
        for i in ArrayOrdenadoQuick:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        #print(izquierda+["-"]+centro+["-"]+derecha)
        return quick(izquierda)+centro+quick(derecha)
    else:
      return ArrayOrdenadoQuick

print(ArrayOrdenadoQuick)
print(quick(ArrayOrdenadoQuick))
finQuick = time.time()
print("El tiempo que tomó ordenar el arreglo de tamaño ",n," mediante el algoritmo QUICK SORT fue de ", finQuick-inicioQuick)

################ BUBBLE SORT ################
import random
import time

n=100000
Array = []

for i in range(n):
    Array.append(random.randint(1,100))

for i in range(n):
    print(Array[i])
ArrayOrdenadoBubble = Array
inicioBubble = time.time()

def bubble(ArrayOrdenadoBubble):
    
finBubble = time.time()
print("El tiempo que tomó ordenar el arreglo de tamaño ",n," mediante el algoritmo BUBBLE SORT fue de ", finBubble-inicioBubble)


################ RADIX SORT ################

ArrayOrdenadoRadix = Array
inicioRadix = time.time()

def radix(ArrayOrdenadoRadix):
    
finRadix = time.time()
print("El tiempo que tomó ordenar el arreglo de tamaño ",n," mediante el algoritmo RADIX SORT fue de ", finRadix-inicioRadix)


################ HEAP SORT ################

ArrayOrdenadoHeap = Array
inicioHeap = time.time()

def heap(ArrayOrdenadoHeap):
    
finHeap = time.time()
print("El tiempo que tomó ordenar el arreglo de tamaño ",n," mediante el algoritmo HEAP SORT fue de ", finHeap-inicioHeap)


################ INSERTION SORT ################

ArrayOrdenadoInsert = Array
inicioInsertion = time.time()

def insertion(ArrayOrdenadoInsert):
    
finInsertion = time.time()
print("El tiempo que tomó ordenar el arreglo de tamaño ",n," mediante el algoritmo INSERTION SORT fue de ", finInsertion-inicioInsertion)

