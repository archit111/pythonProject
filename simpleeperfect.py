'''lis=[]
n=0
s=0
for i in range (5):
    lis.append(int(input()))
s=sum(lis)
n=s/len(lis)
print(n)'''

#To extract useful data from user

'''stri="archit architshukla93@gmail.com 110619960"
str=stri.split('@')
print(str[0])'''


'''def Prime_Game(L,R):
    diff=0
    li=[]

 # Write code here
    for i in range (L,R+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c=c+1
        if c==2:
            li.append(i)
            break


    for i in range (R,L-1,-1):
        c=0
        for j in range (1,i+1):
            if i%j==0:
                c=c+1
        if c==2:
            li.append(i)
            break

    if len(li)==0:
        return -1
    else:

        diff = li[len(li) - 1] - li[0]

        if diff > 0:
            return diff
        elif diff == 0:
            return 0



i=int(input())
j=int(input())
print(Prime_Game(i,j))'''

'''def nthhighest_dict(dict,n):

    li=[]
    for i in sorted(dict.values(),reverse=True):
        li.append(i)
    for i in range(len(li)):
        if i==n:
            print(li[n])

n=int(input())
dict={1:50,3:10,2:20,8:85,5:25}
nthhighest_dict(dict,n)'''

'''word="archit is a good boy"
str=" "
lis=word.split(" ")
for i in lis:
    str=i+str
print(str)'''

p=int(input())
count=0
n=0

while count<=p:
    ele=5*n+2
    if (ele%4==0):
        count+=1
        n+=1
        continue
    else:
        count+=1
        n+=1
        print(ele)

