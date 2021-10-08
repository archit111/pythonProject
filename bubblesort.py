'''def bubble_sort(arr):
    k=len(arr)
    for i in range (0,k):
        for j in range (0,k-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]'''

'''def insertion_sort(arr):
    k=len(arr)
    for i in range (1,k):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key



arr=[]
print("Enter a size of array")
n=int(input())
for i in range (0,n):
    arr.append(input())
insertion_sort(arr)
print ("Array in sorted order")
for i in range(0,n):
    print (arr[i])'''

def selection_sort(arr):
    for i in range (0,len(arr)):
        min=0
        min=arr[i]
        for j in range(i+1,len(arr)):
            if arr[j]<min :
                min=arr[j]
                arr[i],arr[j]=arr[j],arr[i]


arr=[]
print("Enter a size of array")
n=int(input())
for i in range (0,n):
    arr.append(input())
selection_sort(arr)
print ("Array in sorted order")
for i in range(0,n):
    print (arr[i])
