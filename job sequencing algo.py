def printschedulingalgo(arr,t):

    arr.sort(key=lambda x:x[2],reverse=True)
    result=[False]*t
    job=[-1]*t
    for i in range (len(arr)):
        for j in range (min(t-1,arr[i][1]-1),-1,-1):

            if result[j]==False:
                result[j]=True
                job[j]=arr[i][0]
                break

    print(job)






arr = [['a', 2, 100],  # Job Array
        ['b', 1, 19],
        ['c', 2, 27],
        ['d', 1, 25],
        ['e', 3, 15]]

printschedulingalgo(arr,3)