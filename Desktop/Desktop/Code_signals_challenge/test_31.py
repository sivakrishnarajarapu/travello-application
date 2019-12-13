def circleOfNumbers(n, firstNumber):
    s = int(n / 2)
    l = []
    for i in range(0, n):
        l.append(i)
    l1 = l[0:s]
    l2 = l[s:]
    for i in range(len(l1)):
        if l1[i] == firstNumber:
            return l2[i]
        else:
            for j in range(len(l2)):
                if l2[j] == firstNumber:
                    return l1[j]
print(circleOfNumbers(10,2))


# num=10
# first_num=2
# l=[]
# index=0
# for i in range(0,num):
#     # print(i)
#     l.append(i)
# print(l)
# n=int(len(l)/2)
# print(n)
# l1=l[0:n]
# l2=l[n::]
# print(l2)
# print(l1)
# for i in range(len(l1)):
#     if l1[i]==2:
#         return l2[i]
#
# print(l2[index])






