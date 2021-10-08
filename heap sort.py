'''def bubble_sort(arr):
    n=len(arr)
    for i in range (0,n-1):
         for j in range (0,n-i-1):
             if arr[j]> arr[j+1]:
                 arr[j], arr[j+1]=arr[j+1],arr[j]

arr=[5,8,7,6,4,9]
bubble_sort(arr)

print ('sorted array')
#for i  in range(0,len(arr)):
print(arr)'''

def sum_pairs(arr,n):
    k=len(arr)
    for i in range (0,k):
        for j in range (i+1,k):
            if (int(arr[i])+int(arr[j]))==n:
                print('(',arr[i],',',arr[j],')')
arr=[]
print("enter the size of array")
m=int(input())
print ("enter the elements of an array")
for i in range (0,m):
    arr.append(input())
print ("enter the number")
n=int(input())
sum_pairs(arr,n)




