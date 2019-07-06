'''
benefit of selection sort, you need to swap only sequece array with min value or max value.
don't need to swap every value like: bubble sort

Time Complexity: O(n2) as there are two nested loops.
Auxiliary Space: O(1) The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.
In Place : Yes, it does not require extra space.
'''
def sort(list):
    for i in range(len(list)-1):
        minPos = i
        for j in range(i,len(list)):
            if(list[j]<list[minPos]):
                minPos = j
        list[minPos], list[i] = list[i], list[minPos]
        
list = [2, 3, 4, 2, 3, 444, 2234, 1, 56, 8898, 6, 532, 32]
sort(list)
print(list)