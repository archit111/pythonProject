def longest_common_subsequence(wrd1,wrd2):
    m=len(wrd1)
    n=len(wrd2)
    l= [[None] * (n + 1) for i in range(m + 1)]
    for i in range (m+1):
        for j in range (n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif wrd1[i-1]==wrd2[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])

    return l[m][n]

wrd1='abcd'
wrd2='axbxc'
print(longest_common_subsequence(wrd1,wrd2))