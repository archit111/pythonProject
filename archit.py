'''print ("enter the number of elements to be inserted in a list")
n=int(input())
li=[]
for i in range (0,n):
    li.append(input())
li.sort()
print (li)'''

dict={1:'zebra',2:'orange',3:'mango'}
'''for k,v in dict.items():
    print (k,v)'''
'''li=[]
for i  in range (0,len(dict)):
    li.append(dict.get())'''
'''l=[]
for key,value  in dict.items():
    l=list(dict.values())

print (l)
l.sort()
print (l)

lii=[]
tu=(1,5,8,9,0,7,6,2,9)
lii=list(tu)
print ("enter the index upto which you need tuple to get it sort")
i=int(input())
for i in range(i+1,len(lii)):
    lii.pop()
lii.sort()
print (lii)'''

def cube (y):
    x=y*y*y
    return x

lambda_cube=lambda y:y*y*y

print(cube(5))
print(lambda_cube(7))


li=[5,8,2,14,7,17,24]

final_list=list(filter(lambda x:(x%2!=0),li))
print(final_list)

final_list1=list(filter(lambda x:(x%2==0),li))
print (final_list1)

ages = [13, 90, 17, 59, 21, 60, 5]
final_list2=list(filter(lambda x :(x>18),ages))
print(final_list2)


final_list3=list(map(lambda x:(2*x),ages))
print(final_list3)

animals = ['dog', 'cat', 'parrot', 'rabbit']
final=list(map(lambda x:(x.upper()),animals))
print(final)

from functools import reduce
li1=[5,8,10,20]
fi=reduce((lambda x,y:x+y),li1)
fi1=reduce((lambda x,y:y if x>y else x),li1)
print(fi)
print(fi1)

my_list = [12, 65, 54, 39, 102,339, 221, 50, 70]
my_lamb=list(filter(lambda x:(x%13==0),my_list))
print(my_lamb)

my_list = ["geeks", "geeg", "keek", "practice", "aa"]
a=list(filter(lambda x:(x=="".join(reversed(x))),my_list))
print (a)

from collections import Counter
my_list = ["geeks", "geeg", "keegs", "practice", "aa"]
str = "eegsk"
a=list(filter(lambda x:(Counter(x)==Counter(str)),my_list))
print (a)


my_list = [12, 65, 54, 39, 102,339, 221, 50, 70]
b=reduce(lambda x,y:(x+y),my_list)/len(my_list)
print(b)


def intersection(arr1, arr2):
    result=list(filter(lambda x:x in arr1, arr2))
    print(result)


arr1=[3,5,7,8]
arr2=[2,4,6,8,5]
intersection (arr1,arr2)





