#Hacer benchmark a algoritmos MERGE, QUICK, BUBBLE, RADIX, HEAP e INSERTION SORT ordenando un arreglo 
#Se deben considerar distintos arreglos de n tamaños con valores enteros generados aleatoriamente entre 1 y 10.000.000

#Importar librerías
import random
import time

n=10
Array = []

#Generar arreglo de tamaño n con enteros aleatorios
for i in range(n):
    Array.append(random.randint(1,10000000))
#Imprimir arreglo que se desea ordenar
print("El arreglo a ordenar es:")
print(Array)

################ MERGE SORT ################
import random
import time

n=10
Array = []

#Generar arreglo de tamaño n con enteros aleatorios
for i in range(n):
    Array.append(random.randint(1,10))
#Imprimir arreglo que se desea ordenar
print("El arreglo a ordenar es:")
print(Array)
ArrayOrdenadoMerge = Array

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

inicioMerge = time.time()
merge(ArrayOrdenadoMerge)
finMerge = time.time()
print("El tiempo que tomó ordenar el arreglo de tamaño ", n ," mediante el algoritmo MERGE SORT fue de ", finMerge-inicioMerge)
#print("La lista ordenada quedó así:", ArrayOrdenadoMerge)

################ QUICK SORT ################
import random
import time

n=10
Array = []

#Generar arreglo de tamaño n con enteros aleatorios
for i in range(n):
    Array.append(random.randint(1,10))
#Imprimir arreglo que se desea ordenar
print("El arreglo a ordenar es:")
print(Array)
ArrayOrdenadoQuick = Array

def quick(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        #print(izquierda+["-"]+centro+["-"]+derecha)
        return quick(izquierda)+centro+quick(derecha)
    else:
      return lista

inicioQuick = time.time()
quick(ArrayOrdenadoQuick)
finQuick = time.time() 
print("El tiempo que tomó ordenar el arreglo de tamaño ",n," mediante el algoritmo QUICK SORT fue de ", finQuick-inicioQuick)

################ BUBBLE SORT ################
ArrayOrdenadoBubble = Array

def bubble(ArrayOrdenadoBubble):
    # loop to access each array element
    for i in range(len(ArrayOrdenadoBubble)):
        # loop to compare array elements
        for j in range(0, len(ArrayOrdenadoBubble) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if ArrayOrdenadoBubble[j] > ArrayOrdenadoBubble[j + 1]:

                # swapping elements if elements
                # are not in the intended order
                temp = ArrayOrdenadoBubble[j]
                ArrayOrdenadoBubble[j] = ArrayOrdenadoBubble[j+1]
                ArrayOrdenadoBubble[j+1] = temp

inicioBubble = time.time()
bubble(ArrayOrdenadoBubble)
finBubble = time.time()
print("El tiempo que tomó ordenar el arreglo de tamaño ",n," mediante el algoritmo BUBBLE SORT fue de ", finBubble-inicioBubble)
#print("La lista ordenada quedó así:", ArrayOrdenadoBubble)

################ RADIX SORT ################
ArrayOrdenadoRadix = Array

def counting_Sort(arr, p):
    s = len(arr)
    result = [0] * s
    c = [0] * 10
    
    # count of elements
    for i in range(0, s):
        index = arr[i] // p
        c[index % 10] += 1
        
    # cumulative count
    for i in range(1, 10):
        c[i] += c[i - 1]

    # sorted order
    i = s - 1
    while i >= 0:
        index = arr[i] // p  
        result[c[index % 10] - 1] = arr[i]
        c[index % 10] -= 1
        i -= 1
        
    for i in range(0, s):
        arr[i] = result[i]

#  radix sort
def radix(arr):
    maximum = max(arr)

    p = 1
    while maximum // p > 0:
        counting_Sort(arr, p)
        p *= 10

inicioRadix = time.time()
radix(ArrayOrdenadoRadix)    
finRadix = time.time()
print("El tiempo que tomó ordenar el arreglo de tamaño ",n," mediante el algoritmo RADIX SORT fue de ", finRadix-inicioRadix)
#print("La lista ordenada quedó así:", ArrayOrdenadoRadix)

################ HEAP SORT ################
ArrayOrdenadoHeap = Array

def heapify(arr, m, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
  
    # See if left child of root exists and is
    # greater than root
    if l < m and arr[i] < arr[l]:
        largest = l
  
    # See if right child of root exists and is
    # greater than root
    if r < m and arr[largest] < arr[r]:
        largest = r
  
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
  
        # Heapify the root.
        heapify(arr, m, largest)
  
# The main function to sort an array of given size
def heap(arr):
    m = len(arr)
  
    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, m, i)
  
    # One by one extract elements
    for i in range(m-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)
  
m = len(ArrayOrdenadoHeap)    
inicioHeap = time.time()
heap(ArrayOrdenadoHeap)
finHeap = time.time()
print("El tiempo que tomó ordenar el arreglo de tamaño ",n," mediante el algoritmo HEAP SORT fue de ", finHeap-inicioHeap)
#print("La lista ordenada quedó así:", ArrayOrdenadoHeap)

################ INSERTION SORT ################
ArrayOrdenadoInsert = Array

def insertion(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
  
        key = arr[i]
  
        j = i-1

        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    
inicioInsertion = time.time()
insertion(ArrayOrdenadoInsert)
finInsertion = time.time()
print("El tiempo que tomó ordenar el arreglo de tamaño ",n," mediante el algoritmo INSERTION SORT fue de ", finInsertion-inicioInsertion)
#print("La lista ordenada quedó así:", ArrayOrdenadoInsert)