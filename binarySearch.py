pos = -1
def binarySearch(arr, val):
    arr.sort()
    min = 0
    max = len(arr)-1
    while(min<=max):
        mid = (min+max)//2
        if(arr[mid] == val):
            return ('Found at %s'%(mid+1))
        else:
            if(arr[mid]<val):
                min = mid + 1
            if(arr[mid]>val):
                max = mid - 1
    return 'oops'


arr = [12,34,45,56,78,4321,12,3]
print(binarySearch(arr,3))