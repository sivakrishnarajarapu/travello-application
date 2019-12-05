def addBorder(p):
    l=-1
    l2=[]
    l3=''
    l4=[]
    for i in range(len(p)+2):
        if i in range(1,len(p)+1):
            for j in range(len(p[0])+2):
                if j in range(1,len(p[0])+1):
                    l+=1
                    l3+=str(p[i-1][l])
                else:
                    l3+='*'
            l2.append(l3)
            l3=''
            l=-1
        else:
            for j in range(len(p[0])+2):
                l3+='*'
            l2.append(l3)
            l3 = ''
    l4.extend(l2)
    l2=[]
    return l4
print(addBorder(["abc","def"]))

# def addBorder(a):
#     retlist=[]
#     b =["*"+x+"*" for x in a]
#     l = len(b[0])
#     st = "*"*l
#     retlist.append(st)
#     retlist.extend(b)
#     retlist.append(st)
#     return retlist
# print(addBorder(["abc","def"]))

# def increment_last(st):
#     x = int(st[-3:])+1
#     x = str(x)
#     y = "0"*(3-len(x))+x
#     st = st[:-3] + y
#     return st

# print(increment_last("fakhkajnfkj_123"))
#
# def sumlist(lst,k):
#     return [(i,j) for i in lst for j in lst if i+j == k]
#
# x = sumlist([1,2,3,4,5,6],5)
# print(x)