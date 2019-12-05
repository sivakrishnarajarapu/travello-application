# def sortByHeight(a):
#     l = sorted([i for i in a if i > 0])
#     for n,i in enumerate(a):
#         if i == -1:
#             l.insert(n,i)
#     return l
# print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))



def sortByHeight(a):
    l1=[]
    l2=[]
    l4=[]
    c=-1
    for i in range(len(a)):
        if a[i]==-1:
            l1.append(i)
        else:
            l2.append(a[i])
    l3=sorted(l2)
    for j in range(len(a)):
        # k=j
        if j in l1:
            l4.append(-1)
        else:
            c+=1
            l4.append(l3[c])
    return l4
print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))

