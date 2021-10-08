import time
def display_hash(Hashtable):
    for i in range (len(Hashtable)):
        print (i, end=" ")
        for j in Hashtable[i]:
            print ("-->",end=" ")
            print (j,end= " ")
        print()

Hashtable =[[] for _ in range (8)]

def hash_function(value):
    hash_value=hash(value)%8
    return hash_value


def insert(Hashtable,value):
    hashkey=hash_function(value)
    Hashtable[hashkey].append(value)

def accessitem(value):
    start=time.time()
    i=hash_function(value)
    if Hashtable[i]:
        print("Yes")
    else:
        print("No")
    end=time.time()
    print ("Time taken in accessing the element is ",end-start)




insert (Hashtable, 6)
insert (Hashtable , 2.0)
insert (Hashtable , "Shukla")
insert (Hashtable , 87524569)
insert (Hashtable , "Archit")
insert (Hashtable , 20)
insert (Hashtable , 22)
insert (Hashtable , 27)

display_hash(Hashtable)

accessitem("Shukla")