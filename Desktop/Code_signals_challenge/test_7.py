# l=[1,3,2,1]

# def fun(l):
#     drop=False
#     last=prev=min(l)-1
#     for i in l:
#         if i<=last:
#             if drop:
#                 return False
#             else:
#                 drop = True
#         if i<=prev:
#             prev=last
#         elif i>=prev:
#             prev=last=i
#         else:
#             prev , last = last , i
#     return True
# print(fun([1,3,2]))


# ls=[1,3,2,]
#
# def fun(ls):
#     count = 0
#     for i in range(len(ls)):
#          l3 = ls[:i]+ls[i+1:]
#          if sorted(l3)==l3:
#             count+=1
#          else:
#              pass
#     if count!=0:
#         print("Strictly increasing order")
#     else:
#         print("List is not in order")
# fun(ls)


# def fun(ls):
#     for i in range(len(ls)):
#          l3 = ls[:i]+ls[i+1:]
#          if sorted(list(set(l3)))==l3:
#              return True
#     return False
#
# ls=[1,2,1,2]
# print(fun(ls))


# def almostIncreasingSequence(s):
#     return 3> sum((i >= j) + (i >= k) for i, j, k in zip(s, s[1:], s[2:] + [10**6]))
# print(almostIncreasingSequence([10,2,3,4,5,1]))



