def union(arr1,arr2):
    i = j = 0
    n = len(arr1)
    m = len(arr2)
    result = []
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i+=1
        elif arr1[i] > arr2[j]:
            result.append(arr2[j])
            j+=1
        else:
            result.append(arr1[i])
            i+=1
            j+=1
    return result

arr1 = [1,2,5,6,7]
arr2 = [1,3,4,8]
print(union(arr1,arr2))