def reverseArray(arr):
    start = 0
    end = len(arr) - 1
    while start<end:
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end-=1
arr = [1,2,3,4,5,6,7,8]
reverseArray(arr)
print(arr)