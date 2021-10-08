# control structure

#print ('enter a number ')

'''from collections import deque
a=20
if (a%3==0):
    if (a % 5 == 0 and a % 3 == 0):
        print('Zoom')
    else:
        print ('Zip')
elif(a%5==0):
     if (a % 5 == 0 and a % 3 == 0):
         print('Zoom')
     else:
         print('Zap')

else:
    print('Invalid')


list1=[10,20,30,'apple','orange',50,50]

li=deque(list1)

print (len(list1))

list_ele='apple'
if list_ele in list1:
    print ('element found')

else:
    print ('not found ')

list1.append('banana')

list1.insert(1,50)

list1.remove(30)
li.popleft()
li.appendleft(40)
print(list1)
print (li)
li.reverse()
print(li)
list1.reverse()
print (list1)

tupl=(10,30,50,50,'sixty',90,90,90)

print(tupl.count(50))
print (len(tupl))

s=[]




s=set(list1)
print(len(s))'''

'''li=[]
sum=[]
print ("length of list")
n=int(input())
print ('enter numbers')
for i in range(0,n):
    li.append(input())
for i in range (0,len(li)):
    for j in range (i+1,len(li)):
        total=0
        total=total+int(li[i])+int(li[j])
        sum.append(total)
print(max(sum))'''

'''li=[1,1,1,0,1,0,1]
c=-1'''
'''print ("length of array")
n=int(input())
print ('enter numbers only 0 and 1')
for i in range(0,n):
    li.append(input())'''
'''for i in range (0,len(li)):
    if li[i]==0:
        for j in range(i+1, len(li)):
            if li[j]==0:
                break
            else:
                c=c+1
print('Number of 1s between 0 is ',c)'''


'''def findpairs (li,x):
    for i in range (0,len(li)):
        for j in range (i+1,len(li)):
            if (int(li[i])+int(li[j]))==x:
                print(int(li[j]),int(li[i]))
                
                
li=[]
print ("enter size of list")
n=int(input())
for i in range (0,n):
    li.append(input())
print("enter a number")
x=int(input())
findpairs(li,x)'''

'''s='GeeksforGeeks'
s1='Geeksquiz'
li=[]
l=list(s)
l1=list(s1)
for i in l:
    for j in l1:
        if i==j:
            li.append(i)
            break
k = " ".join(li)
print(k)'''

s='aabbcdddaabbe'
visited=[]
for i in s:
    if i not in visited:
        print(i," ",s.count(i))
    visited.append(i)





