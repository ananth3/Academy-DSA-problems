def findDuplicates(arr):
    result = []
    mem = {}
    for i in range(len(arr)):
        if arr[i] in mem:
            result.append(arr[i])
        else:
            mem[arr[i]] = 1
    return result

arr = [2,2,3,4,5,5,6,7,7,9]
print(findDuplicates(arr))