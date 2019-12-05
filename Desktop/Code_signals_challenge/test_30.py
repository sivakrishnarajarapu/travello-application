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

# def fun(s):
#     open=0
#     # close=0
#     for i in s:
#         if i=="(":
#             open+=1
#         elif i==")":
#             open-=1
#             # close+=1
#         # else:
#         #     pass
#     # k=abs(open-close)
#     k=abs(open)
#     print(k)
# fun("((((0)")


# s=[20,30,53,94]
# s.sort()
# k=reversed(s)
# l=" "
# for i in k:
#     l+=str(i)
# print(l)

# s=[20,35,68]
# k=s[::-1]
# l=""
# print(k)
# for i in k:
#     l=l+str(i)
# print(l)






