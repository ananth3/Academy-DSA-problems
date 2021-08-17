def binarySearch(arr, low, high, target):
    if high >= low:
        mid = (high + low)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            return binarySearch(arr, low, mid-1, target)
        else:
            return binarySearch(arr, mid+1, high, target)
    else:
        return -1
        
arr = [1,2,3,4,5,6,7,8]
low = 0
high = len(arr) - 1
target = 7
result = binarySearch(arr, low, high, target)
print(result)
