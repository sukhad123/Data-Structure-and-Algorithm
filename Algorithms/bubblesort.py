#Bubble Sort
#The algorithm would review two items at a time, rearrange those not already in ascending order from left to right, and then continue to cycle through the entire sequence until it completed a pass without switching any numbers.
def bubbleSort(arr):
    for z in range(0, len(arr) -1):     #3 +(n-1)
        
        for i in range(0,len(arr)-1 ):  #(3 + (n-1))*(n-1)
            if(arr[i] > arr[i + 1]):    #(2(n-1)) * (n-1)
                rc =arr[i + 1]          #2(n-1) *(n-1)
                arr[i + 1] = arr[i]     #2(n-1) *(n-1)
                arr[i] = rc             #(n-1) *(n-1)
    return arr                          #1
    
    
#Algorithm Analysis

# #T(n) = 3 + n-1 + (n + 4) *(n-1) + 5(n2 -1)  + 1 
#         2n + 2 + n2  - n + 4n -4 + 5n2 - 5 + 1
#         n -6 + 6n2
# T(n) = O(n2)