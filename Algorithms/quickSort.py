def quick(lst):
    if(len(lst) <= 1):
        return lst
    else:
        pivotElement =lst.pop()
        smallerHalf = []
        greaterHalf= []
        for item in lst:
            if(item < pivotElement):
                smallerHalf.append(item)
            else:
                greaterHalf.append(item)
        return (quick(smallerHalf) + [pivotElement] + quick(greaterHalf))

print(quick([5,4,3,2,1]))