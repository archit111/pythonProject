'''def fucn(arr):
    li=[]
    for i in range (len(arr)-1):
        maximum=0
        li=arr[i+1:len(arr)]
        maximum=max(li)
        arr[i]=maximum
    return arr

arr=[2,4,8,7,6,3]
print(fucn(arr))'''
import math

'''def findmedian(ar,br,cr):
    i=0
    j=0
    for k in range (kl-2):
        if ar[i]<br[j]:
            cr.append(ar[i])
            i=i+1
        else:
            cr.append(br[j])
            j=j+1
    return cr

ar=[1,5,7]
br=[2,8,3]
ar.append(float('inf'))
br.append(float('inf'))
cr=[]*(len(ar)+len(br))
kl=len(ar)+len(br)
print(findmedian(ar,br,cr))'''

'''s="array"
li=[]
last=0
for i in range (len(s)):
    if s[i] not in li:
        li.append(s[i])
print("".join(li))'''


'''def nextLargerElement(arr, n):
    for i in range(0,n-1):
        next=-1
        j = i + 1
        while (j <len(arr)):
            if arr[i] < arr[j]:
                next = arr[j]
                arr[i]=next
                break
            else:
                j = j + 1
        arr[i]=next
    arr[i] = -1
    return arr
n=5
arr=[4,1,3,2,5,6]
print(nextLargerElement(arr,n))'''
'''def secondmaxelement(arr):
    arr.sort(reverse=True)
    return arr[1]

arr=[7,2,5,3,10,15,9]
print(secondmaxelement(arr))

'''
'''def subsets(str,curr,index):
    if index == len(str):
        print(curr)
        return

    subsets(str,curr,index+1)
    subsets(str,curr+str[index],index+1)



curr=" "
index=0
str="ABC"
print(subsets(str,curr,index))'''

'''def towerofhanoi(n,from_rod,aux_rod,to_rod):
    if n==1:
        print("Move disc from",from_rod,"to",to_rod)
        return
    towerofhanoi(n-1,from_rod,to_rod,aux_rod)
    print("Move ", n ,"from",from_rod, "to", to_rod)
    towerofhanoi(n-1,aux_rod,from_rod,to_rod)
n=3
towerofhanoi(n,'A','B','C')'''

'''def secondlargestelement(arr):
    i=0
    max=0
    max=arr[i]
    for j in range (i+1,len(arr)):
        if arr[j]>max:
            max=arr[j]
    max1=arr[i]
    for j in range (len(arr)):
        if (arr[j]!=max):
            if arr[j]>max1:
                max1=arr[j]
    return max1

arr=[5,14,6,8,4,32,168,168]
print(secondlargestelement(arr))'''

'''def arraysorted(arr):
    flag=True
    if (len(arr)==1):
        return flag
    for i in range (len(arr)-1):
        if arr[i]>arr[i+1]:
            flag=False
            return flag
    return flag


arr = [100,20,200]
print(arraysorted(arr))'''


'''def reverse(arr):
    stack=[]
    for i in range (len(arr)):
        stack.append(arr[i])
    for i in range (len(arr),0,-1):
        print(stack.pop() , end=" ")


arr=[30,7,6,5,10]
reverse (arr)'''

'''def distinctelements(arr):
    temp=[]
    for i in range (len(arr)):
        if arr[i] not in temp:
            temp.append(arr[i])
    return temp

arr = [30, 7, 6, 5, 10,10,30,40,40,40,70,5]
print(distinctelements(arr))'''

'''def moveallzerostoend(arr):
    c=0
    for i in range (len(arr)):
        if arr[i]==0:
            for j in range (i+1,len(arr)):
                if arr[j]!=0:
                    arr[i],arr[j]=arr[j],arr[i]
    return arr


arr=[8,5,0,10,0,20]
print(moveallzerostoend(arr))

def moveallzerostoend(arr):
    c=0
    for i in range (len(arr)):
        if arr[i]!=0:
            arr[i],arr[c]=arr[c],arr[i]
            c=c+1
    return arr



arr=[8,5,0,10,0,20]
print(moveallzerostoend(arr))

def moveallzerostostart(arr):
    c=0
    for i in range (len(arr)):
        if arr[i]==0:
            arr[i],arr[c]=arr[c],arr[i]
            c=c+1
    return arr



arr=[8,5,0,10,0,20]
print(moveallzerostostart(arr))'''


'''def leaders(arr):
    li=[]
    for i in range (len(arr)-1):
        m=0
        m=max(arr[i+1:len(arr)])
        if arr[i]>m:
            li.append(arr[i])
    li.append(arr[-1])
    return li

arr=[30,20,10]
print(leaders(arr))'''

'''def maxdiff(arr):
    minvalue=arr[0]
    maxvalue=0
    for j in range (1,len(arr)):
        maxvalue=max(maxvalue,arr[j]-minvalue)
        minvalue=min(arr[j],minvalue)
    return maxvalue



arr=[2,3,10,4,6,8,1]
print(maxdiff(arr))'''

'''def frequencyofsortedarray(arr):
    s=dict()
    for i in range (len(arr)):
        if arr[i] in s.keys():
            s[arr[i]]+=1
        else:
            s[arr[i]]=1

    for x in s:
        print(x," ",s[x])


arr=[10,10,10,25,25,30]
frequencyofsortedarray(arr)'''


'''def trappingrainwater(arr,n):
    lmax=[0]*n
    rmax=[0]*n
    lmax[0]=arr[0]
    rmax[n-1]=arr[n-1]
    res=0
    for i in range (1,len(arr)-1):
        lmax[i]=(max(arr[i],lmax[i-1]))
    for i in range (len(arr)-2,-1):
        rmax[i]=(max(arr[i],rmax[i+1]))

    for i in range (1,len(arr)-1):
        res=res+min(lmax[i],rmax[i])-arr[i]

    return res

n=5
arr=[5,0,6,2,3]
print(trappingrainwater(arr,n))'''
'''import math
def majorityelement(arr):
    mid=0

    mid=math.ceil(len(arr)/2)
    for i in range (len(arr)):
        c=1
        li=[]
        li.append(i)
        for j in range (i+1,len(arr)):
            if arr[i]==arr[j]:
                c=c+1
                li.append(j)
        if c>=mid :
            print(li)




arr=[8,3,4,8,8]
majorityelement(arr)'''


'''def stockmarket (arr):
    price=0
    for i in range (1,len(arr)):
        if arr[i]>arr[i-1]:
            price =price +(arr[i]-arr[i-1])

    print (price)



arr=[1,5,3,8,12]
stockmarket(arr)'''


'''import math
def morevotingalgo(arr):
    res=0
    count=1
    for i in range (1,len(arr)):
        if arr[res]==arr[i]:
            count=count+1
        else:
            count=count-1

        if count==0:
            count=1
            res=i
    return res

def majorityelement(arr):
    re=0
    c=1
    mid=0
    mid=math.floor(len(arr)/2)
    re=morevotingalgo(arr)
    print(re)
    for i in range (len(arr)):
        if arr[re]==arr[i]:
            c=c+1
    if c> mid:
        return arr[re]
arr=[2,1,6,6,8,7,6]
print(majorityelement(arr)'''

'''def windowslidingtechnique(arr):
    a1=a2=0
    result=0
    for i in range (len(arr)-2):
        sum=0
        a1=arr[i+1]
        a2=arr[i+2]
        sum=arr[i]+int(a1)+int(a2)
        result=max(result,sum)
    print(result)

arr=[1,8,30,-5,20,33]
windowslidingtechnique(arr)'''

'''import math
def binarysearch (arr,x):
    low=0
    high=len(arr)
    mid=0
    mid=math.floor((low+high)/2)
    while (low<=high):
        if x==arr[mid]:
            return mid
        elif x>arr[mid]:
            mid=mid+1
        elif x<arr[mid]:
            mid=mid-1



arr=[10,20,30,40,50,60]
x=20
print(binarysearch(arr,x))'''

'''import math
def firstoccurences (arr,x):
    low=c=0
    high=len(arr)-1
    while (low<=high):
        mid = (low + high-1) // 2
        if x>arr[mid]:
            low=mid+1
        elif x<arr[mid]:
            high=mid-1
        else:
            if mid==0 or arr[mid-1]!=arr[mid]:
                return mid
            else:
                return mid-1

arr=[10,20,20,40,50,60]
x=20
print(firstoccurences(arr,x))

import math
def lastoccurences (arr,x):
    low=0
    high=len(arr)-1
    while (low<=high):
        mid = (low + high-1) // 2
        if x>arr[mid]:
            low=mid+1
        elif x<arr[mid]:
            high=mid-1
        else:
            if mid==len(arr)-1 or arr[mid]!=arr[mid+1]:
                return mid
            else:
                return mid+1

arr=[10,20,20,40,50,60,20]
x=20
print(lastoccurences(arr,x))'''

'''import math
def countones(arr):
    low=0
    n=len(arr)
    high=len(arr)-1
    c=0
    while (low<=high):
        mid=math.floor((low+high)/2)
        if arr[mid]==0:
            low=mid+1
        else:
            if mid==0 or arr[mid]!=arr[mid-1]:
                return (n-mid)
            else:
                high=mid-1

    return 0

arr=[0,0,1,1,1,1,1]
print(countones(arr))'''

'''import math
def countzeros(arr):
    low=0
    n=len(arr)
    high=len(arr)-1
    while (low<=high):
        mid=math.floor((low+high)/2)
        if arr[mid]==1:
            high=mid-1
        else:
            if mid==0 or arr[mid]!=arr[mid+1]:
                return mid+1
            else:
                low=mid+1

    return 0

arr=[0,1,1,1,1,1]
print(countzeros(arr))'''


'''def infinitearray(arr,x):
    i=0
    while (True):
        if (arr[i]==x):
            return i
        if arr[i]>x:
            return -1
        i=i+1

x=100
arr=[10,20,30,50,90,100,500,900,1024,1600]
print(infinitearray(arr,x))


import math
def binarysearch(arr,low,high,x):
    mid=0
    while (low<=high):
        mid=math.floor((low+high)/2)
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low=mid+1

def infinitearray(arr,x):
    k=0
    if arr[0]==x:
        return 0
    i=1
    while (arr[i]<=x):
        i=i*2
    k=binarysearch(arr,i/2+1,i-1,x)
    return k
x=100
arr=[10,20,30,50,90,100,500,900,1024,1600]
print(infinitearray(arr,x)'''

'''def peakelement(arr):
    if arr[0]>arr[1]:
        print(arr[0])
    if arr[len(arr)-1]>arr[len(arr)-2]:
        print(arr[len(arr)-1])
    for i in range (1,len(arr)-1):
        if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
            print(arr[i])

arr=[80,70,90]
print(peakelement(arr))'''

'''def findpairinsortedarray(arr,left,right,x):

    while (left<right):
        if arr[left]+arr[right]==x:
            print(arr[left], " ", arr[right])
            return True
        elif arr[left]+arr[right]>x:
            right=right-1
        elif arr[left]+arr[right]<x:
            left=left+1
    return False

x=23
left=0
right=len(arr)-1
arr=[2,4,8,9,11,12,20,30]
print(findpairinsortedarray(arr,x))

def findtriplet(arr,n):
    for i in range (0,len(arr)):
        if (findpairinsortedarray(arr,i+1,len(arr)-1,n-arr[i])==True):
            return "YES"
        else:
            return "NO"

n=16
arr=[2,3,4,8,9,20,40]
print(findtriplet(arr,n))'''

'''def repeatingelement(arr):
    arr.sort()
    for i in range (0,len(arr)-1):
        c=1
        if arr[i]==arr[i+1]:
            print (arr[i])

arr=[10,2,30,10,10,20]
repeatingelement(arr)'''


'''def repeatingelement(arr):
    s=[]
    for i in range (0,len(arr)):
        if arr[i] not in s:
            s.append(arr[i])
        else:
            return arr[i]

arr=[10,2,30,10,10,20]
print(repeatingelement(arr))'''

'''def selectionsort(arr):
    for i in range (len(arr)):
        min_index=i
        for j in range (i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

arr=[10,2,20,4,3]
print(selectionsort(arr))'''

'''def bubblesort(arr):
    for i in range (0,len(arr)):
        for j in range (0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[10,2,20,4,3]
print(bubblesort(arr))

def Insertionsort(arr):
    for i in range (len(arr)):
        key=arr[i]
        j=i-1
        while (j>=0 and  key<arr[j]):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

    return arr
arr=[10,2,20,4,3]
print(Insertionsort(arr))'''


'''import math
def merge (arr,low,mid,high):
    n1=mid-low+1
    n2=high-mid
    left=[None]*(n1+1)
    right=[None]*(n2+1)
    for i in range (0,n1):
        left[i]=arr[i]
    for i in range (0,n2):
        right[i]=arr[mid+1+i]
    i=j=k=0
    while (i<n1 and j<n2):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i=i+1
            k=k+1
        else:
            arr[k]=right[j]
            j=j+1
            k=k+1
    while (i<n1):
        arr[k]=left[i]
        i=i+1
        k=k+1
    while (j<n2):
        arr[k]=right[j]
        j=j+1
        k=k+1

    return arr

def mergesort(arr,low,high):
    li=[]
    if low<high:
        mid=math.floor(low+(high-low)/2)
        mergesort(arr,low,mid)
        mergesort(arr,mid+1,high)
        li=merge(arr,low,mid,high)
    print(li)

arr=[5,10,20,19,2,6,8,41]
mergesort(arr,0,len(arr))'''


'''def union(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    i=j=0
    while (i<n1 and j<n2):
        if(i>0 and arr1[i]==arr1[i-1]):
            i=i+1
            continue
        if (j>0 and arr2[j]==arr2[j-1]):
            j=j+1
            continue
        elif arr1[i]<arr2[j]:
            print(arr1[i])
            i=i+1
        elif arr1[i]>arr2[j]:
            print (arr2[j])
            j=j+1
        else:
            print (arr1[i])
            i=i+1
            j=j+1
    while (i<n1):
        if arr1[i]!=arr1[i-1]:
            print(arr1[i])
            i=i+1
    while (j<n2):
        if arr2[j]!=arr2[j-1]:
            print(arr2[j])
            j=j+1

arr1=[2,3,3,3,4,4]
arr2=[4,4]
union(arr1,arr2)'''

'''def countInversion(arr):
    c=0
    for i in range (len(arr)-1):
        for j in range (i+1,len(arr)):
            if arr[i]>arr[j]:
                c=c+1
    return c

arr=[40,30,20,10]
print(countInversion(arr))'''

'''def Lomuto(arr):
    pivot=arr[len(arr)-1]
    i=-1
    for j in range (0,len(arr)):
        if arr[j]<pivot :
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],pivot=pivot,arr[i+1]
    return i+1

arr=[10,15,12,13,18,21,22]
print(Lomuto(arr))'''



'''def smallestelement(arr,p):
    for i in range (len(arr)):
        key=arr[i]
        j=i-1
        while (j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key

    for i in range (0,len(arr)):
        if i+1==p:
            return arr[i]

arr=[30,20,5,10,8]
print (smallestelement(arr,4))


def partition(arr,l,r):
    pivot=arr[len(arr)-1]
    j=-1
    for i in range (0,len(arr)):
        if arr[i]<pivot:
            j=j+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[j+1],pivot=pivot,arr[j+1]
    return j+1

def smallestele(arr,x):
    l=0
    r=len(arr)-1
    while (l<=r):
        p=partition(arr)
        if x-1==p:
            return arr[p-1]
        elif x-1>p:
            l=p+1
        else:
            r=p-1
    return -1

x=4
arr=[30,20,5,10,8]
print(smallestele(arr,x))'''

'''def chocolatedistributionproblem(arr,m):
    arr.sort()
    li1=[]
    for i in range (0,len(arr)-m):
        li=arr[i:m+i]
        mi=min(li)
        ma=max(li)
        diff=ma-mi
        li1.append(diff)
    return min(li1)

m=3
arr=[7,3,2,4,9,12,56]
print(chocolatedistributionproblem(arr,m))'''

'''def sorttwotypes(arr):
    li=[]
    for i in range (len(arr)):
        if arr[i]<0:
            li.append(arr[i])
    for i in range (len(arr)):
        if arr[i]>0:
            li.append(arr[i])
    print(li)
    
arr=[15,-3,-2,18]
sorttwotypes(arr)'''


'''def mindifference (arr):
    arr.sort()
    res = float('inf')
    if len(arr)==2:
        return arr[1]-arr[0]
    for i in range (len(arr)-1):
        diff=arr[i+1]-arr[i]
        res=min(res,diff)
    return res

arr=[10,3,20,12]
print(mindifference(arr))'''


'''def countingsort(arr):
    li=[]
    for i in range (len(arr)):
        li.append(arr.count(i))
    return li


arr=[1,4,4,1,0,1]
print(countingsort(arr))'''

'''def countdistinctelement (arr):
    s=[]
    for i in arr:
        if i not in s:
            s.append(i)

    return len(s)

arr=[10,10,10]
print (countdistinctelement(arr))'''

'''def reverse_sentence (str):
    li=[]
    li=str.split(' ')
    li.reverse()
    
str="Welcome to GeeksforGeeks"
reverse_sentence(str)'''

'''def minima(arr):
    for i in range (1,len(arr)-1):
        if (arr[i]<arr[i-1] and arr[i]<arr[i+1]):
            print(arr[i])



arr=[]
print ('Enter a size of array')
n=int(input())
for i in range (0,n):
    arr.append(int(input()))
minima(arr)'''

'''def sortedksizearray(arr,x):
    k=0
    c=0
    arr.sort()
    for i in range (len(arr)):
        k = k + arr[i]
        if (k<x):
            c=c+1
    return c

x=10
arr=[1,5,12,111,200]
print (sortedksizearray(arr,x))'''
'''import math
def medianseries(arr):
    temp=[]
    result=[]
    for i in range (len(arr)):
        temp.append(arr[i])
        if (len(temp)%2!=0):
            temp.sort()
            result.append(temp[math.floor(len(temp)/2)])
        else:
            temp.sort()
            result.append((temp[len(temp)//2]+temp[(len(temp)//2)-1])//2)
    return result

arr=[25,7,10,15,20]
print (medianseries(arr))

import queue
q=queue.Queue()'''
'''from collections import deque
def sortarray(arr):
    queue=deque()
    for i in range (len(arr)):
        if arr[i]%11==0:
            queue.appendleft(arr[i])
        else:
            queue.append(arr[i])
    li=list(queue)
    return li

arr=[1,11,3,45,121]
print(sortarray(arr))'''

'''import os
os.environ['Name']='Archit Shukla'
os.environ['Company']='Publicis Sapient'
os.environ['Password']='Ahq5555'


db_password=os.environ['Password']
print (db_password)
os.environ['Password']='Ahq653'
print ("Modified Password : ",os.environ['Password'])
print (os.environ['Name'])
print (os.environ['Company'])'''



'''import pandas as pd
import matplotlib.pyplot as plt

data={
    "calories":[100,50,120],
    "duration":[50,40,45]
}
df=pd.DataFrame(data)
print(df)'''

'''from graphene import ObjectType , String , Schema
class Query(ObjectType):
    hello=String(name=String(default_value="stranger"))
    goodbye=String()

    def resolve_hello(root,info,name):
        return f'hello{name}!'

    def resolve_goodbye (root,info):
        return 'See ya!'

schema=Schema(query=Query)



query_string = '{ hello }'
result = schema.execute(query_string)
print(result.data['hello'])
# "Hello stranger!"'''


'''def sort_rotated_array(arr):
    li=[]
    for i in range(len(arr)-1):
        if (arr[i]>arr[i+1]):
            li.append(arr[i+1:])
            li.append(arr[0:i+1])
            break
    return li

arr=[2,3,4,1]
print(sort_rotated_array(arr))'''


'''def see(arr):
    k=[0]*len(arr)
    for i in arr:
        k[i]+=1
    for i in range (len(arr)):
        if k[i]==1:
            return i

arr=[1,1,3,3,2,4,4]
print(see(arr))'''

'''import math
def delhivery(arr,n):
    dict={}
    li=[]
    for i in range (len(arr)):
        diff=math.fabs(n-arr[i])
        li.append(diff)
        dict[arr[i]]=diff
    for k,v in dict.items():
        if v==min(li):
            return k
n=11
#arr=[2,5,6,7,8,8,9]
arr=[1,2,4,5,6,6,8,9]
print(delhivery(arr,n))'''

'''def delhivery(arr):
    i=0
    j=len(arr)-1
    left=0
    right=0
    left = left + arr[i]
    right = right + arr[j]
    while (j>0 and i<len(arr)):

        if left >right:
            j = j - 1
            right = right + arr[j]

        elif left < right:
            i = i + 1
            left = left + arr[i]

        elif left==right:
            return "Possible"


    return "Not Possible"

#arr=[1,2,3,4,5,5]
#arr=[4,1,2,3]
arr=[4,3,2,1]
print(delhivery(arr))'''



'''def toptwowords(s):
    l=s.split(" ")
    for i in l:
        h[i]=h[i]+1


h=[]
s = "I am a good boy I I am good am girl "
toptwowords(s)'''

'''To sort the dictionary according to value in revrrse order
dict ={1:2,3:4,4:3,2:1,0:0}
dict =sorted(dict.items(),key=lambda item:item[0],reverse=True)
print (dict)'''


'''def list_comprehension(li):
    return [i*2 for i in li if i%2!=0]

li=[2,5,7,8]
print (list_comprehension(li))'''

'''numbers =[i*10 for i in range (10)]
print (numbers)'''


'''def wrappers (a):
    def add(b):
        c=a+b
        return c
    return add

wrapper=wrappers(10)
print (wrapper(20))'''

'''s="I am the geeky Programmer"
n=s.split(' ')
print (n)
s1=" ".join(n)
print(s1)'''

li=[1,6,3,2,7]
new_li=[i for i in li if i%2==0]
print (new_li)

























