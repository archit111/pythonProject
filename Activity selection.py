'''def activity_selection(arr,n):
    selected=[]
    Activity.sort(key=lambda x:x[1])
    i=0
    selected.append(arr[i])
    c=1
    for j in range(1,n):
        if arr[j][0]>arr[i][1]:
            c=c+1
            selected .append(arr[j])
            i=j
    print('Total',c,'activities are selected')
    return selected

Activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
n=len(Activity)
print(activity_selection(Activity,n))'''

'''Activity = [[5, 9], [1, 2], [3, 4], [0, 6], [5, 7], [8, 9]]
Activity.sort(key=lambda x:x[0])
print(Activity)'''

