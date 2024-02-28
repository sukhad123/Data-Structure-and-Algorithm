'''
The algorithm to merge already sorted list works like this

create an empty merged list
have a way to "point" at the first element of each of the two list
compare the values being pointed at and pick the smaller of the two
copy the smaller to the end of the merged list, and advance the "pointer" of the list that the value came from
continue until one of the list is completely copied then copy over remainder of the rest of the list
''' 
def merge(firstHalf, secondHalf):
    emptylst = [0] * (len(firstHalf) + len(secondHalf))  # Pre-allocate list
    
    i = j = z = 0
    while i < len(firstHalf) and j < len(secondHalf):
        if firstHalf[i] < secondHalf[j]:
            emptylst[z] = firstHalf[i]
            i += 1
        else:
            emptylst[z] = secondHalf[j]
            j += 1
        z += 1
    
    # Copy remaining elements from either half
    while i < len(firstHalf):
        emptylst[z] = firstHalf[i]
        i += 1
        z += 1
    
    while j < len(secondHalf):
        emptylst[z] = secondHalf[j]
        j += 1
        z += 1
    
    return emptylst


def mergeSort(lst):
    if len(lst) <= 1: 
        return lst
    
    middle = len(lst)//2
    firstHalf = lst[:middle]
    secondHalf = lst[middle:]
    
    # Recursively sort the halves
    firstHalf = mergeSort(firstHalf)
    secondHalf = mergeSort(secondHalf)
    
    # Merge the sorted halves
    return merge(firstHalf, secondHalf)

 
print(mergeSort([5,4,3,2,1]))
