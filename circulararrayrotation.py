
#O(n^2) compleity
def circularArrayRotation(a, k, queries):
    l=[]
    for i in range(0, k):
        digit = 0
        for j in range(len(a) - 1, -1, -1):
            if (j == len(a) - 1):
                digit = a[j]
                a[j] = a[j - 1]
            if (j == 0):
                a[j] = digit
                break
            a[j] = a[j - 1]

    for i in queries:
        l.append(a[i])

    return a

queries=[1,2]
a=[1,2,3,4,5,6,7]
k=3
print(circularArrayRotation(a,k,queries))

#O(n) complexity
'''def circularArrayRotation(a, k, queries):
    l=[]
    for i in range(0, k):
        q=rotationbyone(a,queries)
        if i==k-1:
            for i in queries:
                l.append(q[i])
            return l

def rotationbyone(a,queries):
    l=[]
    digit=0
    for j in range(len(a) - 1, -1, -1):
        if (j == len(a) - 1):
            digit = a[j]
            a[j] = a[j - 1]
        if (j == 0):
            a[j] = digit
            break
        a[j] = a[j - 1]

    return a
queries=[1,2]
a=[3,4,5]
k=2
print(circularArrayRotation(a,k,queries))'''