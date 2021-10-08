'''list11 = [1, 5, 'apple', 9, 'orange', 10, 'mango']
for i in list11:
    temp = 0
    temp = list11[len(list11) - 1]
    list11[len(list11) - 1] = list11[0]
    list11[0] = temp
print(list11)


def merge (dict1,dict2 ):


    return (dict1.update(dict2))


dict1={1:'a',2:'b'}
dict2={5:'orange '}
print (merge(dict1, dict2))
print (dict1)



k=int(input())
tup=(5,7,7,6,9,8)
list1=list(tup)
print (list1[0:len(list1)-k])



def rev(list2):
    temp = 0
    temp = list2[-1]
    list2[-1] = list2[0]
    list2[0] = temp
    return list2

list2= [1,5,'apple',9,'orange',10,'mango']
print(rev(list2))'''







def findDigits(n):
    c=0
    try:
        temp = n
        while (temp > 0):
            rem = temp % 10
            if n % rem == 0:
                c = c + 1
                print(c)
            temp = temp // 10
    except ZeroDivisionError:
        return



findDigits(1201)