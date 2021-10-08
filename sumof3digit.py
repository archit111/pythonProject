'''def sum_three_digit(arr,n):

    for i in range(0,len(arr)):
        for j in range (i+1,len(arr)):
            k=j+1
            x=k
            if x<len(arr):
                if (int(arr[i])+int(arr[j])+int(arr[x])==n):
                    print(arr[i],arr[j],arr[x])
                x=x+1

n=15
arr=[1,2,3,5,7,6]
sum_three_digit(arr,n)'''

def remove_duplicates(ar):
    sum=0
    for i in range(len(ar)):
        c=0
        c=ar.count(ar[i])
        if (c==1):
            sum+=ar[i]
    return sum
ar=[12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
print(remove_duplicates(ar))

def sumofevenoccuring(ar):
    sum=0
    for i in range (len(ar)):
        c=0
        c=ar.count(ar[i])
        if (c%2==0):
            sum+=ar[i]

    return sum

ar = [12, 1, 12, 3, 1, 1, 2, 3]
print(sumofevenoccuring(ar))

def sumofelementsktimes(ar,k):
    sum=0
    visited=[]
    for i in range (len(ar)):
        c=0
        if ar[i] not in visited:
            visited.append(ar[i])
            c=ar.count(ar[i])
            if (c==k):
                sum+=ar[i]

    return sum

k=int(input())
ar = [9, 8, 8, 8, 10, 4]
print(sumofelementsktimes(ar,k))

def divisible_sum_pairs(ar,k):
    sum=0
    for i in range (len(ar)):
        for j in range (i+1,len(ar)):
            if i<j:
                sum=ar[i]+ar[j]
                if sum%k==0:
                    print(ar[i],ar[j])

k=3
ar=[1,3,2,6,1,2]
divisible_sum_pairs(ar,k)