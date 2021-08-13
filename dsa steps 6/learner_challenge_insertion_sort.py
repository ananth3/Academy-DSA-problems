def insertionSort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i-1
        while k < arr[j] and j>=0:
            arr[j + 1] = arr[j]
            j-=1
        arr[j+1] = k
arr = [6,7,4,1,3,9]
insertionSort(arr)
print(arr)