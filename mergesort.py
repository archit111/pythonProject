import math

def merge(li,p,q,r):
    n1=q-p+1
    n2=r-q
    l=[None]*(n1+1)
    ri=[None]*(n2+1)
    for i in range(n1):
        l[i]=li[p+i]
    for j in range(n2):
        ri[j]=li[q+j+1]

    l[n1]=('inf')
    ri[n2]=('inf')

    i=0
    j=0
    for k in range (p,r+1):
        if l[i]<ri[j]:
            li[k]=l[i]
            i=i+1

        else:
            li[k]=ri[j]
            j=j+1

    return li


def mergesort(li,p,r):
    sk=[]
    if p<r:
        q=math.floor((p+r)/2)
        mergesort(li,p,q)
        mergesort(li,q+1,r)
        sk=merge (li,p,q,r)

    return sk

li=[]
p=0
print ("Enter the qunatity")
n=int(input())
print ("enter the numbers ")
for i in range (n):
    li.append(input())
r=len(li)-1
print(mergesort(li,p,r))

