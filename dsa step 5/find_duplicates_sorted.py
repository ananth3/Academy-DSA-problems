def findDuplicates(arr):
    result = []
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] == 0:
            result.append(arr[i])
    return result
            
arr = [1,2,2,3,4,4,5]
print(findDuplicates(arr))