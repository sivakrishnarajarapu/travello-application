# # def areSimilar(a,b):
# a=[1,2,3,4,6]
# b=[1,2,3,4,6]
# l1=[]
# l3=[]
# l5=[]
# c=0
# for i in range(len(a)):
#     if a[i]==b[i]:
#         l1.append(i)
#     else:
#         l3.append(a[i])
# l4=list(reversed(l3))
# # print(l4)
# for j in range(len(a)):
#     if j in l1:
#         l5.append(a[j])
#     else:
#         # c+=1
#         l5.append(l4[c])
#         c+=1
# print(l5)
# if l5==b:
#     print("True")
# else:
#     print("False")
#
# # areSimilar([1,2,3],[1,2,3])


def fun(a,b):
    d=[]
    if a!=b:
        if len(a)==len(b):
            for i in range(len(a)):
                if a[i]!=b[i]:
                    d.append(i)
                    print(d)
        else:
            return False
        if len(d)==2 and a[d[0]]==b[d[1]] and a[d[1]]==b[d[0]]:
            return True
        else:
            return False
    else:
        return True
print(fun([1,2,3],[2,1,3]))
