#https://realpython.com/python-pickle-module/
#https://www.geeksforgeeks.org/understanding-python-pickling-example/
import pickle
class my_example:
    a_number=123
    a_str="Ramesh"
    a_lis=[1,2,3]
    a_dict={"first":"a","second":2,"third":[1,2,3]}
    a_tuple=(10,12)
    db={}
    db["a_number"]=a_lis


    my_object_serial=pickle.dumps(db)
    print(my_object_serial)


    my_object_unserial=pickle.loads(my_object_serial)
    print(my_object_unserial)



