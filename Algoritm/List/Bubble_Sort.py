def BubbleSort(lst):
    for i in range(len(lst)-1, 0 ,-1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
print(BubbleSort([3,1,5,2,10,7,6]))