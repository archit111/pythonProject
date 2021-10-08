#to find the square root of number
'''def square_root(n):
    for i in range (n//2):
        if (i*i==n):
            return i


print ("enter a number ")
x=int(input())
print(square_root(x))'''

# to find the row with maximum number of 1's
def maximum_ones(arr):
    dict={}
    for i in range (len(arr)):
        c=0
        for j in range (len(arr)):
            if arr[i][j]==1:
                c=c+1
        dict[i]=c

    row=max(dict,key=dict.get)
    return row


arr = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]
print ("Index of row with maximum 1s is",
      maximum_ones(arr))


