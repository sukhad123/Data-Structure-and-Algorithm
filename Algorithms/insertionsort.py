#Insertion sort is called insertion sort because the algorithm repeatedly inserts a value into the part of the array that is already sorted. It essentially chops the array into two pieces. The first piece is sorted, the second is not. 
def insertionSort(lst):
    for i in range(1, len(lst)):
        z = i
        while lst[z] < lst [z -1 ] and z > 0:
            #Rearrange if the current element is smaller than the previous one
            lst[z], lst[z- 1] = lst[z - 1], lst[z]
            z -= 1
    return lst

print(insertionSort( [8, 3,3, 1, 9, 6, 4, 5, 2, 7]))