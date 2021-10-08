def days (S,k):
    days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

    dayIndex=days.index(S)
    y=(dayIndex+k)%7
    return days[y]

S="Mon"
k=24
print(days(S,2))


