def longest_increasing_subsequence(lis1):
    lis=[]*len(lis1)
    max=0
    for i in range (0,len(lis1)):
        lis.append(1)
    for i in range (1,len(lis1)):
        for j in range(0,len(lis1)):
            if (lis1[i]>lis1[j] and lis[j]+1>lis[i]):
                lis[i]=lis[j]+1
    for i in range (len(lis)):
        if max<lis[i]:
            max=lis[i]

    return max

lis1=[10,22,9,33,21,50,41,60]
print(longest_increasing_subsequence(lis1))