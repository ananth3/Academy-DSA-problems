def maxActivities(start,finish):
    i = 0
    print(i)
    for j in range(1,len(start)):
        if finish[i] <= start[j]:
            print(j)
            i=j
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
activity(start,finish)
