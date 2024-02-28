#Selection Sort
#The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element of the unsorted part. This process is repeated for the remaining unsorted portion until the entire list is sorted. 
def selectionSort(lst):
    for i in range(len(lst)):
        small = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[small]:
                small = j
        lst[i], lst[small] = lst[small], lst[i]
    return lst

            
#Example        
print(selectionSort([3,2,6,9,5]))