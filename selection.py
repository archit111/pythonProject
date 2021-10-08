def selection(arr):
    n=len(arr)
    for i in range (0,n):
        min_index=i
        for j in range (i+1,n):
            if arr[j]< arr[min_index]:
                min_index=j
        arr[min_index],arr[i]=arr[i],arr[min_index]

print ("enter a size of array")
arr=[]
n=int (input())
for i in range (0,n):
    arr.append(input())
selection(arr)
print (arr)

