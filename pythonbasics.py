'''def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase
    return wrapper

def splitter_decorator(function):
    def wrapper():
        func=function()
        string_split=func.split()
        return string_split
    return wrapper'''

lis=[10,21,31,42]

squared_list=[x**2 for x in lis]#list comprehension
print(squared_list)

squared_dict={x:x**2 for x in lis}#dictionary comprehension
print(squared_dict)


squared_lis1=map(lambda x:x*x,lis)#mapping in python
print(list(squared_lis1))

#type()
#isinstance()
s=set()
s.add("Google")
s.add("Microsoft")
s.add("lInfosys")
s.add("Amazon")
print(s)
s.remove("Microsoft")
print(s)


def emptyfunc():
    pass

emptyfunc()
from copy import copy,deepcopy
lis1=[2,5,8]
lis2=copy(lis1)
print(lis1)
print(lis2)
lis2[1]=3
print(lis1)
print(lis2)
lis2.append(4)
print(lis1)
print(lis2)

def arrnum(arr):#call by reference
    arr.append(6)

arr=[1,2,30]
print(arr)
arrnum(arr)
print(arr)


class ArrayList:
    def __init__(self,number_list):
        self.numbers=number_list

    def __iter__(self):
        self.pos=0
        return self

    def __next__(self):
        if (self.pos <len(self.numbers)):
            self.pos+=1
            return self.numbers[self.pos-1]
        else:
            raise StopIteration

arr_obj=ArrayList([1,2,3])

it=iter(arr_obj)
print(next(it))
print(next(it))
print(next(it))
#print(next(it))

#How to run python script on unix
#!usr/bin/env python

#How to delete a file in python
#import os
#os.remove("Filename")

string ="This is :a string"
str=string .split(" ")
print(str)
print(" ".join(str))

def multiple(a,b,*args):
    mul=a*b

    for i in args:
        mul*=i

    return mul

print(multiple(1,2,3,4,7))
#args is used tp pass variable length argument
#kargs is used to pass variable length keyworded argument (mainly dictionary of variables name which has its value )




