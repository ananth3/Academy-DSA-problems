# def partition(arr,start,end):
#     pivot = arr[end]
#     p_index = start
#     print(start)
#     print(end)
#     for i in range(start,end):
#         if arr[i] <= pivot:
#             print(i,p_index)
#             arr[i], arr[p_index] = arr[p_index], arr[i]
#             p_index+=1
#     arr[p_index], arr[end] = arr[end], arr[p_index]
#     return p_index
    
# def quicksort(arr,start,end):
#     if (start<end):
#         pi = partition(arr,start,end)
#         quicksort(arr,start,pi-1)
#         quicksort(arr,pi+1,end)

# arr = [7,2,1,6,8,5,3,4]
# start = 0
# end = len(arr) - 1
# quicksort(arr,start,end)
# print(arr)

def merge(left_arr,right_arr,arr):
    n = len(left_arr)
    m = len(right_arr)
    i = j = k = 0
    while i<n and j<m:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            k+=1
            i+=1
        else:
            arr[k] = right_arr[j]
            k+=1
            j+=1
    while i<n:
        arr[k] = left_arr[i]
        k+=1
        i+=1
    while j<m:
        arr[k] = right_arr[j]
        k+=1
        j+=1

def mergeSort(arr):
    n = len(arr)
    if n>1:
        mid = n//2
        l_arr = [arr[i] for i in range(mid)]
        r_arr = [arr[i] for i in range(mid,n)]
        mergeSort(l_arr)
        mergeSort(r_arr)
        merge(l_arr,r_arr,arr)
        

arr = [7,2,1,6,8,5,3,4]
mergeSort(arr)
print(arr)
    
        
