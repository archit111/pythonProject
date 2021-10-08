'''def rotation(arr,n):

    k=len(arr)-1
    ar = []*len(arr)
    for j in range(len(arr)-1,-1,-1):
        ar[k-n]=arr[j]
        k=k+1
    print(ar)
n=2
arr=[0,1,2,4,5,6,7]
rotation(arr,n)'''

word='abc'
print(list(word))

