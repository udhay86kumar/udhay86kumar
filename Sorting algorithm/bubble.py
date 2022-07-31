def bubble_sort(array):
    length=len(array)
    for iterator_1 in range(length):
        for iterator_2 in range(0,length-iterator_1-1):
            if array[iterator_2]>array[iterator_2+1]:
                array[iterator_2],array[iterator_2+1]=array[iterator_2+1],array[iterator_2]
array=[15,67,54,34,98]
bubble_sort(array)
print("Array values after sorting")
for i in range(len(array)):
     print("%d"%array[i])