def findPair(arr, k):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == k:
                return [arr[i],arr[j]]
arr = [2,5,7,3,9]
k = 10
print(findPair(arr,k))