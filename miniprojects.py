'''for i in range (0,4):
    print('what number are you thinking ')
    a = int(input())
    if (a % 2 == 0):
        print('Thats an even number!Have another?')
    else:
        print('Thats an odd number!Have another?')'''

'''print('Whats on your mind today')
a=str(input())
a1=" "
c=0
a1=a+" "
for i in range (0,len(a1)):
    b=a1[i]
    if (b==" " or b==','):
        c=c+1
print ('Oh Nice , you just told me whats on your mind in', c , 'words')'''
'''class Profile:

    def checkname(self,a):
        if (a == '*'):
            print('Input is wrong')
            print ('Enter a valid name ')
            return 
        else:
            return a


print('Whats your name')
a = str(input())
ob=Profile()
print (ob.checkname(a))
print('Enter a date of birth')
st=input()
print (st)'''

'''print('Enter the full meaning of Organization or Concept')
st=str(input())
c=""
st1=" "+st
for i in range (0,len(st1)):
    if (st1[i]==" "):
        c=c+st1[i+1]
print(c)'''

'''print ('Enter five words')
#for i in range(0,5):
st1=" "
st=str(input())
for i in range(0,len(st)//2):
    if (st[i]==st[len(st)-(i+1)]):
        print(st,'is a pallindrome')
    print (st,'is not a pallindrome')'''

class Number:

    def __init__(self):
        self.c=0

    def number(self):
        print('Guess  a number between 1 and 50')
        a = int(input())
        if a<1 or a >50 :
            self.c=self.c+1
            print ("Please choose a number within a given range ")
            print ("Wheather you want to play or you want to quit ")
            ch=' '
            ch=str(input())
            if (ch=='p'):
                ob.number()
            elif(ch=='q'):
                return 0
        elif a>=1 and a<=50 :
            self.c=self.c+1
            print ('Congratulations, you completed the game in ',self.c,'round')
            return 1


ob=Number()
k=ob.number()
if(k==1):
    print("Game completed successfully")
elif(k==0):
    print ('Game Quitted')






