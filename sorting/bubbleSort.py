'''
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping
the adjacent elements if they are in wrong order.

Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.
Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
Auxiliary Space: O(1)
Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.
Sorting In Place: Yes
Stable: Yes
'''
def sort(list):
    for i in range(len(list)):
        for j in range(i, len(list)):
            if(list[i] > list[j]):
                list[i], list[j] = list[j], list[i]
    return list

print(sort([2, 3, 4, 2, 3, 444, 2234, 1, 56, 8898, 6, 532, 32]))