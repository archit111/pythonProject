def knapsack(arr):
    rem_weight=weight
    final_result=0
    for i in range (len(arr)):
        j=2
        arr[i][j]=((arr[i][1])//(arr[i][0]))
    flag=True
    arr.sort(key=lambda x:x[2],reverse=True)
    i=0
    while (flag):
        if i!=len(arr)-1:
            final_result+=arr[i][1]
            rem_weight = rem_weight - arr[i][0]
            i = i + 1
            flag=True
        else:
            final_result+=(arr[i][1])*((rem_weight)/(arr[i][0]))
            flag=False
    return final_result
weight=50
arr=[[10,60,None],[20,100,None],[30,210,None ]]
print(knapsack(arr))