n=int(input())
c=0
sum=0
sum1=0
'''while (n>0):
    n=n//10
    c=c+1'''
while(n>0):
    sum=sum+n%10
    n=n//10
while(sum>0):
    sum1=sum1+sum%10
    sum=sum//10
print(sum1)

