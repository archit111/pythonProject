'''lis=[]
print("enter the size of list")
n=int(input())
for i in range(0,n):
    lis.append(input())
lis.sort()
for j in range (0,len(lis)):
    c=1
    for k in range (j+1, len(lis)):
        if lis[j]==lis[k]:
            c=c+1
            print (lis[j],c)   '''


lis=[1,2,3,4,5,6,7,8,9]
li=[2,3,4,7]
'''print("enter the size of list")
n=int(input())
for i in range (0,n):
    li.append(input())'''
for i in li:
    for j in lis:
        if i==j:
            lis.remove(j)
print(lis)



