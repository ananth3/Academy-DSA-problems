def missingInteger(arr):
    n = arr[-1]
    return n * (n+1)//2 - sum(arr)
arr = [1,2,4,5]
print(missingInteger(arr))