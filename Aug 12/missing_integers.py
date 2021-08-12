def missingIntegers(arr):
    result = []
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] != 1:
            diff = arr[i+1] - arr[i]
            j = 1
            while j < diff:
                result.append(arr[i]+j)
                j+=1
    return result
arr = [1,2,3,9]
print(missingInteger(arr))