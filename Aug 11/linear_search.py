def linearSearch(arr, target):
	n = len(arr)
	for i in range(n):
		if arr[i] == target:
			return i
	return -1
arr = [1,2,3,4,5]
target = 5
print(linearSearch(arr,target))