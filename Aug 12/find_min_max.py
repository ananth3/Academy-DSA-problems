def maxMin(arr):
    maxi = arr[0]
    mini = arr[0]
    for i in range(len(arr)):
        if arr[i] < mini:
            mini = arr[i]
        elif arr[i] > maxi:
            maxi = arr[i]
    return [mini,maxi]
arr = [10,2,3,4,5]
print(maxMin(arr))