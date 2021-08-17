def checkSorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
arr = [1,2,3,4,6,5,7,8]
result = checkSorted(arr)
# print(result)
if result:
    print("Array is sorted")
else:
    print("Array is not sorted")