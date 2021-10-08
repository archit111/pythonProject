'''empty_tuple =()
print (empty_tuple )
tuple =("Geeks","for","geeks")
print (tuple)
print (len(tuple))
tuple1=("concatenation","Hello")
tuple2= tuple +tuple1
print(tuple2[1:3])

list1=[1,2,2,3,4,5,6,4]
s=set(list1)
for i in s:
    print (i,end=" " )
print (" ")
s.add(9)
s.add(10)
for i in s:
    print (i,end=" " )
s.remove(9)
print(s)'''
from _ast import slice
from builtins import int
'''from threading import Thread
from time import sleep

def threaded_function(arg):
    for i in range (arg):
        print ("running")

        sleep(1)
if __name__=="__main__":
    t1=Thread(target=threaded_function,args=(5,))
    t1.start()
    t1.join()
    print ("Thread finish exiting ")'''

'''import json
dictionary={"name":"archit","department":"IT"}


json_object=json.dumps(dictionary,indent=2)
print (json_object)'''

dict={1:"Geeks",2:"for",3:{"Name":"Archit"}}
print(dict)
dict[2]="Archit"
print(dict[3]["Name"])

print (dict.pop(1))
dict[6]="archit"
print(dict)

s=set()
s.add(4)
s.add(1)
i=4