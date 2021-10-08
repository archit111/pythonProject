list1=[10,20,30]
list2=[9,8,7]
list3=[5,4,3]
result=map(lambda x,y,z:x+y+z,list1,list2,list3)
print(list(result))

lis=[10,20]
result=map(lambda x:pow(x,2),lis)
print(list(result))

li=['aarchit']
result=map(lambda x:set(x), li)
print(list(result))

'''li=[10,20,30]
result=map(lambda x:sum(x), li)
print(list(result))'''

tup=(1,5,7,'archit')
result=map(lambda x:str(x),tup)
print (list(result))

array=[-1,-1,4,5,6]
l=filter((lambda x:x>0),array)
print(list(l))


