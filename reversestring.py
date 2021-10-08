'''def reverse_string(str):
    l=len(str)

    rev_str=" "

    for i in range (0,l):
        if str[i]!=" ":
            word =""
            word=word+str[i]
        rev_str=word+rev_str

    return rev_str



print ("Enter a string ")
str=str(input())
print(reverse_string(str))'''

def anagram (st,str1):
    if len(st)!=len(str1):
        return False
    c=0
    for i in st:
        for j in str1:
            if i==j:
                c=c+1
    if c==len(st):
        return True
    return False







print("Enter a first string ")
st = str(input())
print ("enter a second string")
str1 = str(input())
print(anagram(st,str1))