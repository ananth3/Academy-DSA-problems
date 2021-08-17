def partition(arr,start,end):
    pivot = arr[end]
    p_index = start
    print(start)
    print(end)
    for i in range(start,end):
        if arr[i] <= pivot:
            print(i,p_index)
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index+=1
    arr[p_index], arr[end] = arr[end], arr[p_index]
    return p_index
    
def quicksort(arr,start,end):
    if (start<end):
        pi = partition(arr,start,end)
        quicksort(arr,start,pi-1)
        quicksort(arr,pi+1,end)

arr = [7,2,1,6,8,5,3,4]
start = 0
end = len(arr) - 1
quicksort(arr,start,end)
print(arr)

